# Exercise 1: Write a program to read through a file and print the contents
# of the file (line by line) all in upper case. Executing the program will
# look as follows:
# python shout.py
# Enter a file name: mbox-short.txt
# FROM STEPHEN.MARQUARD@UCT.AC.ZA SAT JAN 5 09:14:16 2008
# RETURN-PATH: <POSTMASTER@COLLAB.SAKAIPROJECT.ORG>
# RECEIVED: FROM MURDER (MAIL.UMICH.EDU [141.211.14.90])
# BY FRANKENSTEIN.MAIL.UMICH.EDU (CYRUS V2.3.8) WITH LMTPA;
# SAT, 05 JAN 2008 09:14:16 -0500
# You can download the file from www.py4e.com/code3/mbox-short.txt

import requests

def shout_out(file_url):
    file_name = downloadfile(file_url)
    fhand = open(file_name)
    for line in fhand:
        line = line.strip().upper()
        print(line)

def downloadfile(url):
    file_name = url.split('/')[-1]
    response = requests.get(url)
    with open(file_name, 'wb') as f:
        f.write(response.content)
    return file_name

file_url = input("Enter a file url: ")
shout_out(file_url)