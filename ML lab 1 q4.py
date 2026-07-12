
def highestChar(text):
    maxChar = ""
    maxCount = 0
    for ch in text:
        if ch.isalpha():
            count = text.count(ch)
            if count > maxCount:
                maxCount = count
                maxChar = ch
    return maxChar, maxCount
inputst= input("Enter a string: ")
character, count = highestChar(inputst)
print("Highest character =", character)
print("Occurrence count =", count)