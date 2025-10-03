from input_handler import open_file

input_list = open_file("Puzzle input.txt")

left_list = []
right_list = []
total_difference = 0

for i in range(len(input_list)):
    split_list = input_list[i].split("   ")
    input_list[i] = split_list
    
for i in range(len(input_list)):
    left_list.append(input_list[i][0])
    right_list.append(input_list[i][1])
    
left_list.sort()
right_list.sort()

for i in range(len(input_list)):
    current_difference =  abs(int(left_list[i]) - int(right_list[i]))
    #print(current_difference)
    total_difference = total_difference + current_difference
    
print(total_difference)
    