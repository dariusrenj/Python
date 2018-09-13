"""Name: Zackery Vering
    Project: Python2 lab2f
    Date: 5 Sept 2018"""
print "==================================="
print "This program will check if two words entered are anagrams."
#take in the user's words
user_string = raw_input("Input the first word.\n").lower()
user_string2 = raw_input("Input the second word.\n").lower()
#check to see if the words are the same length
if (len(user_string)!=len(user_string2)):
    print "The words are different lengths and can not be anagrams."
    #sort the strings to compare
else:
    letters = [sorted(user_string.split()[0])]
    letters2 = [sorted(user_string2.split()[0])]
    #if the lists match, let the user know the words are anagrams
    if (letters == letters2):
        print "{} and {} are anagrams.".format(user_string, user_string2)
    else:
        #if the lists don't match, let the user know the words are not anagrams
        print "{} and {} are not anagrams.".format(user_string, user_string2)