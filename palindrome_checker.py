def isPalindrome(s):
    print(s)
    leftIndex = 0
    rightIndex = len(s)-1
    while(leftIndex < len(s)//2):
        if(s[leftIndex] != s[rightIndex]):
            return False

        leftIndex += 1
        rightIndex -= 1

    return True


print(isPalindrome("kayak"))
print(isPalindrome("sees"))
print(isPalindrome("varun"))

