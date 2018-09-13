"""Name: Zackery Vering
    Project: Python2 lab2d
    Date: 5 Sept 2018"""
print "==================================="
user_string = raw_input("Input a sentence.\n")
reverse_string = user_string[::-1].upper()
print "Here is your input reversed and upper cased:\n{}".format(reverse_string)
split_string = user_string.split(' ')
print "Here is your input split by spaces:\n{}".format(split_string)