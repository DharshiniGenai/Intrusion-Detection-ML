from collections import OrderedDict

import pandas as pd


LIVE_NUMERIC_FEATURES = [
    "duration",
    "src_bytes",
    "dst_bytes",
    "src_dst_byte_ratio",
    "byte_rate",
    "packets_per_second",
    "src_packets",
    "dst_packets",
    "tcp_syn",
    "tcp_ack",
    "tcp_fin",
    "tcp_rst",
    "tcp_psh",
    "tcp_urg",
    "min_packet_size",
    "max_packet_size",
    "bytes_per_packet",
    "syn_ratio",
    "rst_ratio",
]


def build_live_features(flows):
    """
    Convert extracted network flows into a consistent live
    feature representation.

    The live feature set is derived only from observable
    packet and flow metadata. It is separate from the
    NSL-KDD 41-feature representation used by dataset mode.
    """
    rows = []

    for flow in flows:
        duration = max(float(flow.get("duration", 0.0)), 0.0)
        packet_count = max(int(flow.get("packet_count", 0)), 0)

        src_packets = max(int(flow.get("src_packets", 0)), 0)
        dst_packets = max(int(flow.get("dst_packets", 0)), 0)

        src_bytes = max(int(flow.get("src_bytes", 0)), 0)
        dst_bytes = max(int(flow.get("dst_bytes", 0)), 0)

        tcp_syn = max(int(flow.get("tcp_syn", 0)), 0)
        tcp_rst = max(int(flow.get("tcp_rst", 0)), 0)

        total_bytes = src_bytes + dst_bytes

        bytes_per_packet = (
            total_bytes / packet_count
            if packet_count > 0
            else 0.0
        )

        packets_per_second = (
            packet_count / duration
            if duration > 0
            else 0.0
        )

        byte_rate = (
            total_bytes / duration
            if duration > 0
            else float(total_bytes)
        )

        src_dst_byte_ratio = (
            src_bytes / dst_bytes
            if dst_bytes > 0
            else float(src_bytes)
        )

        syn_ratio = (
            tcp_syn / packet_count
            if packet_count > 0
            else 0.0
        )

        rst_ratio = (
            tcp_rst / packet_count
            if packet_count > 0
            else 0.0
        )

        rows.append(
            {
                "duration": duration,
                "src_bytes": src_bytes,
                "dst_bytes": dst_bytes,
                "src_dst_byte_ratio": src_dst_byte_ratio,
                "byte_rate": byte_rate,
                "packets_per_second": packets_per_second,
                "src_packets": src_packets,
                "dst_packets": dst_packets,
                "tcp_syn": tcp_syn,
                "tcp_ack": int(flow.get("tcp_ack", 0)),
                "tcp_fin": int(flow.get("tcp_fin", 0)),
                "tcp_rst": tcp_rst,
                "tcp_psh": int(flow.get("tcp_psh", 0)),
                "tcp_urg": int(flow.get("tcp_urg", 0)),
                "min_packet_size": int(flow.get("min_packet_size", 0)),
                "max_packet_size": int(flow.get("max_packet_size", 0)),
                "bytes_per_packet": bytes_per_packet,
                "syn_ratio": syn_ratio,
                "rst_ratio": rst_ratio,
            }
        )

    return pd.DataFrame(
        rows,
        columns=LIVE_NUMERIC_FEATURES,
    )
