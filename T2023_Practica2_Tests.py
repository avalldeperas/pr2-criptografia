#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

#from T2023_Practica2_Solution_Skeleton import *
from T2023_Practica2_Skeleton import *


class TestGenKey(unittest.TestCase):

    def test_basic_genkey_1(self):
        result = uoc_lfsr_sequence([1, 1, 0, 0], [1, 0, 0, 0], 20)
        exp_resu1t = [1, 0, 0, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1, 1, 1, 1, 0, 0, 0, 1]
        self.assertEqual(result, exp_resu1t)

    def test_basic_genkey_2(self):
        result = uoc_lfsr_sequence([1, 0, 1, 1, 0, 0], [0, 0, 0, 1, 0, 0], 20)
        exp_resu1t = [0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0, 0, 1, 0, 1]
        self.assertEqual(result, exp_resu1t)

    def test_basic_genkey_3(self):
        result = uoc_lfsr_sequence([1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                   [0, 0, 1, 1, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0], 30)
        exp_resu1t = [0, 0, 1, 1, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        self.assertEqual(result, exp_resu1t)

    def test_basic_genkey_4(self):
        result = uoc_lfsr_sequence([1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 0, 1, 0], 30)
        exp_resu1t = [0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 1, 1, 0, 0, 0, 0, 1, 1, 0, 1, 1, 1, 0]
        self.assertEqual(result, exp_resu1t)

    def test_long_genkey_1(self):
        result = uoc_lfsr_sequence([1, 1, 0, 0, 1, 0, 1, 0], [1, 0, 0, 0, 0, 0, 0, 0], 70)
        exp_resu1t = [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 1,
                      0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0,
                      1, 1, 1, 0]
        self.assertEqual(result, exp_resu1t)

    def test_long_genkey_2(self):
        result = uoc_lfsr_sequence([1, 0, 0, 1, 1, 0, 0, 0], [1, 1, 0, 0, 1, 1, 0, 0], 70)
        exp_resu1t = [1, 1, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 0, 1, 1,
                      1, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 1, 1, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0,
                      0, 1, 1, 1]
        self.assertEqual(result, exp_resu1t)


class TestPseudoRandGen(unittest.TestCase):
    def test_pseudorandom_gen_1(self):
        p0 = [[1, 0, 1], [1, 0, 0]]
        p1 = [[1, 0, 0, 1], [1, 0, 0, 0]]
        p2 = [[1, 0, 0, 1, 0], [1, 0, 0, 0, 0]]
        clocking_bits = [2, 3, 3]
        size = 30
        exp_sequence = [1, 1, 0, 1, 0, 0, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1]
        result = uoc_ext_a5_pseudo_random_gen(p0, p1, p2, clocking_bits, size)
        self.assertEqual(result, exp_sequence)

    def test_pseudorandom_gen_2(self):
        p0 = [[1, 0, 0, 1, 1], [0, 0, 1, 0, 0]]
        p1 = [[1, 0, 0, 1, 0, 1], [1, 0, 1, 0, 0, 0]]
        p2 = [[1, 0, 1, 1, 0], [0, 0, 1, 0, 0]]
        clocking_bits = [3, 4, 2]
        size = 30
        exp_sequence = [1, 0, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 0, 1]
        result = uoc_ext_a5_pseudo_random_gen(p0, p1, p2, clocking_bits, size)
        self.assertEqual(result, exp_sequence)

    def test_pseudorandom_gen_3(self):
        p0 = [[1, 0, 1, 0, 1], [0, 0, 1, 0, 0]]
        p1 = [[1, 0, 0, 1, 1, 1], [1, 0, 1, 0, 0, 0]]
        p2 = [[1, 1, 1, 0], [0, 1, 1, 0]]
        clocking_bits = [2, 1, 2]
        size = 30
        exp_sequence = [1, 0, 0, 0, 1, 0, 1, 0, 1, 1, 0, 0, 0, 1, 0, 1, 0, 1, 1, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 1]
        result = uoc_ext_a5_pseudo_random_gen(p0, p1, p2, clocking_bits, size)
        self.assertEqual(result, exp_sequence)


class TestA5Cipher(unittest.TestCase):
    def test_cipher_1(self):
        init_st_0 = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        init_st_1 = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        init_st_2 = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        message = "PLAINTEXT"
        exp_ciphered = "110100000100110001000111010011010100110001011011100001010111110011010101"
        ciphered = uoc_a5_cipher(init_st_0, init_st_1, init_st_2, message, MODE_CIPHER)
        self.assertEqual(ciphered, exp_ciphered)

    def test_cipher_2(self):
        init_st_0 = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        init_st_1 = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        init_st_2 = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        message = "CHECKTHEOUTPUTMESSAGETOTESTIFITWASRIGHT"
        exp_ciphered = "1100001101001000010000110100011101001001010110111000100001100001110011100000111110101111011" \
                       "1010100001111000000011100100011101000111010001000111001110100101000000111101011111101001110" \
                       "0111010001000000111101011011101101011011110011100011100101111010110001011110001110101001100" \
                       "101000111101101110011010000111101100110"
        ciphered = uoc_a5_cipher(init_st_0, init_st_1, init_st_2, message, MODE_CIPHER)
        self.assertEqual(ciphered, exp_ciphered)

    def test_cipher_3(self):
        init_st_0 = [0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        init_st_1 = [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        init_st_2 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 1]
        message = "DUMMYINPUTTEXT"
        exp_ciphered = "01001001110011010101111000001111011010011001100001010000010010010011011000110101000000110111" \
                       "11011001000100110011"
        ciphered = uoc_a5_cipher(init_st_0, init_st_1, init_st_2, message, MODE_CIPHER)
        self.assertEqual(ciphered, exp_ciphered)

    def test_cipher_4(self):
        init_st_0 = [0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        init_st_1 = [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        init_st_2 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 1]
        message = "AREALLYOURTESTSWORKING"
        exp_ciphered = "01001100110010100101011000000011011111001001110101000111010101100011011000110011000000110111" \
                       "110110011010001100110000111101111110010010001111101111100010100010010001111010100100"
        ciphered = uoc_a5_cipher(init_st_0, init_st_1, init_st_2, message, MODE_CIPHER)
        self.assertEqual(ciphered, exp_ciphered)

    def test_cipher_5(self):
        init_st_0 = [0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        init_st_1 = [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        init_st_2 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 1]
        message = "THISCIPHERISQUITEGOOD"
        exp_ciphered = "01011001110100000101101000010001011100111001100001001110010100010010011000110011000111100110" \
                       "1011100110000011001000010101011111010100001011101110111001101000111100010100"
        ciphered = uoc_a5_cipher(init_st_0, init_st_1, init_st_2, message, MODE_CIPHER)
        self.assertEqual(ciphered, exp_ciphered)

    def test_cipher_6(self):
        init_st_0 = [0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        init_st_1 = [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        init_st_2 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 1]
        message = "THISLASTMESSAGEISTHELONGESTONEFIRSTTIMETHISLASTMESSAGEISTHELONGESTONESECONDTIMETHISLASTMESSAGEIS" \
                  "THELONGESTONETHIRDTTIMETHISLASTMESSAGEISTHELONGESTONELASTTIME"
        exp_ciphered = "010110011101000001011010000100010111110010010000010011010100110100101110001001000000010001101" \
                       "011100010000010000000011001011000000101010011111101111000011000010100011100101011001000100100" \
                       "010011010101011100001010100011000101110010001010011000111111100100111101101010101010100110100" \
                       "001111011110011011011100101100001011111000011001001110010010010110000110101111100001110001100" \
                       "110000110111101100111101110011000101000100110010000001101001110101101100001011010101010110101" \
                       "111011101011011101101001110110001001010000101000100100010001011000111011111001100111110011000" \
                       "000000101101101010011111110001001101010010001100111110000100101111101111101010000000100101111" \
                       "110011000001001011000010110011011110000110001111010110100001010110000010001001110010111111100" \
                       "000100001101011000110110000101101000000110101001110000100100100111010001001011111011011010010" \
                       "010000111011001000000010010010111101100110110101110101001111110101010100100100000111000100000" \
                       "000111011111110010110001110011010000110011111011101001111100011001010000111100011110001101100" \
                       "001111010100000011100101000011110001011111110100010101111111100011110111010100101001010010001" \
                       "101001011110111011010100100101000000001000101101001111100111011000010011000010010010100100101" \
                       "10001000100101111100010100101111100110110101100"
        ciphered = uoc_a5_cipher(init_st_0, init_st_1, init_st_2, message, MODE_CIPHER)
        self.assertEqual(ciphered, exp_ciphered)


class TestA5Decipher(unittest.TestCase):
    def test_decipher_1(self):
        init_st_0 = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        init_st_1 = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        init_st_2 = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        exp_message = "PLAINTEXT"
        ciphered = "110100000100110001000111010011010100110001011011100001010111110011010101"
        message = uoc_a5_cipher(init_st_0, init_st_1, init_st_2, ciphered, MODE_DECIPHER)
        self.assertEqual(message, exp_message)

    def test_decipher_2(self):
        init_st_0 = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        init_st_1 = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        init_st_2 = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        exp_message = "CHECKTHEOUTPUTMESSAGETOTESTIFITWASRIGHT"
        ciphered = "1100001101001000010000110100011101001001010110111000100001100001110011100000111110101111011" \
                   "1010100001111000000011100100011101000111010001000111001110100101000000111101011111101001110" \
                   "0111010001000000111101011011101101011011110011100011100101111010110001011110001110101001100" \
                   "101000111101101110011010000111101100110"
        message = uoc_a5_cipher(init_st_0, init_st_1, init_st_2, ciphered, MODE_DECIPHER)
        self.assertEqual(message, exp_message)

    def test_decipher_3(self):
        init_st_0 = [0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        init_st_1 = [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        init_st_2 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 1]
        exp_message = "DUMMYINPUTTEXT"
        ciphered = "01001001110011010101111000001111011010011001100001010000010010010011011000110101000000110111" \
                   "11011001000100110011"
        message = uoc_a5_cipher(init_st_0, init_st_1, init_st_2, ciphered, MODE_DECIPHER)
        self.assertEqual(message, exp_message)

    def test_decipher_4(self):
        init_st_0 = [0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        init_st_1 = [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        init_st_2 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 1]
        exp_message = "AREALLYOURTESTSWORKING"
        ciphered = "01001100110010100101011000000011011111001001110101000111010101100011011000110011000000110111" \
                   "110110011010001100110000111101111110010010001111101111100010100010010001111010100100"
        message = uoc_a5_cipher(init_st_0, init_st_1, init_st_2, ciphered, MODE_DECIPHER)
        self.assertEqual(message, exp_message)

    def test_decipher_5(self):
        init_st_0 = [0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        init_st_1 = [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        init_st_2 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 1]
        exp_message = "THISCIPHERISQUITEGOOD"
        ciphered = "01011001110100000101101000010001011100111001100001001110010100010010011000110011000111100110" \
                   "1011100110000011001000010101011111010100001011101110111001101000111100010100"
        message = uoc_a5_cipher(init_st_0, init_st_1, init_st_2, ciphered, MODE_DECIPHER)
        self.assertEqual(message, exp_message)

    def test_decipher_6(self):
        init_st_0 = [0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        init_st_1 = [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        init_st_2 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 1]
        exp_message = "THISLASTMESSAGEISTHELONGESTONEFIRSTTIMETHISLASTMESSAGEISTHELONGESTONESECONDTIMETHISLASTMESSAGE" \
                      "ISTHELONGESTONETHIRDTTIMETHISLASTMESSAGEISTHELONGESTONELASTTIME"
        ciphered = "0101100111010000010110100001000101111100100100000100110101001101001011100010010000000100011010111" \
                   "0001000001000000001100101100000010101001111110111100001100001010001110010101100100010010001001101" \
                   "0101011100001010100011000101110010001010011000111111100100111101101010101010100110100001111011110" \
                   "0110110111001011000010111110000110010011100100100101100001101011111000011100011001100001101111011" \
                   "0011110111001100010100010011001000000110100111010110110000101101010101011010111101110101101110110" \
                   "1001110110001001010000101000100100010001011000111011111001100111110011000000000101101101010011111" \
                   "1100010011010100100011001111100001001011111011111010100000001001011111100110000010010110000101100" \
                   "1101111000011000111101011010000101011000001000100111001011111110000010000110101100011011000010110" \
                   "1000000110101001110000100100100111010001001011111011011010010010000111011001000000010010010111101" \
                   "1001101101011101010011111101010101001001000001110001000000001110111111100101100011100110100001100" \
                   "1111101110100111110001100101000011110001111000110110000111101010000001110010100001111000101111111" \
                   "0100010101111111100011110111010100101001010010001101001011110111011010100100101000000001000101101" \
                   "00111110011101100001001100001001001010010010110001000100101111100010100101111100110110101100"
        message = uoc_a5_cipher(init_st_0, init_st_1, init_st_2, ciphered, MODE_DECIPHER)
        self.assertEqual(message, exp_message)


class TestAES(unittest.TestCase):

    def test_aes_1(self):
        plain = "011010111100000110111110111000100010111001000000100111111001011011101001001111010111111000010001011" \
                "10011100100110001011100101010"
        key = "01100000001111011110101100010000000101011100101001110001101111100010101101110011101011101111000010000" \
              "10101111101011101111000000100011111001101010010110000000111001110110110000100001000110101110010110110" \
              "011000000100001010001100001001000101001101111111110100"
        exp_cipher = "1111001111101110110100011011110110110101110100101010000000111100000001100100101101011010011111" \
                     "1000111101101100011000000111111000"
        assert(len(plain) == 128)  # 16 bytes
        assert(len(key) == 256)  # 32 bytes
        assert(len(exp_cipher) == 128)  # 16 bytes
        cipher = uoc_aes(plain, key)
        assert(cipher == exp_cipher)

    def test_aes_2(self):
        plain = "101011100010110110001010010101110001111000000011101011001001110010011110101101110110111110101100010" \
                "00101101011111000111001010001"
        key = "01100000001111011110101100010000000101011100101001110001101111100010101101110011101011101111000010000" \
              "10101111101011101111000000100011111001101010010110000000111001110110110000100001000110101110010110110" \
              "011000000100001010001100001001000101001101111111110100"
        exp_cipher = "0101100100011100110010110001000011010100000100001110110100100110110111000101101110100111010010" \
                     "1000110001001101100010100001110000"
        assert(len(plain) == 128)  # 16 bytes
        assert(len(key) == 256)  # 32 bytes
        assert(len(exp_cipher) == 128)  # 16 bytes
        cipher = uoc_aes(plain, key)
        assert(cipher == exp_cipher)

    def test_aes_3(self):
        plain = "001100001100100000011100010001101010001101011100111001000001000111100101111110111100000100011001000" \
                "11010000010100101001011101111"
        key = "01100000001111011110101100010000000101011100101001110001101111100010101101110011101011101111000010000" \
              "10101111101011101111000000100011111001101010010110000000111001110110110000100001000110101110010110110" \
              "011000000100001010001100001001000101001101111111110100"
        exp_cipher = "1011011011101101001000011011100110011100101001101111010011111001111100010101001111100111101100" \
                     "0110111110101011111110110100011101"
        assert(len(plain) == 128)  # 16 bytes
        assert(len(key) == 256)  # 32 bytes
        assert(len(exp_cipher) == 128)  # 16 bytes
        cipher = uoc_aes(plain, key)
        assert(cipher == exp_cipher)


class TestG(unittest.TestCase):

    def test_g_1(self):
        i = "1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111" \
            "1111111111111111111111111"
        o = uoc_g(i)
        exp_o = "111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111" \
                "111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111" \
                "1111111111111111111111111111111111111111111111111111111111"
        assert(len(i) == 128)
        assert(len(o) == 128*2)
        assert(o == exp_o)

    def test_g_2(self):
        i = "1010010100101111100011101100101111001100110000000110100001010001011001001100100001001001101101000010000" \
            "1111011001101000011010100"
        o = uoc_g(i)
        exp_o = "101001010010111110001110110010111100110011000000011010000101000101100100110010000100100110110100001" \
                "000011110110011010000110101001010010100101111100011101100101111001100110000000110100001010001011001" \
                "0011001000010010011011010000100001111011001101000011010100"
        assert(len(i) == 128)
        assert(len(o) == 128*2)
        assert(o == exp_o)

    def test_g_3(self):
        i = "1010011011010110100100000011001110000101100110101000110110100100111000000110111110101111000001100001111" \
            "1101100101101110101111010"
        o = uoc_g(i)
        exp_o = "101001101101011010010000001100111000010110011010100011011010010011100000011011111010111100000110000" \
                "111111011001011011101011110101010011011010110100100000011001110000101100110101000110110100100111000" \
                "0001101111101011110000011000011111101100101101110101111010"
        assert(len(i) == 128)
        assert(len(o) == 128*2)
        assert(o == exp_o)


class TestNaivePadding(unittest.TestCase):

    def test_naive_padding_1(self):
        # no padding
        block_len = 128
        message = "CRYPTOGRAPHY0123"
        o = uoc_naive_padding(message, block_len)
        exp_o = "010000110101001001011001010100000101010001001111010001110101001001000001010100000100100001011001001" \
                "10000001100010011001000110011"
        assert(len(exp_o) % block_len == 0)
        assert(o == exp_o)

    def test_naive_padding_2(self):
        # no padding
        block_len = 256
        message = "CRYPTOGRAPHY0123CRYPTOGRAPHY3210"
        o = uoc_naive_padding(message, block_len)
        exp_o = "010000110101001001011001010100000101010001001111010001110101001001000001010100000100100001011001001" \
                "100000011000100110010001100110100001101010010010110010101000001010100010011110100011101010010010000" \
                "0101010000010010000101100100110011001100100011000100110000"
        assert(len(exp_o) % block_len == 0)
        assert(o == exp_o)

    def test_naive_padding_3(self):
        # no padding
        block_len = 32
        message = "WORL"
        o = uoc_naive_padding(message, block_len)
        exp_o = "01010111010011110101001001001100"
        assert(len(exp_o) % block_len == 0)
        assert(o == exp_o)

    def test_naive_padding_4(self):
        block_len = 128
        message = "CRYPTOGRAPHY"
        o = uoc_naive_padding(message, block_len)
        exp_o = "010000110101001001011001010100000101010001001111010001110101001001000001010100000100100001011001000" \
                "00000000000000000000000000000"
        assert(len(exp_o) % block_len == 0)
        assert(o == exp_o)

    def test_naive_padding_5(self):
        block_len = 256
        message = "CRYPTOGRAPHY"
        o = uoc_naive_padding(message, block_len)
        exp_o = "010000110101001001011001010100000101010001001111010001110101001001000001010100000100100001011001000" \
                "000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000" \
                "0000000000000000000000000000000000000000000000000000000000"
        assert(len(exp_o) % block_len == 0)
        assert(o == exp_o)

    def test_naive_padding_6(self):
        block_len = 32
        message = "WOR"
        o = uoc_naive_padding(message, block_len)
        exp_o = "01010111010011110101001000000000"
        assert(len(exp_o) % block_len == 0)
        assert(o == exp_o)

    def test_naive_padding_7(self):
        block_len = 128
        message = "CRYPTOGRA"
        o = uoc_naive_padding(message, block_len)
        exp_o = "010000110101001001011001010100000101010001001111010001110101001001000001000000000000000000000000000" \
                "00000000000000000000000000000"
        assert(len(exp_o) % block_len == 0)
        assert(o == exp_o)

    def test_naive_padding_8(self):
        block_len = 128
        message = "CRYPTOGRAPHY012"
        o = uoc_naive_padding(message, block_len)
        exp_o = "010000110101001001011001010100000101010001001111010001110101001001000001010100000100100001011001001" \
                "10000001100010011001000000000"
        assert(len(exp_o) % block_len == 0)
        assert(o == exp_o)


class TestMMOHash(unittest.TestCase):

    def test_mmo_1(self):
        # no padding, 1 block
        block_size = 128
        message = "CRYPTOGRAPHY0123"
        exp_hash = "111000010010011011001100101111101000101100010101011100011000110101110000100010010100101011101010" \
                   "11100001010000000101110100100101"
        h = uoc_mmo_hash(message)
        assert(h == exp_hash)
        assert(len(h) == block_size)

    def test_mmo_2(self):
        # with padding, 1 block
        block_size = 128
        message = "CRYPTOGRAPHY"
        exp_hash = "000110001011100011100101110111001110000110110111111000111100110101111000000100011000011111101001" \
                   "11101111011000111000000100011111"
        h = uoc_mmo_hash(message)
        assert(h == exp_hash)
        assert(len(h) == block_size)

    def test_mmo_3(self):
        # no padding, 2 blocks
        block_size = 128
        message = "HELLOWORLDCRIPTOGRAPHYISABOUTHAS"
        exp_hash = "011001100010000110111000111010001111011001011010110000101100010010010101101110101110111111001101" \
                   "11000001001000011010101111001001"
        h = uoc_mmo_hash(message)
        assert(h == exp_hash)
        assert(len(h) == block_size)

    def test_mmo_4(self):
        # with padding, multiple blocks
        block_size = 128
        message = "HELLOWORLDCRIPTOGRAPHYISABOUTHASHFUNCTIONS"
        exp_hash = "110010010111100111101111010001111111001001000001000010010011110001011000010001000101111011110100" \
                   "11001101011001010011000000110100"
        h = uoc_mmo_hash(message)
        assert(h == exp_hash)
        assert(len(h) == block_size)

    def test_mmo_5(self):
        # with padding, multiple blocks
        block_size = 128
        message = "THISISAVERYLONGLONGMESSAGETOTESTTHEIMPLEMENTATIONOFOURHASHFUNCTION"
        exp_hash = "000001101110101100111001011111010111101111110010100001011001001010111000100101010110100010010001" \
                   "01100100110100111111101110010110"
        h = uoc_mmo_hash(message)
        assert(h == exp_hash)
        assert(len(h) == block_size)


class TestCollision(unittest.TestCase):

    def test_collision_1(self):
        prefix = "CRYPTO"
        (m1, m2) = uoc_collision(prefix)
        assert(uoc_mmo_hash(m1) == uoc_mmo_hash(m2))
        assert(m1 != m2)

    def test_collision_2(self):
        prefix = "ACOLLISION"
        (m1, m2) = uoc_collision(prefix)
        assert(uoc_mmo_hash(m1) == uoc_mmo_hash(m2))
        assert(m1 != m2)

    def test_collision_3(self):
        prefix = "ACOLLISIONISNICE"
        (m1, m2) = uoc_collision(prefix)
        assert(uoc_mmo_hash(m1) == uoc_mmo_hash(m2))
        assert(m1 != m2)

    def test_collision_4(self):
        prefix = "TWOMESSAGESWITHTHESAMEHASHTHISIA"
        (m1, m2) = uoc_collision(prefix)
        assert(uoc_mmo_hash(m1) == uoc_mmo_hash(m2))
        assert(m1 != m2)


if __name__ == '__main__':

    # create a suite with all tests
    test_classes_to_run = [TestGenKey, TestPseudoRandGen, TestA5Cipher, TestA5Decipher,
                           TestAES, TestG, TestNaivePadding, TestMMOHash, TestCollision]
    loader = unittest.TestLoader()
    suites_list = []
    for test_class in test_classes_to_run:
        suite = loader.loadTestsFromTestCase(test_class)
        suites_list.append(suite)

    all_tests_suite = unittest.TestSuite(suites_list)

    # run the test suite with high verbosity
    runner = unittest.TextTestRunner(verbosity=2)
    results = runner.run(all_tests_suite)
