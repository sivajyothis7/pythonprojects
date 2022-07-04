name='luminartechnolab'
vowels='aeiou'
#l ==>n
#u ==>y
#m ==>n
#i ==>y

lst=['y' if i in vowels else 'n' for i in name]
print(lst)