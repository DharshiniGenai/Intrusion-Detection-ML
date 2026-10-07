from scapy.all import sniff, IFACES


# Your active Wi-Fi interface identified during testing
INTERFACE_INDEX = 17


def capture_packets(count=50, timeout=20):
    """
    Capture live network packets from the configured interface.

    Parameters:
        count: Maximum number of packets to capture.
        timeout: Maximum capture time in seconds.

    Returns:
        A list of captured Scapy packets.
    """
    interface = IFACES.dev_from_index(INTERFACE_INDEX)

    print(f"Capturing packets on: {interface}")

    packets = sniff(
        iface=interface,
        count=count,
        timeout=timeout
    )

    print(f"Packets captured: {len(packets)}")

    return packets


if __name__ == "__main__":
    packets = capture_packets()

    for packet in packets:
        print(packet.summary())