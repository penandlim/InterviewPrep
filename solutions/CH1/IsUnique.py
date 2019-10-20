def isUnique(s):
    countMap = {}

    for c in s:
        if (c in countMap):
            return False
        else:
            countMap[c] = 1
    return True

def test(arr):
    for a in arr:
        print("Input: " + a)
        print("Output: " + str(isUnique(a)) + "\n")

test(["asda  sd", "a  bc", "awwww2"])