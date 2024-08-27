# Task 1: Розподіл студентів за оцінками
marks = [('Alice', 87), ('Bob', 87), ('Mark', 65)]
rating = {}

for name, mark in marks:
    if mark in rating:
        rating[mark].append(name)
    else:
        rating[mark] = [name]

print("Rating by marks:", rating)

# Task 2    
def average(rating):
    total_sum = 0
    count = 0

    for mark in rating:
        students_mark = len(rating[mark])
        total_sum = total_sum + (mark * students_mark)
        count = count + students_mark
    
    average = total_sum / count
    return average

average_mark = average(rating)
print(f"The average mark is: {average_mark}")



# Task 3 



# numbers = (1, 2, 56, 1, 56, 4, 685)

# total_sum = 0
# count = 0

# for number in numbers:
#     total_sum = total_sum + number
#     count = count + 1

# average = total_sum / count

# print(f"The average value is: {average}")
