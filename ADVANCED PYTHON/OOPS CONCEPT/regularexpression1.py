s="qwweewqwewqwerrreere"
count=0

import re

match=re.finditer('qw',s)

for i in match:
    count+=1
    print(i.start())
    print(i.group())
print(count)
