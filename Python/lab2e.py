"""Name: Zackery Vering
    Project: Python2 lab2e
    Date: 5 Sept 2018"""
print "==================================="
user_string = raw_input("Input a sentence.\n")
print "There are {} words in your sentence.\n".format(len(user_string.split(" ")))
print "There are {} upper case letters in your sentence.\n".format(sum(1 for c in user_string if c.isupper))
print "There are {} lower case letters in your sentence.\n".format(sum(1 for d in user_string if d.islower))