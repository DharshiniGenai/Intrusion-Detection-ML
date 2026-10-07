import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
# NSL-KDD column names
COLUMNS = [
    "duration",
    "protocol_type",
    "service",
    "flag",
    "src_bytes",
    "dst_bytes",
    "land",
    "wrong_fragment",
    "urgent",
    "hot",
    "num_failed_logins",
    "logged_in",
    "num_compromised",
    "root_shell",
    "su_attempted",
    "num_root",
    "num_file_creations",
    "num_shells",
    "num_access_files",
    "num_outbound_cmds",
    "is_host_login",
    "is_guest_login",
    "count",
    "srv_count",
    "serror_rate",
    "srv_serror_rate",
    "rerror_rate",
    "srv_rerror_rate",
    "same_srv_rate",
    "diff_srv_rate",
    "srv_diff_host_rate",
    "dst_host_count",
    "dst_host_srv_count",
    "dst_host_same_srv_rate",
    "dst_host_diff_srv_rate",
    "dst_host_same_src_port_rate",
    "dst_host_srv_diff_host_rate",
    "dst_host_serror_rate",
    "dst_host_srv_serror_rate",
    "dst_host_rerror_rate",
    "dst_host_srv_rerror_rate",
    "attack",
    "difficulty"
]
# Map individual NSL-KDD attacks to broader attack categories
ATTACK_CATEGORIES = {
    # Denial of Service (DoS)
    "back": "DoS",
    "land": "DoS",
    "neptune": "DoS",
    "pod": "DoS",
    "smurf": "DoS",
    "teardrop": "DoS",
    "apache2": "DoS",
    "processtable": "DoS",
    "mailbomb": "DoS",
    "udpstorm": "DoS",
    "worm": "DoS",

    # Probe
    "ipsweep": "Probe",
    "nmap": "Probe",
    "portsweep": "Probe",
    "satan": "Probe",
    "mscan": "Probe",
    "saint": "Probe",

    # Remote to Local (R2L)
    "ftp_write": "R2L",
    "guess_passwd": "R2L",
    "imap": "R2L",
    "multihop": "R2L",
    "phf": "R2L",
    "spy": "R2L",
    "warezclient": "R2L",
    "warezmaster": "R2L",
    "snmpguess": "R2L",
    "snmpgetattack": "R2L",
    "httptunnel": "R2L",
    "named": "R2L",
    "sendmail": "R2L",
    "xlock": "R2L",
    "xsnoop": "R2L",
    "sqlattack": "R2L",

    # User to Root (U2R)
    "buffer_overflow": "U2R",
    "loadmodule": "U2R",
    "perl": "U2R",
    "rootkit": "U2R",
    "ps": "U2R",
    "xterm": "U2R",

    # Normal traffic
    "normal": "Normal",
}
CATEGORICAL_FEATURES = [
    "protocol_type",
    "service",
    "flag",
]

TARGET_COLUMN = "category"

DROP_COLUMNS = [
    "attack",
    "category",
    "difficulty",
]

TRAIN_PATH = "data/KDDTrain+.txt"
TEST_PATH = "data/KDDTest+.txt"


def load_data():
    train = pd.read_csv(TRAIN_PATH, header=None, names=COLUMNS)
    test = pd.read_csv(TEST_PATH, header=None, names=COLUMNS)

    train["category"] = train["attack"].map(ATTACK_CATEGORIES)
    test["category"] = test["attack"].map(ATTACK_CATEGORIES)

    return train, test

def create_preprocessor():
    numerical_features = [
        column
        for column in COLUMNS
        if column not in CATEGORICAL_FEATURES
        and column not in DROP_COLUMNS
    ]

    preprocessor = ColumnTransformer(
        transformers=[
            (
                "categorical",
                OneHotEncoder(handle_unknown="ignore"),
                CATEGORICAL_FEATURES,
            ),
            (
                "numerical",
                StandardScaler(),
                numerical_features,
            ),
        ]
    )

    return preprocessor


if __name__ == "__main__":
    train, test = load_data()

    print("Train shape:", train.shape)
    print("Test shape:", test.shape)

    print("\nCategory distribution:")
    print(train["category"].value_counts())

    print("\nUnknown attack labels:")
    print(train.loc[train["category"].isna(), "attack"].unique())