list = open("input.txt", "r")
rucksacks = list.read().split("\n")
list.close()

shared_items = []
three_sack_shared = []

def eval_priority_total(item_list):
    total = 0
    for item in item_list:
        if item.isupper():
            total += ord(item) - 38
        else:
            total += ord(item) - 96
    return total

for rucksack in rucksacks:
    half_length = int(len(rucksack)/2)

    front = rucksack[:half_length]
    back = rucksack[half_length:]

    for item in front:
        if item in back:
            shared_items.append(item)
            break

print(eval_priority_total(shared_items)) # step 1

for i in range(0, len(rucksacks), 3):
    for item in rucksacks[i]:
        if item in rucksacks[i+1] and item in rucksacks[i+2]:
            three_sack_shared.append(item)
            break

print(eval_priority_total(three_sack_shared)) # step 2