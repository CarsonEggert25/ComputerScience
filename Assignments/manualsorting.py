import random
nums = [random.randint(0,100),random.randint(0,100),random.randint(0,100),random.randint(0,100),random.randint(0,100),]
print(nums)

def bubble_sort(numbers):
    steps = 0
    for j in range(0,len(nums)-1):
        for i in range(0, len(numbers) - 1):
            if numbers[i] > numbers[i+1]:
                numbers[i], numbers[i+1] = numbers[i+1], numbers[i]
                steps += 1
    print(numbers)
    print("competed in " + str(steps) + "steps.")

bubble_sort(nums)

nums = [random.randint(0,100),random.randint(0,100),random.randint(0,100),random.randint(0,100),random.randint(0,100),]
print(nums)
def quick_sort(n):
    pivot = n[-1]

    lpos = 0
 #first number from the left that is larger
 #first number from the right that is smaller
    for j in range(0,len(n)):

        for i in range(0,len(n)):
            if n[i] > pivot:
                lpos = i
                break

        for i in range(len(n)-1, -1, -1):
            if n[i] < pivot:
                rpos = i
                break

        if lpos > rpos:
            n[lpos], n[-1] = n[-1], n[lpos]
            break
        else:
        

            n[lpos], n[rpos] = n[rpos], n[lpos]

    
   
    print(n)






