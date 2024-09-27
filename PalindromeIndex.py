def palindrome_index(s):
    def is_palindrome(s):
        return s == s[::-1]
    if is_palindrome(s):
        return -1
    n = len(s)
    for i in range(n // 2):
        if s[i] != s[n - 1 - i]:
            left_removed = s[:i] + s[i + 1:]
            right_removed = s[:n - 1 - i] + s[n - i:]
            if is_palindrome(left_removed):
                return i
            elif is_palindrome(right_removed):
                return n - 1 - i
            else:
                return -1

    return -1
s = 'xabbax'
print(s[::-1])
print(palindrome_index(s))
