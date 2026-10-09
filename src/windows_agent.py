
import os
import time
import requests

from src.live_detector import analyze_live_traffic


API_URL = os.getenv(
    "AGENT_API_URL",
    "http://127.0.0.1:8001/api/agent/detections",
)

AGENT_ID = os.getenv(
    "AGENT_ID",
    "windows-agent-01",
)

API_TOKEN = os.getenv("AGENT_API_TOKEN", "")

PACKET_COUNT = 50
CAPTURE_TIMEOUT = 20
RETRY_DELAY = 5


def send_detections(detections):
    if not API_TOKEN:
        raise RuntimeError(
            "AGENT_API_TOKEN is not configured."
        )

    headers = {
        "Authorization": f"Bearer {API_TOKEN}",
        "Content-Type": "application/json",
    }

    payload = {
        "agent_id": AGENT_ID,
        "detections": detections,
    }

    response = requests.post(
        API_URL,
        json=payload,
        headers=headers,
        timeout=15,
    )

    response.raise_for_status()
    return response.json()


def run_agent():
    print("=" * 55)
    print("SecureNet AI - Windows Detection Agent")
    print(f"Agent ID: {AGENT_ID}")
    print(f"API: {API_URL}")
    print("Press Ctrl+C to stop.")
    print("=" * 55)

    while True:
        try:
            print(
                f"\nCapturing up to {PACKET_COUNT} packets "
                f"for {CAPTURE_TIMEOUT} seconds..."
            )

            detections = analyze_live_traffic(
                count=PACKET_COUNT,
                timeout=CAPTURE_TIMEOUT,
            )

            if not detections:
                print("No flows detected in this capture.")
                continue

            result = send_detections(detections)

            print(
                f"Submitted: {result['received']} detections"
            )

            for item in detections:
                print(
                    f"{item['src_ip']} -> {item['dst_ip']} | "
                    f"{item['protocol']} | "
                    f"{item['prediction']} | "
                    f"{item['confidence']}%"
                )

        except KeyboardInterrupt:
            print("\nAgent stopped.")
            break

        except requests.RequestException as exc:
            print(f"API submission failed: {exc}")
            time.sleep(RETRY_DELAY)

        except Exception as exc:
            print(f"Detection error: {exc}")
            time.sleep(RETRY_DELAY)


if __name__ == "__main__":
    run_agent()
