#Problem enunciation:
#https://www.hackerrank.com/challenges/validating-credit-card-number/problem
# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

#16 numbers starting with 4, 5 or 6
pattern0 = r"^[456][0-9]{15}$"
#correct separator (if available) at the correct locations
pattern1 = r"^[456][0-9]{3}\-[0-9]{4}\-[0-9]{4}\-[0-9]{4}$"
#consecutive 4 or more identical digits
pattern2 = r'.*(\d)(\1{3,}).*'

N = int(input())
for _ in range(N):
    card_num = input()
    mm0 = re.match(pattern0,card_num)
    #mm1 = re.match(pattern0,card_num.replace('-',''))
    mm2 = re.match(pattern1,card_num)
    mm3 = re.match(pattern2,card_num.replace('-',''))
    if (mm0 is None and mm2 is None) or mm3 is not None:
        print("Invalid")
    else:
        print("Valid")
