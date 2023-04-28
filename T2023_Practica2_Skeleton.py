#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Crypto.Cipher import AES

MODE_CIPHER = 0
MODE_DECIPHER = 1


# --- IMPLEMENTATION GOES HERE ---------------------------------------------
#  Student helpers (functions, constants, etc.) can be defined here, if needed
def xor(x, y):
    return x ^ y


def rotate(lfsr, polynomial):
    first_element = calculate_first_element(polynomial, lfsr)
    lfsr.pop()
    lfsr.insert(0, first_element)


def calculate_first_element(polynomial, lfsr):
    result = 0

    for i in range(len(polynomial)):
        if polynomial[i] == 1:
            result = xor(lfsr[i], result)

    return result

# --------------------------------------------------------------------------


def uoc_lfsr_sequence(polynomial, initial_state, output_bits):
    """
    Returns the output sequence of output_bits bits of an LFSR with a given initial state and connection polynomial.

    :param polynomial: list of integers, with the coefficients of the connection polynomial that define the LFSR.
    :param initial_state: list of integers with the initial state of the LFSR
    :param output_bits: integer, number of bits of the output sequence
    :return: a list of output_bits bits
    """
    result = None

    # --- IMPLEMENTATION GOES HERE ---
    result = []
    initial_state.reverse()
    polynomial.reverse()
    lfsr = initial_state.copy()
    for i in range(output_bits):
        result.append(lfsr[-1])
        rotate(lfsr, polynomial)
    # --------------------------------

    return result


def validate_clocking_bits(clocking_bit, *param_pols):
    for i in range(len(clocking_bit)):
        current_param = param_pols[i]
        polynomial = current_param[0]
        initial_state = current_param[1]
        if clocking_bit[i] >= len(initial_state) or clocking_bit[i] >= len(polynomial) or clocking_bit[i] < 0:
            raise Exception(f"Clocking bit provided '{clocking_bit[i]}' is not valid for '{initial_state}'")


def uoc_ext_a5_pseudo_random_gen(params_pol_0, params_pol_1, params_pol_2, clocking_bits, output_bits):
    """
    Implements extended A5's pseudorandom generator.
    :param params_pol_0: two-element list describing the first LFSR: the first element contains a list with the
    coefficients of the connection polynomial, the second element contains a list with the initial state of the LFSR.
    :param params_pol_1: two-element list describing the second LFSR: the first element contains a list with the
    coefficients of the connection polynomial, the second element contains a list with the initial state of the LFSR.
    :param params_pol_2: two-element list describing the third LFSR: the first element contains a list with the
    coefficients of the connection polynomial, the second element contains a list with the initial state of the LFSR.
    :param clocking_bits: three-element list, with the clocking bits of each LFSR
    :param output_bits: integer, number of bits of the output sequence
    :return: list of output_bits elements with the pseudo random sequence
    """

    sequence = []

    # --- IMPLEMENTATION GOES HERE ---
    validate_clocking_bits(clocking_bits, params_pol_0, params_pol_1, params_pol_2)
    lfsr_1 = uoc_lfsr_sequence(params_pol_0[0], params_pol_0[1], len(params_pol_0[1]))
    lfsr_2 = uoc_lfsr_sequence(params_pol_1[0], params_pol_1[1], len(params_pol_1[1]))
    lfsr_3 = uoc_lfsr_sequence(params_pol_2[0], params_pol_2[1], len(params_pol_2[1]))

    lfsr_1.reverse()
    lfsr_2.reverse()
    lfsr_3.reverse()
    for i in range(output_bits):
        output = xor(xor(lfsr_1[-1], lfsr_2[-1]), lfsr_3[-1])
        sequence.append(output)
        clock_bit_val1 = lfsr_1[clocking_bits[0]]
        clock_bit_val2 = lfsr_2[clocking_bits[1]]
        clock_bit_val3 = lfsr_3[clocking_bits[2]]

        if clock_bit_val1 == clock_bit_val2 == clock_bit_val3:
            rotate(lfsr_1, params_pol_0[0])
            rotate(lfsr_2, params_pol_1[0])
            rotate(lfsr_3, params_pol_2[0])
        if clock_bit_val1 == clock_bit_val2 != clock_bit_val3:
            rotate(lfsr_1, params_pol_0[0])
            rotate(lfsr_2, params_pol_1[0])
        if clock_bit_val1 != clock_bit_val2 == clock_bit_val3:
            rotate(lfsr_2, params_pol_1[0])
            rotate(lfsr_3, params_pol_2[0])
        if clock_bit_val1 == clock_bit_val3 != clock_bit_val2:
            rotate(lfsr_1, params_pol_0[0])
            rotate(lfsr_3, params_pol_2[0])

    print(sequence)
    # --------------------------------

    return sequence


def uoc_a5_cipher(initial_state_0, initial_state_1, initial_state_2, message, mode):
    """
    Implements ciphering/deciphering with the A5 pseudo random generator.

    :param initial_state_0: list, initial state of the first LFSR
    :param initial_state_1: list, initial state of the second LFSR
    :param initial_state_2: list, initial state of the third LFSR
    :param message: string, plaintext to cipher (mode=MODE_CIPHER) or ciphertext to decipher (mode=MODE_DECIPHER)
    :param mode: MODE_CIPHER or MODE_DECIPHER, whether to cipher or decipher
    :return: string, ciphertext (mode=MODE_CIPHER) or plaintext (mode=MODE_DECIPHER)
    """

    output = ""

    # --- IMPLEMENTATION GOES HERE ---

    # --------------------------------

    return output


def uoc_aes(message, key):
    """
    Implements 1 block AES enciphering using a 256-bit key.

    :param message: string of 1 and 0s with the binary representation of the messsage, 128 char. long
    :param key: string of 1 and 0s with the binary representation of the key, 256 char. long
    :return: string of 1 and 0s with the binary representation of the ciphered message, 128 char. long
    """

    cipher_text = ""

    # --- IMPLEMENTATION GOES HERE ---

    # --------------------------------

    return cipher_text


def uoc_g(message):
    """
    Implements the g function.

    :param message: string of 1 and 0s with the binary representation of the messsage, 128 char. long
    :return: string of 1 and 0s, 256 char. long
    """

    output = ""

    # --- IMPLEMENTATION GOES HERE ---

    # --------------------------------

    return output


def uoc_naive_padding(message, block_len):
    """
    Implements a naive padding scheme. As many 0 are appended at the end of the message
    until the desired block length is reached.

    :param message: string with the message
    :param block_len: integer, block length
    :return: string of 1 and 0s with the padded message
    """

    output = ""

    # --- IMPLEMENTATION GOES HERE ---

    # --------------------------------

    return output


def uoc_mmo_hash(message):
    """
    Implements the hash function.

    :param message: a char. string with the message
    :return: string of 1 and 0s with the hash of the message
    """

    h_i = ""

    # --- IMPLEMENTATION GOES HERE ---

    # --------------------------------

    return h_i


def uoc_collision(prefix):
    """
    Generates collisions for uoc_mmo_hash, with messages having a given prefix.

    :param prefix: string, prefix for the messages
    :return: 2-element tuple, with the two strings that start with prefix and have the same hash.
    """

    collision = ("", "")

    # --- IMPLEMENTATION GOES HERE ---

    # --------------------------------

    return collision
