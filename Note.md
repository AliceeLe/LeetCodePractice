# 1: Array and Hashing

- **Sort**: O(n log n)
```Python
sorted(list)
```

- Create **hash map**: O(n)
```Python
hashMap = {}

for i in range(len(s)):
    hashMap[s[i]] = 1 + hashMap.get(s[i], 0)
```

- Enumerated a list: O(n)
```Python
    indexList = list(enumerate(nums))
    # Input: nums = [7, 5, 3]
    # Output: [(0, 7), (1, 5), (2, 3)]
```

- Sort an enumerated list based on 2nd element
```Python
    indexList = sorted(indexList, key=lambda x: x[1])
    # Key: sorted based on x[1]
```

- Return list of dictionary values
```Python
return list(hashMap.values())
```

- Create dictionary of 'a -> 'b list:
```Python
hashMap = {}

if key not in hashMap:
    hashMap[key] = [value]
else:
    hashMap[key].append
```