#Regular expression

#python package

#pattern matching

#validation

import re
s="abaaabbbbaaababababa"
count=0

#finditer(argument1,argument2)

#argument1 : find_pattern(find cheyenda data)

#argument2 : string_name
matcher=re.finditer('ab',s)

for i in matcher:
    count+=1
    print(i.start())
    print(i.group())
print(count)
