import random
nums = [random.randint(0,100),random.randint(0,100),random.randint(0,100),random.randint(0,100),]
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






