VERSION_SUM = 0
PACKET_COUNT = 0


def hex_to_binary(hex_number: str, num_digits: int = 8) -> str:
    """
    Converts a hexadecimal value into a string representation
    of the corresponding binary value
    Args:
        hex_number: str hexadecimal value
        num_digits: integer value for length of binary value.
                    defaults to 8
    Returns:
        string representation of a binary number 0-padded
        to a minimum length of <num_digits>
    """
    return str(bin(int(hex_number, 16)))[2:].zfill(num_digits)


def build_packets_from_sequence(sequence, add_to_global=True):
    # build Packets until the sequence ends
    packets = []
    while len(sequence) > 0:
        type_id = int(sequence[3:6], 2)
        if type_id == 4:
            count = 0
            while True:
                val = sequence[6 + 5 * count]
                if val == "0":
                    break
                else:
                    count += 1
            packets.append(Packet(sequence[: 6 + (count + 1) * 5], add_to_global))
            sequence = sequence[6 + (count + 1) * 5 :]
        else:
            length_type_id = sequence[6]
            if length_type_id == "0":
                length_of_subseq_packet = sequence[7:22]
                length_of_subseq_packet = int(length_of_subseq_packet, 2)
                new_packet = Packet(sequence[0 : 22 + length_of_subseq_packet], add_to_global)
                packets.append(new_packet)
                sequence = sequence[22 + length_of_subseq_packet :]
            elif length_type_id == "1":
                number_of_subseq_packet = sequence[7:18]
                number_of_subseq_packet = int(number_of_subseq_packet, 2)
                new_packets, consumed = build_n_number_of_packets(
                    sequence[18:], number_of_subseq_packet, False
                )
                del new_packets
                # packets.extend(new_packets)
                new_packet = Packet(sequence[: 18 + consumed], add_to_global)
                packets.append(new_packet)
                sequence = sequence[18 + consumed :]
    return packets


def build_n_number_of_packets(sequence, n, add_to_global):
    # Build 'n' number of packets from the sequence
    packets = []
    sequence_pointer = 0
    while len(packets) < n and sequence:
        type_id = int(sequence[3:6], 2)
        if type_id == 4:
            count = 0
            while True:
                val = sequence[6 + 5 * count]
                if val == "0":
                    break
                else:
                    count += 1
            packets.append(Packet(sequence[: 6 + (count + 1) * 5], add_to_global))
            sequence_pointer += 6 + (count + 1) * 5
            sequence = sequence[6 + (count + 1) * 5 :]
        else:
            length_type_id = sequence[6]
            if length_type_id == "0":
                length_of_subseq_packet = sequence[7:22]
                length_of_subseq_packet = int(length_of_subseq_packet, 2)
                new_packet = Packet(sequence[: 22 + length_of_subseq_packet], add_to_global)
                packets.append(new_packet)
                sequence = sequence[22 + length_of_subseq_packet :]
                sequence_pointer += 22 + length_of_subseq_packet
            elif length_type_id == "1":
                number_of_subseq_packet = sequence[7:18]
                number_of_subseq_packet = int(number_of_subseq_packet, 2)
                new_packets, consumed = build_n_number_of_packets(
                    sequence[18:], number_of_subseq_packet, False
                )
                del new_packets
                new_packet = Packet(sequence[: 18 + consumed], add_to_global)
                packets.append(new_packet)
                sequence = sequence[18 + consumed :]
                sequence_pointer += consumed + 18
    return packets, sequence_pointer


class Packet(object):
    def __init__(self, binary_data, add_to_global=True):
        self.binary_data = binary_data
        self.version = int(binary_data[0:3], 2)

        if add_to_global:
            global VERSION_SUM, PACKET_COUNT
            VERSION_SUM += self.version
            PACKET_COUNT += 1

        self.type_id = int(binary_data[3:6], 2)
        print(f"Packet; Iniitialized; type:{self.type_id}; version:{self.version}")
        if self.type_id == 4:
            val = ""
            stop = False
            count = 0
            while not stop:
                start_index = 6 + count * 5
                chunk = binary_data[start_index : start_index + 5]
                val += chunk[1:]
                if chunk[0] == "0":
                    break
                else:
                    count += 1
            self.literal_vals = val
            # print(f"literal value: {val} == {int(val, 2)}, version: {self.version}")
        else:
            length_type_id = binary_data[6]
            if length_type_id == "0":
                length_of_subseq_packet = binary_data[7:22]
                length_of_subseq_packet = int(length_of_subseq_packet, 2)
                self.child_packets = build_packets_from_sequence(
                    binary_data[22 : 22 + length_of_subseq_packet], add_to_global
                )
            elif length_type_id == "1":
                number_of_subseq_packet = binary_data[7:18]
                number_of_subseq_packet = int(number_of_subseq_packet, 2)
                # print(f"here: {binary_data[18:]}, {number_of_subseq_packet}")
                self.child_packets, _ = build_n_number_of_packets(
                    binary_data[18:], number_of_subseq_packet, add_to_global
                )


if __name__ == "__main__":
    with open("input", "r") as fh:
        line = fh.readline()

    # line = "D2FE28"

    # line = "38006F45291200"  # 27 sequence, 2 subpackets
    # line = "EE00D40C823060" # 3 literal value subpackets

    # line = "8A004A801A8002F478"  # 16
    # line = "620080001611562C8802118E34"   # 12
    # line = "C0015000016115A2E0802F182340"  # 23
    # line = "A0016C880162017C3686B18A3D4780" # 31
    bin_val = hex_to_binary(line)
    if len(bin_val) % 4:
        bin_val = "0" * (4 - len(bin_val) % 4) + bin_val
    packet = Packet(bin_val)
    
    # print(packet.literal_vals)
    # print(f"Packets: {PACKET_COUNT}, VERSION_SUM: {VERSION_SUM}")

