"""
Given a string, find the length of the longest substring
without repeating characters.

Examples:
Given "abcabcbb", the answer is "abc", which the length is 3.
Given "bbbbb", the answer is "b", with the length of 1.
Given "pwwkew", the answer is "wke", with the length of 3.
Note that the answer must be a substring,
"pwke" is a subsequence and not a substring.
"""


def longest_non_repeat_v1(string):
    """
    Find the length of the longest substring
    without repeating characters.
    """
    if string is None:
        return 0
    dict = {}
    max_length = 0
    j = 0
    for i in range(len(string)):
        if string[i] in dict:
            j = max(dict[string[i]], j)
        dict[string[i]] = i + 1
        max_length = max(max_length, i - j + 1)
    return max_length

def longest_non_repeat_v2(string):
    """
    Find the length of the longest substring
    without repeating characters.
    Uses alternative algorithm.
    """
    if string is None:
        return 0
    start, max_len = 0, 0
    used_char = {}
    for index, char in enumerate(string):
        if char in used_char and start <= used_char[char]:
            start = used_char[char] + 1
        else:
            max_len = max(max_len, index - start + 1)
        used_char[char] = index
    return max_len

# get functions of above, returning the max_len and substring
def get_longest_non_repeat_v1(string):
    """
    Find the length of the longest substring
    without repeating characters.
    Return max_len and the substring as a tuple
    """
    if string is None:
        return 0, ''
    sub_string = ''
    dict = {}
    max_length = 0
    j = 0
    for i in range(len(string)):
        if string[i] in dict:
            j = max(dict[string[i]], j)
        dict[string[i]] = i + 1
        if i - j + 1 > max_length:
            max_length = i - j + 1
            sub_string = string[j: i + 1]
    return max_length, sub_string

def get_longest_non_repeat_v2(string):
    """
    Find the length of the longest substring
    without repeating characters.
    Uses alternative algorithm.
    Return max_len and the substring as a tuple
    """
    if string is None:
        return 0, ''
    sub_string = ''
    start, max_len = 0, 0
    used_char = {}
    for index, char in enumerate(string):
        if char in used_char and start <= used_char[char]:
            start = used_char[char] + 1
        else:
            if index - start + 1 > max_len:
                max_len = index - start + 1
                sub_string = string[start: index + 1]
        used_char[char] = index
    return max_len, sub_string


## My solution solved unseen

def unique(string):
    return len(set(string)) == len(string)

def longest_unique(string):
    if len(string) == 0:
        return 0
    if len(string) == 1:
        return 1
    p0 = 0
    p1 = 1
    max_length = 0
    while p1 < len(string):
        if unique(string[p0:p1+1]):
            curr_length = len(string[p0:p1+1])
            print(string[p0:p1+1])
            p1 += 1   
        else:
            p0 += 1
            curr_length = 0
            
        max_length = max(max_length, curr_length)

    return max_length
            
print(longest_unique('bbbbb'))
