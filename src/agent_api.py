
import os
import hmac
from datetime import datetime, timezone

from fastapi import FastAPI, Header, HTTPException, Query
from pydantic import BaseModel, Field

from src.database import (
    initialize_database,
    save_live_detections,
    get_recent_live_detections,
)

app = FastAPI(
    title="SecureNet AI Agent API",
    version="1.0.0",
)

AGENT_API_TOKEN = os.getenv("AGENT_API_TOKEN", "")

# Create the tables if they do not exist.
initialize_database()


class FlowDetection(BaseModel):
    src_ip: str = Field(max_length=45)
    dst_ip: str = Field(max_length=45)
    src_port: int = Field(ge=0, le=65535)
    dst_port: int = Field(ge=0, le=65535)
    protocol: str = Field(max_length=20)
    packet_count: int = Field(ge=0)
    src_bytes: int = Field(ge=0)
    dst_bytes: int = Field(ge=0)
    prediction: str
    confidence: float = Field(ge=0, le=100)


class AgentReport(BaseModel):
    agent_id: str = Field(min_length=1, max_length=100)
    detections: list[FlowDetection] = Field(max_length=200)


def verify_agent(authorization: str):
    token = os.getenv("AGENT_API_TOKEN", "")

    if not token:
        raise HTTPException(
            status_code=503,
            detail="Agent API authentication is not configured.",
        )

    expected = f"Bearer {token}"

    if not hmac.compare_digest(authorization, expected):
        raise HTTPException(
            status_code=401,
            detail="Invalid agent credentials.",
        )


@app.get("/health")
def health():
    return {
        "status": "ok",
        "service": "SecureNet AI Agent API",
    }


@app.post("/api/agent/detections")
def receive_detections(
    report: AgentReport,
    authorization: str = Header(default=""),
):
    verify_agent(authorization)

    for detection in report.detections:
        if detection.prediction not in {"Normal", "Attack"}:
            raise HTTPException(
                status_code=422,
                detail="Prediction must be Normal or Attack.",
            )

    count = save_live_detections(
        report.agent_id,
        [detection.model_dump() for detection in report.detections],
    )

    return {
        "status": "accepted",
        "agent_id": report.agent_id,
        "received": count,
        "received_at": datetime.now(timezone.utc).isoformat(),
    }


@app.get("/api/agent/detections")
def list_detections(
    authorization: str = Header(default=""),
    limit: int = Query(default=100, ge=1, le=500),
):
    verify_agent(authorization)

    detections = get_recent_live_detections(limit=limit)

    return {
        "count": len(detections),
        "detections": detections,
    }
