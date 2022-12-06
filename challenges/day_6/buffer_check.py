buffer = open("input.txt", "r")
buffer = buffer.read()
marker_check = []
message_check = []
counter = 0
buffer_counter = 0

for i in buffer:
    counter += 1
    marker_check.append(i)
    message_check.append(i)
    
    if len(marker_check) == 4 and len(marker_check) == len(set(marker_check)):
        if not buffer_counter:
            buffer_counter = counter
        

    if len(message_check) == 14 and len(message_check) == len(set(message_check)):
        message_counter = counter
        break
    
    if len(marker_check) == 4:
        marker_check.pop(0)

    if len(message_check) == 14:
        message_check.pop(0)

print(buffer_counter)
print(message_counter)