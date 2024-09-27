def isBalanced(s):
    while True:
        original_n = len(s)
        s = s.replace('()','')
        s = s.replace('[]','')
        s = s.replace('{}','')
        new_n = len(s)
        if new_n == original_n :
            break
    if len(s) == 0 :
        return 'YES'
    else :
        return 'NO'