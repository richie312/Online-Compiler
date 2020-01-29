# -*- coding: utf-8 -*-

import os
import sys

# =============================================================================
# # file descriptors
# TEST_CASE_INPUT_FD = 0
# TEST_CASE_OUTPUT_FD = 4
# PROGRAM_SOURCE_FD = 5
# PROGRAM_OUTPUT_FD = 3
# PROGRAM_INPUT_FD = 8 # interactive only
# SCORE_FD = 1
# DEBUG_FD = 6
# 
# # statuses
# ACCEPTED = 0
# WRONG_ANSWER = 1
# 
# =============================================================================
# open streams
files = os.listdir()
TEST_CASE_INPUT_FD = 0
TEST_CASE_OUTPUT_FD = 1
PROGRAM_SOURCE_FD = 2


streams = {
    # reading
    'test_case_input': os.fdopen(TEST_CASE_INPUT_FD, 'r'),
    'test_case_output': os.fdopen(TEST_CASE_OUTPUT_FD, 'r'),
    'program_source': os.fdopen(PROGRAM_SOURCE_FD, 'r'),
    #'program_output': os.fdopen(PROGRAM_OUTPUT_FD, 'r'),
    }

################################################################################


""" read the files"""


number_of_lines = 0
number_of_correct_lines = 0

for test_case_output_line in streams['test_case_output']:
    test_case_output_line = test_case_output_line.rstrip('\n')
    program_output_line = streams['test_case_output'].readline()
    number_of_lines += 1

    if program_output_line == '':
        streams['debug'].write('Outputs differ on line {}. Expected "{}" but program\'s output has ended before.\n'
            .format(number_of_lines, test_case_output_line))
        continue

    program_output_line = program_output_line.rstrip('\n')

    if test_case_output_line == program_output_line:
        number_of_correct_lines += 1
    else:
        streams['debug'].write('Outputs differ on line {}. Expected "{}" but was "{}".\n'
            .format(number_of_lines, test_case_output_line, program_output_line))

# determine result (i.e. score and status)
score = 100 if number_of_lines == 0 else int(100 * number_of_correct_lines / number_of_lines)
status = ACCEPTED if score > 0 else WRONG_ANSWER

# set score
streams['score'].write(str(score))

# close streams
for stream in streams:
    streams[stream].close()

# exit with suitable status
sys.exit(status)