"# DNHS-Hackathon" 

Tracker:
How it works
Covid Tracker:
simple, uses a built in package that you can install via os.system('pip install COVID19Py')
You can track by country, either country name or 2 digit country code, uses country package to do conversions
Package Tracker:
Steps:
Shorten URL
Get Product
Get Price
Get Details
Put into MongoDB database
Get data from MongoDB database
put into file
For more questions, DM me at Monchi King#7034
Track bootime:
Needed packages:
psutil
datetime
os
Steps:
Get boot time
Get boot time by seconds
Get boot time by date
Put into file
Remove multiple boottimes in case ran multiple times
Gets average boot time
returns current vs average boot time

DeHasher:
3 types
Brute
Dictionary
Wordlist
Dictionary uses a pre built-in english dictionary
One is uppercase, one is lowercase
creates set amount of threads to run faster, hashes possible string in 6 different hashes, sha 224, sha256, sha 384, sha 512, MD5
Brute force:
puts all characters into file
converts current repitetion number to base of how many characters are in file
hashes them like DIctionary
Wordlist:
uses wordlist provided by user
hashes all things
looks for similarities
Directory Buster:
3 types
Brute
Dictionary
Wordlist
similar as last except it uses ping instead of hashing the strings
The ping uses requests.head.status_code to get status code
checks for 404
if 404 or another version of 404, e.g. 403, it returs false, else, it returns true
