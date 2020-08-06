# 1
# Read text file -> plaintext
# Encrypt the plaintext <-> defined key
# Write the ciphertext -> text file

# 2
# Read ciphertext from #1
# Decrypt ciphertext -> original plaintext

# 3
# Runtime Plotting
#    -> Of encryption/decryption
#        -> Versus the input file size

################################################################################################

import math
import numpy as np
from timeit import default_timer as timer
import matplotlib.pyplot as plt
import re

key = '4312567'

with open('PlainText.txt', 'r', encoding="utf8") as file0:
    original_plain = file0.read()


################################################################################################
################################################################################################


def encrypt(x):
    for i in range(x):
        with open('PlainText.txt', 'r', encoding="utf8") as file:

            plain_text = file.read()
            plain_text = plain_text.replace(' ', '*')

            key_list = list(key)

            plaintext_length = len(plain_text)
            key_length = cols = len(key)

            rows_raw = plaintext_length / key_length
            rows = math.ceil(rows_raw)

            left_overs = (rows * cols) - plaintext_length
            plain_text += ('#' * left_overs)

            plain_matrix = np.array(list(plain_text)).reshape(rows, cols)

            cipher_list = []

            counter = 1
            k = 0

            while True:
                if int(key_list[k]) == counter:
                    counter += 1
                    for r in range(rows):
                        cipher_list.append(plain_matrix[r][k])

                if k == int(key_length) - 1:
                    k = 0
                else:
                    k += 1

                if counter == int(key_length) + 1:
                    break

            cipher_matrix = np.array(cipher_list).reshape(rows, cols)

            cipher = ''.join(cipher_list)

            txt_file = 'Encryptions/CipherText-' + str(i + 1) + '.txt'

            with open(txt_file, 'w+', encoding="utf8") as e:
                e.write(cipher)

            with open('CipherText.txt', 'w+', encoding="utf8") as file2:
                file2.write(cipher)
            with open('PlainText.txt', 'w+', encoding="utf8") as file3:
                file3.write(cipher)

            if i == 0:
                print('\nKey = ', key)
                print('Key List = ', key_list)
                print('Key Length = ', key_length)
                print('OriginalText Length = ', len(original_plain), '\n')

            if plaintext_length < 350:
                if i == 0:
                    print('\nOriginalText = ', original_plain, '\n\n')
                print('-' * 50)
                print('Encryption #' + str(i + 1))

                print('\nPlainText = ', plain_text, '\n')
                print('PlainText Length = ', len(plain_text))
                print('PlainList = ', list(plain_text))
                print('\n PlainMatrix = \n', plain_matrix, '\n')

                print('\nCipher_List = ', cipher_list)
                print('\n CipherMatrix = \n', cipher_matrix, '\n')
                print('CipherText = ', cipher, '\n\n')


################################################################################################
################################################################################################

