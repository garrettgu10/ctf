import os

flag_padding = """001011101000110100101101110011001110101111101110100011010000110010101101101011100110110010101101100011101100110010101110011011111011010001010110100101110101010010101110101001000101011111101010101100101001010111110100100010101000101111010010101010010111000111000010101011110000101101000101001001110000101010010001010001010111010101010010101011010010001110100100101101110100010111010101001110010010110100101010010001011010110100111010010100010101011000011101010100011101001000110101001011101010001101110010111001010110101001111000101010001101001101101001011100101010011100101010011011001100011011111101001010001110110100101000101010001111011011010110001100101010010110101111010010101001001011010101000100110110001011010001011110100101000110111010101011100101001110001010011010100100101111010100101110010101001110100100011100011010100111010101111010010010011101010101000100101010100101110101110001011101010101000111001001110101011010010010011011010001110101001001101011100101101001101101010110100110001010010001101110101101010100101011011101010100101110101001001000110101101001011010101000110110101010111010110111001010101101010100111100100101101101010010100011011101000110110001101101101111000101010010101010101011010111001010101101010101000111010101001101001101001110010010101001011101001000111010110100100111010010100101001101001010101101101010001101110101010101010101110101001001011010010101000100111010100101010011010100111110101010010101110100011011001010101110010100011011010010101101110101011110101010100111100101000001101010110101110100011101001011101010001010101110100110101001110101000110110101101011010101011010111010100010101010011101010101101010011101010010101101001110001100011101001000011011011100101001111010100011100101111001001010110101000111100010001101010000110110110100100100101111001011010010101011101101110010100011001011101001000111100111001011110001100010101101100100101001101101100101001011101100010101100101010001111010001101010101101010111101010101010100101010101010110100101010111010100100011010111010101111011100011101101110101000110101011001110011011101000101010110101010011010101001110101010110001101100010010011101010111111001001001101110100101001010100101001010011110100100100010100100100100010010100100101001001001001001010111011001101111010101010010101010101010101010101010110111001010101010101010110100101101010010101010101010101010101010010101001100101010010110101010100101010010010100100010101010010101010100111111101010110100101010101010101010100110010111111111111111111111110110100100101001010101010101010101010110101011010100010101010101010100101010100101010101010010111100101010101010111011010100111101010010101010101010010101010101010101110010101010101010101010010100110100101101001010101001010111010100101011001011010010101010000110010100100101010101000100110011010101010101010010101010110101010101011010101010101001010101010101000101010101010101010101001010101010101001010010101010100101010101010111001010101010100100101010111010101010100101010100101010100101010010101010010101010101010100101010100101010100100101010001010010010101010010100010100101010101000101001000000010000100000100010000000101010101001010100100101011011010010100101010100101010101010100101001001001001001000101010010100101010010101010101011010100101010100101010101010010101001010101010010101010100101010101010010101010101010101010100101010110101010010101100101010101000100101001001010101010101010010101010011001010101010101011010101010101001001001001010010010010010010010010010101010001010101010010010101010101001010101010010010101010100101010101010010101011110010101010001000101010001011100100100010011001000100010101011010101001010101010010101010100101010101001001010101001010101111001111001011001011011010010010111101010101010010010101010001010010101011101000100101001010010101011001011001010101001101010110010101010100101010010101001100101010101010101010110100100101001010010100101010100100101101010111011001010101010111011011101101001010111010010010010101001010100100100100101111011100111011010111000010100101101100100101010010100010100100100100010010010010100101010100101010011010101010101010101010101010101010110111010101101000011001"""

def flag_binary():
    flag = 'utflag{y0u_4r3_n0t_a_r4nd0m_numb3r_g3n3r4t0r}'
    binary = ''.join(format(ord(i),'b').zfill(8) for i in flag)
    return binary

def generate_flag_key(length):
    flag = flag_binary()
    remainder = length - len(flag)
    return flag + flag_padding[:remainder]

def random_1():
    return ord(os.urandom(1)) % 2

def generate_key2(message, key):
    key2 = ""
    for i in range(length):
        messageChar = message[i]
        keyChar = key[i]
        if messageChar == '0' and keyChar == '0':
            key2 += '0'
        elif messageChar == '0' and keyChar == '1':
            key2 += '1'
        elif messageChar == '1' and keyChar == '0':
            key2 += '1'
        elif messageChar == '1' and keyChar == '1':
            key2 += '0'
        else:
            print(messageChar + ' ' + keyChar)

    return key2


def generate_random_bitstring(length):
    string = ""
    for i in range(length):
        if random_1() == 1:
            string += '0'
        else:
            string += '1'
    return string

if __name__ == "__main__":
    length = 4384
    flag_key = generate_flag_key(length)
    key1 = open("key.txt", 'r').read()[:length]
    key2 = generate_key2(flag_key, key1)
    assert(len(flag_key) == len(key1))
    assert(len(key1) == len(key2))
    
    key1_index = 18213
    key2_index = 43819

    output = open('file.txt', 'w')
    for i in range(0, 50000):
        if i + 1 == key1_index:
            output.write(key1 + "\n")
        elif i + 1 == key2_index:
            output.write(key2 + "\n")
        else:
            output.write(generate_random_bitstring(length) + "\n")

output.close()