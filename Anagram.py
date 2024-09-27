def anagram(s):
    if len(s) % 2 != 0:
        return -1
    mid = len(s) // 2
    s1 = s[:mid]
    s2 = s[mid:]
    
    # Create frequency dictionaries for both halves
    freq1 = {}
    freq2 = {}
    
    for char in s1:
        if char in freq1:
            freq1[char] += 1
        else:
            freq1[char] = 1
    
    for char in s2:
        if char in freq2:
            freq2[char] += 1
        else:
            freq2[char] = 1
    
    # Calculate the minimum number of changes required
    changes = 0
    for char in freq1:
        if char in freq2:
            if freq1[char] > freq2[char]:
                changes += freq1[char] - freq2[char]
        else:
            changes += freq1[char]
    
    return changes

# Test cases
print(anagram('asdfjoieufoa'))  # Output: 3
print(anagram('fdhlvosfpafhalll'))  # Output: 5
print(anagram('mvdalvkiopaufl'))  # Output: 5