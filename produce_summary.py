
print("Day 1")
the_file = open("um-deliveries-day-1.txt")
for line in the_file:
    #for every line in the file, remove extra spaces at the right
    line = line.rstrip()

    #split the line at every bar | 
    words = line.split('|')  

    # words = (Ali Baba Watermelon, 18, 25.00)

    #redefine words at each index
    melon = words[0]
    count = words[1]
    amount = words[2]

    print(f"Delivered {count} {melon}s for total of ${amount}")
the_file.close()


# print("Day 2")
# the_file = open("um-deliveries-day-2.txt")
# for line in the_file:
#     line = line.rstrip()
#     words = line.split('|')

#     melon = words[0]
#     count = words[0]
#     amount = words[0]

#     print(f"Delivered {count} {melon}s for total of ${amount}")
# the_file.close()


# print("Day 3")
# the_file = open("um-deliveries-day-3.txt")
# for line in the_file:
#     line = line.rstrip()
#     words = line.split('|')

#     melon = words[0]
#     count = words[0]
#     amount = words[0]

#     print(f"Delivered {count} {melon}s for total of ${amount}")
# the_file.close()
