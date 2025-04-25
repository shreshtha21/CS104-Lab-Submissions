#!/bin/bash
echo "rollno,quiz1,quiz2,midsem,endsem,total-marks,grades" > ug23.csv
echo "rollno,quiz1,quiz2,midsem,endsem,total-marks,grades" > ug24.csv
touch temp23.csv temp24.csv
touch temps23.csv temps24.csv
grep -E "^23" $1 | cut -d ',' -f -6 >> temp23.csv
grep -E "^24" $1 | cut -d ',' -f -6 >> temp24.csv
while IFS=',' read -r -a arr; do
    arr[5]=$(echo "${arr[5]}" | tr -d '\r')
    if [[ ${arr[5]} > "85" ]]; then
    arr[6]="AA"
    elif [[ ${arr[5]} > "65" ]]; then
    arr[6]="AB"
    elif [[ ${arr[5]} > "45" ]]; then
    arr[6]="BB"
    elif [[ ${arr[5]} > "35" ]]; then
    arr[6]="CC"
    else 
    arr[6]="F"
    fi
    echo "${arr[0]},${arr[1]},${arr[2]},${arr[3]},${arr[4]},${arr[5]},${arr[6]}" >> temps23.csv
done < temp23.csv
while IFS=',' read -r -a arr; do
    arr[5]=$(echo "${arr[5]}" | tr -d '\r')
    if [[ ${arr[5]} > "85" ]]; then
    arr[6]="AA"
    elif [[ ${arr[5]} > "65" ]]; then
    arr[6]="AB"
    elif [[ ${arr[5]} > "45" ]]; then
    arr[6]="BB"
    elif [[ ${arr[5]} > "35" ]]; then
    arr[6]="CC"
    else 
    arr[6]="F"
    fi
    echo "${arr[0]},${arr[1]},${arr[2]},${arr[3]},${arr[4]},${arr[5]},${arr[6]}" >> temps24.csv
done < temp24.csv
sort -t ',' -k7,7 -k1,1n temps23.csv >> ug23.csv
sort -t ',' -k7,7 -k1,1n temps24.csv >> ug24.csv
rm temp23.csv
rm temp24.csv
rm temps23.csv
rm temps24.csv