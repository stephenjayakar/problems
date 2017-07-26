import sys

arr = []
for arr_i in range(6):
    arr_t = [int(arr_temp) for arr_temp in input().strip().split(' ')]
    arr.append(arr_t)

largest_sum = "Not Instantiated"

for i in range(4):
    for j in range(4):
        hourglass = [arr[i][j], arr[i][j + 1], arr[i][j + 2],
                     arr[i + 1][j + 1],
                     arr[i + 2][j], arr[i + 2][j + 1], arr[i + 2][j + 2]]
        hourglass_sum = sum(hourglass)
        if largest_sum == "Not Instantiated" or hourglass_sum > largest_sum:
            largest_sum = hourglass_sum
print(largest_sum)
            
def hourglass_sum(lst):
    return sum(lst)
