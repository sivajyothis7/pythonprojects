# Find all of the numbers from 1-1000 that are divisible by 7
# Find all of the numbers from 1-1000 that have a 3 in them
# Count the number of spaces in a string
# Create a list of all the consonants in the string “Yellow Yaks like yelling and yawning and yesturday they yodled while eating yuky yams”

lst=[i for i in range(1,1001) if i%7==0]
print(lst)

lst=[i for i in range(1,1001) if '3' in str(i)]
print(lst)

list='Yellow Yaks like yelling and yawning and yesturday they yodled while eating yuky yams'
lst=[i for i in list if i==' ']
print(len(lst))

list='Yellow Yaks like yelling and yawning and yesturday they yodled while eating yuky yams'
vowels='aeiou'

lst=[i for i in list if i not in vowels]
print(lst)