def countPerms(s, l):

    def compare(s, poss):
        for i in xrange(len(poss)):
            if poss[i] in s:
                position = s.index(poss[i])
                s = s[:position] + s[position+1:]
            else:
                return False
        return True

    count = 0

    for i in xrange(len(l)-len(s)+1):
        currSubstring = l[i:i+len(s)]
        if compare(s,currSubstring):
            count += 1
    return count

print(countPerms("abc", "abc"))
print(countPerms("abc", "abca"))