def decrypt(x):
    for i in range(x):
        with open('CipherText.txt', 'r', encoding="utf8") as file:
            cipher_text = file.read()
            key_list = list(key)

            # print(cipher_text)
            # print(key_list)

            cipher_length = len(cipher_text)
            key_length = cols = len(key)

            rows_raw = cipher_length / key_length
            rows = math.ceil(rows_raw)

            left_overs = (rows * cols) - cipher_length
            cipher_text += ('#' * left_overs)

            cipher_matrix = np.array(list(cipher_text)).reshape(rows, cols)

            # print(cipher_text)
            # print(cipher_matrix)

            plain_list = []
            plain_list2 = []

            cipher_counter = 0

            for r in range(rows):
                for c in range(cols):
                    plain_list.append(cipher_text[((c + 1) * rows - rows) + cipher_counter])
                cipher_counter += 1

            # print(plain_list)

            plain_matrix = np.array(plain_list).reshape(rows, cols)

            # print('\n -------')
            # print(plain_matrix)

            for r in range(rows):
                for k in key:
                    plain_list2.append(plain_list[(r * cols) + int(k) - 1])

            # print('\n -------')
            # print(plain_list2)

            plain_matrix2 = np.array(plain_list2).reshape(rows, cols)
            # print(plain_matrix2)

            '''
            Split the CipherText chars per number of Rows 
            (example here to 4: TTNA APTM TSUO AODW COI# KNL# PET# )
            
            0  4  8  12  16  20  24
            1  5  9  13  17  21  25
            2  6  10 14  18  22  26
            3  7  11 15  19  23  27
            
            0  4  8  12  16  20  24  - 1  5  9  13  17  21  25  - 2  6  10 14  18  22  26 - 3  7  11 15  19  23  27
       
            Store each consecutive 4 chars in a column in new 2D matrix
            1 2 3 4 5 6 7
            -------------
            T A T A C K P
            T P S O O N E
            N T U D I L T
            A M O W # # #
            
            TATACKP TPSOONE NTUDILT AMOW###
            ATTACKP OSTPONE DUNTILT WOAM###
            
            
            Rearrange Columns based on Key
            4 3 1 2 5 6 7
            -------------
            A T T A C K P
            O S T P O N E
            D U N T I L T
            W O A M # # #
            
            Convert 2D matrix to string
            '''

            plain = ''.join(plain_list2)

            txt_file = 'Decryptions/PlainText-' + str(i + 1) + '.txt'

            with open(txt_file, 'w+', encoding="utf8") as d:
                d.write(plain)

            with open('DecryptedText.txt', 'w+', encoding="utf8") as file5:
                file5.write(plain)
            with open('CipherText.txt', 'w+', encoding="utf8") as file6:
                file6.write(plain)

            if i == 0:
                print('\n')
                print('-' * 80, )
                print('-' * 80, '\n')
                print('\nKey = ', key)
                print('Key List = ', key_list)
                print('Key Length = ', key_length, '\n')

            if cipher_length < 350:
                print('-' * 50)
                print('Decryption #' + str(i + 1))

                print('\nCipherText = ', cipher_text, '\n')
                print('CipherText Length = ', len(cipher_text))
                print('CipherList = ', list(cipher_text))
                print('\nCipherMatrix = \n', cipher_matrix, '\n')

                print('\nPlain_List = ', plain_list)
                print('\nPlainMatrix = \n', plain_matrix, '\n')
                print('PlainText = ', plain, '\n\n')


def decrypted_to_original():
    with open('DecryptedText.txt', 'r+', encoding="utf8") as file7:
        read_it = file7.read()
        read_it = re.sub(r"[*]", " ", read_it)
        read_it = re.sub(r"#", "", read_it)
        with open('DecryptedText.txt', 'w+', encoding="utf8") as file8:
            file8.write(read_it)

        if len(original_plain) < 350:
            print('-' * 80, )
            print('\nDecrypted Text = \n', read_it, '\n')

################################################################################################
################################################################################################

# TIME PLOTTING Against 100 Runs
n = 100


def ed_time():
    start = timer()

    for _ in range(n):
        encrypt(2)
        decrypt(2)

    end = timer()
    print('Avg Time = ', (end - start) / n)


# ed_time()

def ed_plot():
    # 30 chars
    E_Time_30 = 0.007632138
    D_Time_30 = 0.007179960
    Time_30 = 0.015463284

    # 300 chars
    E_Time_300 = 0.012433908
    D_Time_300 = 0.012199800
    Time_300 = 0.024077437

    # 3000 chars
    E_Time_3K = 0.017330335
    D_Time_3K = 0.013047129
    Time_3K = 0.029399291

    # 30,000 chars
    E_Time_30K = 0.082124978
    D_Time_30K = 0.092922126
    Time_30K = 0.195039277

    # 300,000 chars
    E_Time_300K = 0.698710706
    D_Time_300K = 0.798134312
    Time_300K = 1.534922414

    E_Time = [E_Time_30, E_Time_300, E_Time_3K, E_Time_30K, E_Time_300K]
    D_Time = [D_Time_30, D_Time_300, D_Time_3K, D_Time_30K, D_Time_300K]
    Time = [Time_30, Time_300, Time_3K, Time_30K, Time_300K]

    plt.plot([30, 300, 3000, 30000, 300000], E_Time,  'r')
    plt.plot([30, 300, 3000, 30000, 300000], D_Time,  'g')
    plt.plot([30, 300, 3000, 30000, 300000], Time,  'b')

    plt.xlabel('Chars Count')
    plt.ylabel('Time In Seconds')
    plt.gca().legend(('Encryption', 'Decryption', 'Both'))
    plt.show()


