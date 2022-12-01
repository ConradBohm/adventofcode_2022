import heapq

calorie_data = open("input.txt", "r")
calorie_list = calorie_data.read().split("\n")
calorie_data.close()

intermediate_list = []
sum_calorie_list = []

for line in calorie_list:
    if line != '':
        intermediate_list.append(int(line))      
    else:
        sum_calorie_list.append(sum(intermediate_list))
        intermediate_list = []

print(max(sum_calorie_list))                    # part 1
print(sum(heapq.nlargest(3, sum_calorie_list))) # part 2
