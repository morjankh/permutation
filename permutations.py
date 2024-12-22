def permutations(s):
    if len(s) == 1:
        return [s]


    result = []
    for i, char in enumerate(s):
        remaining = s[:i] + s[i+1:]
        for perm in permutations(remaining):
            result.append(char + perm)
    
    return result


print(permutations("abc"))
