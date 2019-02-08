#!/bin/bash

if [ -f out/time.txt ]; then
	rm out/time.txt
fi

touch out/time.txt

files=$(ls -1 Ciphers/vig_group*.crypto)

for f in $files
do
	printf $f >> out/time.txt
	{ time python3 main.py break $f;} 2>>out/time.txt
	printf "\n\n" >> out/time.txt
done

printf "text*.crypto" >> out/time.txt
{ time python3 main.py break -k210 Ciphers/text*.crypto; } 2>>out/time.txt
printf "\n\n" >> out/time.txt

echo "$files timed" 
echo "text*.crypto timed together"
