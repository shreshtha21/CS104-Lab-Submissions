#!/bin/bash
if [[ $# -ne 1 ]]; then
    echo  "Usage: ./getEmails.sh <file>"
elif [[ ! -e $1 ]]; then
    echo "Input File doesn't exist"
else
    grep -E "[A-Z0-9a-z]+@[A-Za-z]+\.iitb\.ac\.in" $1 > emails.txt
    sort -rfd emails.txt > sortedEmails.txt
    grep -E "[A-Z0-9a-z]+@cse\.iitb\.ac\.in" sortedEmails.txt > cseEmails.txt
fi