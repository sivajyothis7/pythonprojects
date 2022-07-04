#read a string from console

#apple

#remove vowels and add balance letters to string


string=input("enter the string")
string1=''

vowels='aeiou'
for i in string:
    if i not in vowels:
        string1+=i
       
print(string1)