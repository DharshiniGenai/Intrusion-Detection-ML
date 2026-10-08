from scapy.all import sniff


def capture_packets(count=50, timeout=20):
    """
    Capture live network packets from the default network interface.

    Parameters:
        count: Maximum number of packets to capture.
        timeout: Maximum capture time in seconds.

    Returns:
        A list of captured Scapy packets.
    """
    print("Capturing packets on the default network interface...")

    packets = sniff(
        count=count,
        timeout=timeout
    )

    print(f"Packets captured: {len(packets)}")

    return packets


if __name__ == "__main__":
    packets = capture_packets()

    for packet in packets:
        print(packet.summary())