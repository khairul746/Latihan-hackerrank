def pangrams(s):
    # Write your code here
    alphabets = 'abcdefghijklmnopqrstuvwxyz'
    count = 0
    for alphabet in alphabets:
        if alphabet in s or alphabet.upper() in s:
            count += 1
    if count == 26:
        return 'pangram'
    else:
        return 'not pangram'
    
s = 'We promptly judged antique ivory buckles for the prize'
print(pangrams(s))