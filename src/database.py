import sqlite3
import hashlib
import json
from datetime import datetime
from pathlib import Path


# ============================================================
# DATABASE PATH
# ============================================================

DATABASE_PATH = Path("/tmp/securenet.db")


# ============================================================
# DATABASE CONNECTION
# ============================================================

def get_connection():
    connection = sqlite3.connect(DATABASE_PATH)
    connection.row_factory = sqlite3.Row
    return connection


# ============================================================
# INITIALIZE DATABASE
# ============================================================

def initialize_database():

    DATABASE_PATH.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    connection = get_connection()

    cursor = connection.cursor()

    # --------------------------------------------------------
    # USERS TABLE
    # --------------------------------------------------------

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            full_name TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE,
            password_hash TEXT NOT NULL,
            created_at TEXT NOT NULL
        )
        """
    )

    # --------------------------------------------------------
    # ANALYSES TABLE
    # --------------------------------------------------------

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS analyses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            filename TEXT NOT NULL,
            analyzed_at TEXT NOT NULL,
            total_records INTEGER NOT NULL,
            normal_count INTEGER NOT NULL,
            attack_count INTEGER NOT NULL,
            intrusion_rate REAL NOT NULL,
            category_counts TEXT NOT NULL,
            FOREIGN KEY (user_id) REFERENCES users(id)
        )
        """
    )

    connection.commit()
    connection.close()

# ============================================================
# PASSWORD HASHING
# ============================================================

def hash_password(password):
    return hashlib.sha256(
        password.encode("utf-8")
    ).hexdigest()


# ============================================================
# CREATE USER
# ============================================================

def create_user(full_name, email, password):

    connection = get_connection()

    try:
        cursor = connection.cursor()

        password_hash = hash_password(password)

        cursor.execute(
            """
            INSERT INTO users (
                full_name,
                email,
                password_hash,
                created_at
            )
            VALUES (?, ?, ?, ?)
            """,
            (
                full_name,
                email.lower(),
                password_hash,
                datetime.now().isoformat(),
            ),
        )

        connection.commit()

        return cursor.lastrowid

    except sqlite3.IntegrityError:
        return None

    finally:
        connection.close()


# ============================================================
# GET USER BY EMAIL
# ============================================================

def get_user_by_email(email):

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute(
        """
        SELECT *
        FROM users
        WHERE email = ?
        """,
        (email.lower(),),
    )

    user = cursor.fetchone()

    connection.close()

    return user


# ============================================================
# VERIFY LOGIN
# ============================================================

def verify_user(email, password):

    user = get_user_by_email(email)

    if user is None:
        return None

    password_hash = hash_password(password)

    if user["password_hash"] != password_hash:
        return None

    return user

# ============================================================
# RESET USER PASSWORD
# ============================================================

def reset_user_password(full_name, email, new_password):

    connection = get_connection()

    try:
        cursor = connection.cursor()

        cursor.execute(
            """
            SELECT id
            FROM users
            WHERE LOWER(email) = ?
            AND LOWER(full_name) = ?
            """,
            (
                email.strip().lower(),
                full_name.strip().lower(),
            ),
        )

        user = cursor.fetchone()

        if user is None:
            return False

        new_password_hash = hash_password(
            new_password
        )

        cursor.execute(
            """
            UPDATE users
            SET password_hash = ?
            WHERE id = ?
            """,
            (
                new_password_hash,
                user["id"],
            ),
        )

        connection.commit()

        return True

    finally:
        connection.close()

def save_analysis(
    user_id,
    filename,
    total_records,
    normal_count,
    attack_count,
    intrusion_rate,
    category_counts,
):
    connection = get_connection()

    try:
        cursor = connection.cursor()

        cursor.execute(
            """
            INSERT INTO analyses (
                user_id,
                filename,
                analyzed_at,
                total_records,
                normal_count,
                attack_count,
                intrusion_rate,
                category_counts
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                user_id,
                filename,
                datetime.now().isoformat(),
                total_records,
                normal_count,
                attack_count,
                intrusion_rate,
                json.dumps(category_counts),
            ),
        )

        connection.commit()

        return cursor.lastrowid

    finally:
        connection.close()

def get_latest_analysis(user_id):
    connection = get_connection()

    try:
        cursor = connection.cursor()

        cursor.execute(
            """
            SELECT *
            FROM analyses
            WHERE user_id = ?
            ORDER BY analyzed_at DESC
            LIMIT 1
            """,
            (user_id,),
        )

        return cursor.fetchone()

    finally:
        connection.close()

def get_user_analyses(user_id):
    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute(
        """
        SELECT
            id,
            filename,
            analyzed_at,
            total_records,
            normal_count,
            attack_count,
            intrusion_rate,
            category_counts
        FROM analyses
        WHERE user_id = ?
        ORDER BY analyzed_at DESC
        """,
        (user_id,),
    )

    analyses = cursor.fetchall()

    connection.close()

    return [dict(row) for row in analyses]