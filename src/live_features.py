from collections import defaultdict
from datetime import datetime

from scapy.layers.inet import IP, TCP, UDP


def _protocol_name(packet):
    """Return the network protocol name."""
    if TCP in packet:
        return "tcp"
    if UDP in packet:
        return "udp"
    if IP in packet:
        return str(packet[IP].proto)
    return "other"


def _packet_size(packet):
    """Return the total packet size in bytes."""
    try:
        return len(packet)
    except Exception:
        return 0


def _packet_timestamp(packet):
    """Return the packet timestamp as a float."""
    try:
        return float(packet.time)
    except Exception:
        return datetime.now().timestamp()


def _flow_key(packet):
    """
    Create a bidirectional flow key.

    Packets travelling in either direction belong to the same flow.
    """
    if IP not in packet:
        return None

    src_ip = packet[IP].src
    dst_ip = packet[IP].dst

    if TCP in packet:
        src_port = int(packet[TCP].sport)
        dst_port = int(packet[TCP].dport)
        protocol = "tcp"
    elif UDP in packet:
        src_port = int(packet[UDP].sport)
        dst_port = int(packet[UDP].dport)
        protocol = "udp"
    else:
        src_port = 0
        dst_port = 0
        protocol = _protocol_name(packet)

    endpoint_a = (src_ip, src_port)
    endpoint_b = (dst_ip, dst_port)

    endpoints = tuple(sorted((endpoint_a, endpoint_b)))

    return protocol, endpoints


def extract_flow_features(packets):
    """
    Convert captured packets into flow-level network features.

    Only packet and connection metadata is used.
    Application payload contents are not stored or inspected.

    Returns:
        List of dictionaries containing extracted flow features.
    """
    flows = defaultdict(
        lambda: {
            "protocol": "other",
            "src_ip": "",
            "dst_ip": "",
            "src_port": 0,
            "dst_port": 0,
            "start_time": None,
            "end_time": None,
            "packet_count": 0,
            "src_packets": 0,
            "dst_packets": 0,
            "src_bytes": 0,
            "dst_bytes": 0,
            "tcp_syn": 0,
            "tcp_ack": 0,
            "tcp_fin": 0,
            "tcp_rst": 0,
            "tcp_psh": 0,
            "tcp_urg": 0,
            "min_packet_size": None,
            "max_packet_size": 0,
        }
    )

    for packet in packets:
        if IP not in packet:
            continue

        key = _flow_key(packet)

        if key is None:
            continue

        flow = flows[key]

        timestamp = _packet_timestamp(packet)
        packet_size = _packet_size(packet)

        src_ip = packet[IP].src
        dst_ip = packet[IP].dst

        flow["protocol"] = _protocol_name(packet)

        if flow["start_time"] is None:
            flow["start_time"] = timestamp

        flow["end_time"] = timestamp
        flow["packet_count"] += 1

        if not flow["src_ip"]:
            flow["src_ip"] = src_ip
            flow["src_port"] = (
                int(packet[TCP].sport)
                if TCP in packet
                else int(packet[UDP].sport)
                if UDP in packet
                else 0
            )

        if not flow["dst_ip"]:
            flow["dst_ip"] = dst_ip
            flow["dst_port"] = (
                int(packet[TCP].dport)
                if TCP in packet
                else int(packet[UDP].dport)
                if UDP in packet
                else 0
            )

        if src_ip == flow["src_ip"]:
            flow["src_packets"] += 1
            flow["src_bytes"] += packet_size
        else:
            flow["dst_packets"] += 1
            flow["dst_bytes"] += packet_size

        flow["min_packet_size"] = (
            packet_size
            if flow["min_packet_size"] is None
            else min(flow["min_packet_size"], packet_size)
        )

        flow["max_packet_size"] = max(
            flow["max_packet_size"],
            packet_size
        )

        if TCP in packet:
            flags = packet[TCP].flags

            if flags & 0x02:
                flow["tcp_syn"] += 1

            if flags & 0x10:
                flow["tcp_ack"] += 1

            if flags & 0x01:
                flow["tcp_fin"] += 1

            if flags & 0x04:
                flow["tcp_rst"] += 1

            if flags & 0x08:
                flow["tcp_psh"] += 1

            if flags & 0x20:
                flow["tcp_urg"] += 1

    results = []

    for flow in flows.values():
        duration = 0.0

        if (
            flow["start_time"] is not None
            and flow["end_time"] is not None
        ):
            duration = max(
                0.0,
                flow["end_time"] - flow["start_time"]
            )

        results.append(
            {
                "src_ip": flow["src_ip"],
                "dst_ip": flow["dst_ip"],
                "src_port": flow["src_port"],
                "dst_port": flow["dst_port"],
                "protocol": flow["protocol"],
                "duration": duration,
                "packet_count": flow["packet_count"],
                "src_packets": flow["src_packets"],
                "dst_packets": flow["dst_packets"],
                "src_bytes": flow["src_bytes"],
                "dst_bytes": flow["dst_bytes"],
                "tcp_syn": flow["tcp_syn"],
                "tcp_ack": flow["tcp_ack"],
                "tcp_fin": flow["tcp_fin"],
                "tcp_rst": flow["tcp_rst"],
                "tcp_psh": flow["tcp_psh"],
                "tcp_urg": flow["tcp_urg"],
                "min_packet_size": flow["min_packet_size"] or 0,
                "max_packet_size": flow["max_packet_size"],
            }
        )

    return results