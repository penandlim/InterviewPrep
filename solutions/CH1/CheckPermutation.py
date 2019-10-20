def checkPermutation(s1, s2):

    if (len(s1) is not len(s2)):
        return False

    countMap = {}

    for c in s1:
        if (c in countMap):
            countMap[c] += 1
        else:
            countMap[c] = 1

    for c in s2:
        if (c in countMap):
            countMap[c] -= 1
            if (countMap[c] < 0):
                return False
        else:
            return False

    return True

def test(arr):
    for a in arr:
        print("Input: " + a[0] + ", " + a[1])
        print("Output: " + str(checkPermutation(a[0], a[1])) + "\n")

test([
    ["abs", "asb"],
    ["1abs", "asb1"],
    [" asd", "  asd"]
])