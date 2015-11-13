######################################
## PyCrunch							##
## By Nathan ASH 					##
## http://nathanash.id.au 			##
## https://github.com/ompster		##
## @ompster 						##
######################################
from tempfile import mkstemp
from shutil import move
from os import remove
import subprocess
import os
import sys

####COLOURS YO##########
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
########################

version = '0.2'
print bcolors.OKBLUE + """
	                                     
 _____     _____                 _   
|  _  |_ _|     |___ _ _ ___ ___| |_ 
|   __| | |   --|  _| | |   |  _|   |
|__|  |_  |_____|_| |___|_|_|___|_|_|
      |___|                          
      """
print bcolors.OKBLUE + 'version: ' + version + bcolors.ENDC


# example calls subprocess.call(['cmd', 'arg1', 'arg2'])

minLength = raw_input('Min length of Password \n ')
maxLength = raw_input('Max length of Password \n ')
outputFile = raw_input('Where would you like the file saved to \n ')

subprocess.call(['clear'])
print bcolors.OKGREEN + 'Will now attempt to generate the wordlist with the following paramters:' + bcolors.ENDC
print bcolors.BOLD + 'Min Length: ' + bcolors.ENDC + minLength
print bcolors.BOLD + 'Max Length: ' + bcolors.ENDC + maxLength
print bcolors.BOLD + 'The wordlist will be saved to: ' + bcolors.ENDC + outputFile
print bcolors.UNDERLINE + ""
raw_input('This can take some time, hit enter to continue...')
print bcolors.ENDC + ""
subprocess.call(['crunch', minLength, maxLength, '-o', outputFile])