strs = ["eat", "tea", "tan", "ate","nat", "bat"]
opt = []


for i in range(len(strs)):
    for j in range(len(strs)):
        list = []
        if sorted(strs[i]) == sorted(strs[j]):
            list.append(list)

opt.append(list)
print(opt)