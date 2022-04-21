from typing import List
from functools import reduce


class Packet:
    """
    Class to represent a packet.
    ...

    Attributes
    ----------
    version: int
        Packet version.
    type_ID: int
        Packet type ID.
    sub_packets: List[Packet]
        List of sub-packets.
    value: int
        Packet value.
    length: int
        Number of bits of the packet.

    Methods
    -------
    get_sum_version_numbers() -> int:
        Calculate the sum of version numbers of the packet and its sub-packets.
    calculate() -> int:
        Calculate the value of the current packet.

    """
    def __init__(self, binary_string: str):
        """
        Create a Packet object from its binary string representation.
        @param binary_string: Representation of the packet in a form of a binary string.
        """
        self.version = int(binary_string[0:3], 2)
        self.type_ID = int(binary_string[3:6], 2)
        self.sub_packets = []
        self.value = None
        self.length = None

        # Packet representing a literal value
        if self.type_ID == 4:
            self.value = self.__compute_value(binary_string)

        # Packet representing an operator
        else:
            if binary_string[6] == '0':
                length_sub_packets = int(binary_string[7:22], 2)
                self.__compute_sub_packets(binary_string[22:22 + length_sub_packets])
                self.length = 22 + length_sub_packets
            else:
                nb_sub_packets = int(binary_string[7:18], 2)
                self.__compute_sub_packets(binary_string[18:], nb_sub_packets)

    def __repr__(self) -> str:
        """
        Representation of a packet.
        @return: Information of the packet.
        """
        return 'Packet version: ' + str(self.version) + '\n' \
               + 'Type ID: ' + str(self.type_ID) + '\n' \
               + 'Nb sub-packets: ' + str(len(self.sub_packets)) + '\n' \
               + 'Value: ' + str(self.value) + '\n' \
               + 'Length: ' + str(self.length) + '\n'

    def __compute_value(self, binary_string: str) -> int:
        """
        Compute the value of a packet representing a literal value.
        @param binary_string: Representation of the packet in a form of a binary string.
        @return: Value of the packet.
        """
        value = ''
        i = 6
        while i < len(binary_string):
            if binary_string[i] == '0':
                value += binary_string[i + 1:i + 5]
                break
            value += binary_string[i + 1:i + 5]
            i += 5
        self.length = i + 5
        return int(value, 2)

    def __compute_sub_packets(self, sub_packets_string: str, nb_sub_packets: int = None) -> None:
        """
        Compute all the sub-packets of the current packet representing an operator.
        @param sub_packets_string: Sub-string of the packet string that only includes sub-packets' information.
        @param nb_sub_packets: Number of sub-packets. The number of packets is only known if the length type ID is 1.
        @type nb_sub_packets: int
        """
        if not nb_sub_packets:
            remaining_bits = len(sub_packets_string)
            while remaining_bits != 0:
                self.sub_packets.append(Packet(sub_packets_string))
                sub_packets_string = sub_packets_string[self.sub_packets[-1].length:]
                remaining_bits -= self.sub_packets[-1].length
        else:
            self.length = 18
            for i in range(nb_sub_packets):
                self.sub_packets.append(Packet(sub_packets_string))
                sub_packets_string = sub_packets_string[self.sub_packets[-1].length:]
                self.length += self.sub_packets[-1].length

    def get_sum_version_numbers(self) -> int:
        """
        Calculate the sum of version numbers of the packet and its sub-packets.
        @return: Sum of version numbers of the packet and its sub-packets.
        """
        return self.version + sum([sub_packet.get_sum_version_numbers() for sub_packet in self.sub_packets])

    def calculate(self) -> int:
        """
        Calculate the value of the current packet.
        @return: Value of the current packet.
        """
        # Return the value
        if self.type_ID == 4:
            return self.value
        # Return the sum of sub-packets
        elif self.type_ID == 0:
            return sum([sub_packet.calculate() for sub_packet in self.sub_packets])
        # Return the product of sub-packets
        elif self.type_ID == 1:
            return reduce(lambda x, y: x * y, [sub_packet.calculate() for sub_packet in self.sub_packets])
        # Return the minimum sub-packet value
        elif self.type_ID == 2:
            return min([sub_packet.calculate() for sub_packet in self.sub_packets])
        # Return the maximum sub-packet value
        elif self.type_ID == 3:
            return max([sub_packet.calculate() for sub_packet in self.sub_packets])
        # Return 1 if the value of the first sub-packet is greater than the value of the second packet, 0 otherwise.
        elif self.type_ID == 5:
            return 1 if self.sub_packets[0].calculate() > self.sub_packets[1].calculate() else 0
        # Return 1 if the value of the first sub-packet is less than the value of the second sub-packet, 0 otherwise.
        elif self.type_ID == 6:
            return 1 if self.sub_packets[0].calculate() < self.sub_packets[1].calculate() else 0
        # Return 1 if the value of the first sub-packet is equal to the value of the second sub-packet, 0 otherwise
        elif self.type_ID == 7:
            return 1 if self.sub_packets[0].calculate() == self.sub_packets[1].calculate() else 0
        else:
            raise AssertionError('Invalid operator.')


def parse_input(input_file: str) -> str:
    """
    Parse input.
    @param input_file: Input file to parse.
    @return:
    """
    binary_string = ''
    with open(input_file, 'r') as f:
        for c in f.readline():
            binary_string += str(bin(int(c, 16))[2:]).zfill(4)
    return binary_string


def part1(transmission: str) -> int:
    """
    Solve part 1.
    @param transmission: Binary string representing the BITS transmission.
    @return: Sum of the version numbers in all packets of the BITS transmission.
    """
    packet = Packet(transmission)
    return packet.get_sum_version_numbers()


def part2(transmission: str) -> int:
    """
    Solve part 2.
    @param transmission: Binary string representing the BITS transmission.
    @return: Result of the calculation represented by all the packets of the BITS transmission.
    """
    packet = Packet(transmission)
    return packet.calculate()


def solve() -> None:
    """
    Solve the puzzle
    """
    puzzle_input = parse_input('input.txt')
    print(part1(puzzle_input))
    print(part2(puzzle_input))


solve()