ed_plot()


################################################################################################
################################################################################################

number = 2
encrypt(number)
decrypt(number)
decrypted_to_original()

################################################################################################
################################################################################################

# 30 chars
# ----------------
# Hogwarts School of Witchcraft


# 300 chars
# ----------------
# Dear Mr. Potter,
# We are pleased to inform you that you have been accepted at Hogwarts School of Witchcraft and Wizardry.
# Please find enclosed a list of all necessary books and equipment.
# The term begins on September 1. We await your owl by no later than July 31
# Yours sincerely,
# Prof. Dr. Muath Juady


# 3000 chars
# HOGWARTS SCHOOL of WITCHCRAFT and WIZARDRY
# UNIFORM
# First-year students will require:
# 1. Three sets of plain work robes (black)
# 2. One plain pointed hat (black) for day wear
# 3. One pair of protective gloves (dragon hide or similar)
# 4. One winter cloak (black, silver fastenings)
# Please note that all pupils’ clothes should carry name tags
# COURSE BOOKS
# All students should have a copy of each of the following:
# The Standard Book of Spells (Grade 1) by Miranda Goshawk
# A History of Magic by Bathilda Bagshot
# Magical Theory by Adalbert Waffling
# A Beginners’ Guide to Transfiguration by Emeric Switch
# One Thousand Magical Herbs and Fungi by Phyllida Spore
# Magical Draughts and Potions by Arsenius Jigger
# Fantastic Beasts and Where to Find Them by Newt Scamander
# The Dark Forces: A Guide to Self-Protection by Quentin Trimble
# OTHER EQUIPMENT
# 1 wand
# 1 cauldron (pewter, standard size 2)
# 1 set glass or crystal phials
# 1 telescope
# 1 set brass scales
# Students may also bring an owl OR a cat OR a toad
# PARENTS ARE REMINDED THAT FIRST YEARS ARE NOT ALLOWED THEIR OWN BROOMSTICKS
#
# “Can we buy all this in London?” Harry wondered aloud.
# “If yeh know where to go,” said Hagrid.
# Harry had never been to London before. Although Hagrid seemed to know
# where he was going, he was obviously not used to getting there in an ordinary
# way. He got stuck in the ticket barrier on the Underground, and complained
# loudly that the seats were too small and the trains too slow.
# “I don’t know how the Muggles manage without magic,” he said as they
# climbed a broken-down escalator that led up to a bustling road lined with
# shops.
# Hagrid was so huge that he parted the crowd easily; all Harry had to do
# was keep close behind him. They passed book shops and music stores,
# hamburger restaurants and cinemas, but nowhere that looked as if it could sell
# you a magic wand. This was just an ordinary street full of ordinary people.
# Could there really be piles of wizard gold buried miles beneath them? Were
# there really shops that sold spell books and broomsticks? Might this not all be
# some huge joke that the Dursleys had cooked up? If Harry hadn’t known that
# the Dursleys had no sense of humor, he might have thought so; yet somehow,
# even though everything Hagrid had told him so far was unbelievable, Harry
# couldn’t help trusting him.
# “This is it,” said Hagrid, coming to a halt, “the Leaky Cauldron. It’s a
# famous place.”
# It was a tiny, grubby-looking pub. If Hagrid hadn’t pointed it out, Harry
# wouldn’t have noticed it was there. The people hurrying by didn’t glance at
# it. Their eyes slid from the big book shop on one side to the record shop on
# the other as if they couldn’t see the Leaky Cauldron at all. In fact, Harry had
# the most peculiar feeling that only he and Hagrid could see it. Before he
# could mention this, Hagrid had steered him inside.
# For a famous place, it was very dark and shabby. A few old women were
# sitting in a corner, drinking tiny glasses of sherry. One of them was smoking
# a long pipe. A little man in an.


# 30000 chars
# In 30K.txt


# 300000 chars
# In 300K.txt


################################################################################################
################################################################################################

with open('PlainText.txt', 'w+', encoding="utf8") as file0:
    file0.write(original_plain)
