def find_needle(needle, haystack):
    print(needle, haystack)

    for i in range(len(haystack)):
        found = False
        j = 0
        while (j < len(needle)) and ((i+j) < len(haystack)):
            if haystack[i+j] == needle[j]:
                found = True
            else:
                found = False
                break

            j += 1

        if found == True:
            return True 

    return False


haystack = "abdefghi"
needle = "def"
print(find_needle(needle, haystack))


haystack = "abdefghi"
needle = "dd"
print(find_needle(needle, haystack))


haystack = "coweatshayandgrass"
needle = "hay"
print(find_needle(needle, haystack))

