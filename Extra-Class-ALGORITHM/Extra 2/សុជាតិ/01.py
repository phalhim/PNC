#1 សេលសេ function ល ើមាបីគុណលលខទាំងអស់កនុងបញ្ជីមួយ។

def sums(number):
    sum =0
    for i in range(len(number)):
        sum += number[i]
    return sum
result =eval(input("have number:  "))
print(sums(result))