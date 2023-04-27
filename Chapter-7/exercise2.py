import re
import requests
# Exercise 2: Write a program to prompt for a file name, and then read
# through the file and look for lines of the form:
# X-DSPAM-Confidence: 0.8475
# When you encounter a line that starts with “X-DSPAM-Confidence:”
# pull apart the line to extract the floating-point number on the line.
# Count these lines and then compute the total of the spam confidence
# values from these lines. When you reach the end of the file, print out
# the average spam confidence.
# Enter the file name: mbox.txt
# Average spam confidence: 0.894128046745
# Enter the file name: mbox-short.txt
# Average spam confidence: 0.750718518519
# Test your file on the mbox.txt and mbox-short.txt files.

def avg_XDSPAM(url):
    fil = downloadfile(url)
    x = []
    with open(fil, 'r') as file:
        for line in file:
            line.strip()
            if line.find('X-DSPAM-Confidence: ') == -1: continue
            y = re.findall(r"([0-9].[0-9]*)", line)
            y = float(y[0])
            x.append(y)
    return x

def downloadfile(url):
    filename = url.split('/')[-1]
    response = requests.get(url)
    with open(filename, 'wb') as f:
        f.write(response.content)
    return filename

url = input("Enter the URL: ")
x = avg_XDSPAM(url)
print(x)
print(sum(x)/len(x))
