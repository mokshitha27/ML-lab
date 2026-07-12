import random
def genlist():
    numbers=[]
    for i in range(25):
        numbers.append(random.randint(1, 10))
    return numbers
def mean(numbers):
    return sum(numbers)/len(numbers)
def median(numbers):
    numbers.sort()
    return numbers[len(numbers)//2]
def mode(numbers):
    mode=numbers[0]
    max_count=0
    for i in numbers:
        count=numbers.count(i)
        if count>max_count:
            max_count=count
            mode=i
    return mode,max_count
def main():
    numbers=genlist()
    print("Generated list:",numbers)
    print("Mean:",mean(numbers))
    print("Median:",median(numbers))
    print("Mode:",mode(numbers))
main()