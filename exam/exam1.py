master_string="abbcddeghgggt"
chk_word="egg"


res=""

dic={}

for i in master_string:
    if i in dic:
        dic[i]+=1
    else:
        dic[i]=1