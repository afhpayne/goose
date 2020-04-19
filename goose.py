#!/usr/bin/env python3

# Andrew Payne, contact(*t)duckbrainsoftware(d*t)com 
# MIT License

# Copyright (c) 2018-2020 Andrew Payne

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.


import os
from csv import reader
import re
import shutil
import sys
import time

# Software information
soft_name = "goose.py"
soft_tag  = "a contact converter for Mutt and Alpine"

# Software version
soft_vers = "0.2.0"

# User home
user_home = os.environ['HOME']

# Work directory (can change this to any user directory)
work_dir = "/tmp/"

# email address search
email_address = re.compile("^([a-zA-Z0-9_\-\.]+)@([a-zA-Z0-9_\-\.]+)\.([a-zA-Z]{2,5})$")

# Lists we're about to use
alpine_format = []
mutt_format = []

# Arguments
# -a (--alpine) means import for alpine only
# -m (--mutt) means import for mutt only
try:
    arg_1 = sys.argv[1]
    print(arg_1)
except(IndexError):
    arg_1 = "0"
    pass


def parse_csv_func():
    # read csv file as a list of lists
    with open(os.path.join(user_home, 'Downloads/contacts.csv'), 'r') as csv_obj:
        # pass the file object to reader() to get the reader object
        csv_reader = reader(csv_obj)
        # Pass reader object to list() to get a list of lists
        list_of_rows = list(csv_reader)
        # print(list_of_rows)
        for row in list_of_rows:
            if row[0]:
                full_name=row[0]            
            if row[1] and row[1] not in row[0]:
                full_name=row[1]
            if row[2] and row[2] not in row[0]:
                full_name=row[1] + " " + row[2]
            if row[3] and row[3] not in row[0]:
                full_name=row[1] + " " + row[2] + " " + row[3]
    
            full_name=full_name.strip()
            full_name=full_name.replace(".", "")
            full_name=full_name.replace("  ", " ")
    
            nick_name=full_name.lower().replace(" ", "_")
            nick_name=nick_name.replace("'", "")
    
            multi = 0
            for item in row:
                if item:
                    item = item.split(" ")
                    regsearch = email_address.match(str(item[0]))
                    if regsearch is not None:
                        multi += 1
                        if multi > 1:
                            alpine_format.append \
                                (nick_name + "_" + str(multi) + "\t" + full_name + "\t" + regsearch[0])
                            mutt_format.append \
                                ("alias" + " " + nick_name + "_" + str(multi) + " " + full_name + " " + "<" + regsearch[0] + ">")
                        else:
                            alpine_format.append(nick_name + "\t" + full_name + "\t" + regsearch[0])
                            mutt_format.append("alias" + " " + nick_name + " " + full_name + " " + "<" + regsearch[0] + ">")

def write_alpine_func():
    with open(work_dir + 'addressbook', mode='wt', encoding='utf-8') as addressbook:
        for line in alpine_format:
            addressbook.write(''.join(line + "\n"))

def write_mutt_func():
    with open(work_dir + 'aliases', mode='wt', encoding='utf-8') as aliases:
        for line in mutt_format:
            aliases.write(''.join(line + "\n"))

def alpine_backup_func():
    alpine_path = os.path.join(user_home, ".alpine/")
    if os.path.isfile(alpine_path + "addressbook"):
        shutil.copy2(alpine_path + "addressbook", work_dir + "addressbook" + "_" + str(time.monotonic()))
        shutil.copy2(alpine_path + "addressbook", alpine_path + "addressbook" + "_BACKUP")
        shutil.copy2(work_dir + "addressbook", alpine_path + "addressbook")

def mutt_backup_func():
    mutt_path = os.path.join(user_home, ".mutt/")
    if os.path.isfile(mutt_path + "aliases"):
        shutil.copy2(mutt_path + "aliases", work_dir + "aliases" + "_" + str(time.monotonic()))
        shutil.copy2(mutt_path + "aliases", mutt_path + "aliases" + "_BACKUP")
        shutil.copy2(work_dir + "aliases", mutt_path + "aliases")

def stop_or_go_func():
    print("")
    print("Please download your contacts.csv or google.csv to " + user_home + "/Downloads" )
    user_nag = input("Continue y/n? ")
    if user_nag == "Y" or user_nag == "y":
        pass
    else:
        exit(1)

# Let's get started
if arg_1 == "--alpine" or arg_1 == "-a":
        stop_or_go_func()
        parse_csv_func()
        write_alpine_func()
        alpine_backup_func()
        print("--> Imported contacts to Alpine\n")
        exit(0)

elif arg_1 == "--mutt" or arg_1 == "-m":
        stop_or_go_func()
        parse_csv_func()
        write_mutt_func()
        mutt_backup_func()
        print("--> Imported contacts to Mutt\n")
        exit(0)

else:
    os.system('clear')
    print("")
    print("Welcome to Goose " + str(soft_vers) + ", " + str(soft_tag) + ".")
    print("")
    print("Please download your contacts.csv or google.csv to " + user_home + "/Downloads" )

    stay_main = 0        
    while stay_main == 0:
        mutt_or_alp = input("\nImport to (A)lpine, (M)utt, (B)oth, or (Q)uit? ")
        if mutt_or_alp == "Q" or mutt_or_alp == 'q':
            stay_main = 1
            exit(0)
        elif mutt_or_alp == "A" or mutt_or_alp == "a":
            stay_main = 1
            parse_csv_func()
            write_alpine_func()
            alpine_backup_func()
            print("--> Imported contacts to Alpine\n")
            exit(0)
        elif mutt_or_alp == "M" or mutt_or_alp == "m":
            stay_main = 1
            parse_csv_func()
            write_mutt_func()
            mutt_backup_func()
            print("--> Imported contacts to Mutt\n")
            exit(0)
        elif mutt_or_alp == "B" or mutt_or_alp == "b":
            stay_main = 1
            parse_csv_func()
            write_alpine_func()
            write_mutt_func()
            mutt_backup_func()
            alpine_backup_func()
            print("--> Imported contacts to Alpine and Mutt\n")
            exit(0)

