def main():
    data = open('alice30.txt')
    wordList = data.read().split()
    count = {}
    for w in wordList:
        w = w.lower()
        count[w] = count.setdefault(w,0) + 1

    keyList = count.keys()
    keyList = sorted(keyList)
    for k in keyList:
        print("%-20s occured %4d times" % (k, count[k]))

main()
