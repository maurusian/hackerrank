#Problen enunciation: https://www.hackerrank.com/challenges/ginorts/problem
# Enter your code here. Read input from STDIN. Print output to STDOUT

def reverse_ascii(ch):
    """
    Returns value depending on the
    character type.
    """
    if ord(ch) < 58:
        return 1000
    elif ord(ch) < 93:
        return 500
    else:
        return 0

def chr_num_value(ch):
    """
    Returns value depending on
    whether the character ch
    is a number or a letter,
    and whether a number is
    even or odd.
    """
    try:
        x = int(ch)
        return 1-x%2
    except:
        return -100

def attach(ss):
    """
    Attaches a list of characters ss
    together as a string xx.
    """
    xx = ""
    for i in range(len(ss)):
        xx+=ss[i]
    return xx

string = input()

ss     = attach(sorted(string, key = lambda x: (reverse_ascii(x),chr_num_value(x),x)))

#print(sorted([1,-1,2,-4]))
print(ss)
