results = [
    {"district":"tvm","win": 98, "A+": 45000},
    {"district":"ktm","win": 95, "A+": 44000},
    {"district":"apy","win": 97, "A+": 47000},
    {"district":"idk","win": 90 ,"A+": 38000},
    {"district":"ekm","win": 99, "A+": 56000},
    {"district":"pta","win": 99, "A+": 58000},
    {"district":"tsr","win": 98, "A+": 57000},
    {"district":"kzd","win": 99, "A+": 58000},
    {"district":"pkd","win" :95, "A+": 50000},
    {"district":"mpm","win": 90,"A+": 4500},

]

#win % of tvm
#district with highest win %
#district with lowest win %
#district with highest A+
#district with lowest A+
#total number of A+
#total win %
#sort district ert win % in asc. order


#1. win % of tvm

print([res["win"] for res in results if res["district"]=="tvm")


for i in results:
    if i["district"]=="tvm":
        print((i["win"]))

#2. district with highest win %

print(max(results,key=lambda res:res["win"]))

#district with lowest win %
print(min(results,key=lambda res:res["win"]))

#district with highest A+
print(max(results,key=lambda res:res["A+"]))

#district with lowest A+
low=min(results,key=lambda res:res["A+"])
print(low["district"])

#sort district ert win % in asc. order

results.sort(key=lambda res:res["win"])
print(results)

#total number of A+
print(sum(res["A+"] for res in results))

print(sum(res["win"] for res in results))