"""
Name: Zackery Vering
Project: Lab 2H
Date: 6 Sept 2018
"""
import random
print("{:_^20}").format('MAD LIBS')
nouns = ['dog', 'pineapple', 'car', 'house', 'horse', 'pizza', 'human', 'planet', 'sun', 'fortress', 'chainsaw', 'grim reaper']
verbs = ['ran', 'jumped', 'drove', 'typed', 'battled', 'slept', 'found', 'talked', 'bounced', 'climbed', 'swung']
adjectives = ['good', 'bad', 'interesting', 'large', 'tiny', 'metallic', 'funny', 'loud', 'slow']
adverbs = ['quickly', 'weirdly', 'deviously', 'randomly', 'oddly', 'literally']
#mad lib 1
noun_select = random.sample(xrange(0, 11), 5)
verb_select = random.sample(xrange(0, 10), 5)
adjective_select = random.sample(xrange(0, 8), 5)
adverb_select = random.sample(xrange(0, 5), 3)
noun_list1 = [nouns[noun_select[0]], nouns[noun_select[1]], nouns[noun_select[2]], nouns[noun_select[3]], nouns[noun_select[4]]]
verb_list1 = [verbs[verb_select[0]], verbs[verb_select[1]], verbs[verb_select[2]], verbs[verb_select[3]], verbs[verb_select[4]]]
adjectives_list1 = [adjectives[adjective_select[0]], adjectives[adjective_select[1]], adjectives[adjective_select[2]], adjectives[adjective_select[3]], adjectives[adjective_select[4]]]
adverbs_list1 = [adverbs[adverb_select[0]], adverbs[adverb_select[1]], adverbs[adverb_select[2]]]
user_words1 = []
for i in range(len(noun_list1)):
    print ("{}: {}").format(i+1, noun_list1[i])
    i +=1
user_words1.append(noun_list1[int(raw_input("Please select a noun.\n"))-1])
print("{:_^20}").format("")
for j in range(len(verb_list1)):
    print ("{}: {}").format(j+1, verb_list1[j])
    j += 1
user_words1.append(verb_list1[int(raw_input("Please select a verb.\n"))-1])
print("{:_^20}").format("")
for y in range(len(adjectives_list1)):
    print ("{}: {}").format(y+1, adjectives_list1[y])
    y +=1
user_words1.append(adjectives_list1[int(raw_input("Please select an adjective.\n"))-1])
print("{:_^20}").format("")
for x in range(len(adverbs_list1)):
    print ("{}: {}").format(x+1, adverbs_list1[x])
    x += 1
user_words1.append(adverbs_list1[int(raw_input("Please select an adverb.\n"))-1])
print("{:_^20}").format("")
for z in range(len(noun_list1)):
    print ("{}: {}").format(z+1, noun_list1[z])
    z += 1
user_words1.append(noun_list1[int(raw_input("Please select a noun.\n"))-1])
print("{:_^20}").format("")
print("Your choices were:\nnoun: {}\nverb: {}\nadjective: {}\nadverb: {}\nnoun: {}").format(user_words1[0], user_words1[1], user_words1[2], user_words1[3], user_words1[4])
print("{:_^20}").format("")
print("The {} {} {} {} the {}.").format(user_words1[2], user_words1[0], user_words1[3], user_words1[1], user_words1[4])

""" disabled to test functionality
#mad lib 2
noun_list2 = [nouns[random.randint(0, 11)], nouns[random.randint(0, 11)], nouns[random.randint(0, 11)], nouns[random.randint(0, 11)], nouns[random.randint(0, 11)]]
verb_list2 = [verbs[random.randint(0, 10)], verbs[random.randint(0, 10)], verbs[random.randint(0, 10)], verbs[random.randint(0, 10)], verbs[random.randint(0, 10)]]
adjectives_list2 = [adjectives[random.randint(0, 8)], adjectives[random.randint(0, 8)], adjectives[random.randint(0, 8)], adjectives[random.randint(0, 8)], adjectives[random.randint(0, 8)]]
adverbs_list2 = [adverbs[random.randint(0, 5)], [adverbs[random.randint(0, 5)], [adverbs[random.randint(0, 5)]]
i = j = y = x = 1
user_words2 = []
for i in range(noun_list2):
    print ("{}: {}").format(i, noun_list2[i-1])
user_words2.append(noun_list2[int(raw_input("Please select a noun.\n"))-1])
for j in range(verb_list2):
    print ("{}: {}").format(j, verb_list2[j-1])
user_words2.append(verb_list2[int(raw_input("Please select a verb.\n"))-1])
for y in range(adjectives_list2):
    print ("{}: {}").format(y, adjectives_list2[y-1])
user_words2.append(adjectives_list2[int(raw_input("Please select an adjective.\n"))-1])
for x in range(adverbs_list2):
    print ("{}: {}").format(x, adverbs_list2[x-1])
user_words2.append(adverbs_list2[int(raw_input("Please select an adverb.\n"))-1])"""

""" just to simplify things at the moment
#mad lib 3
noun_list3 = []
verb_list3 = []
adjectives_list3 = []
adverbs_list3 = []
user_words3 = []

#mad lib 4
noun_list4 = []
verb_list4 = []
adjectives_list4 = []
adverbs_list4 = []
user_words4 = []

#mad lib 5
noun_list5 = []
verb_list5 = []
adjectives_list5 = []
adverbs_list5 = []
user_words5 = []"""
