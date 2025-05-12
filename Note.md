# 1: Array and Hashing

## String operations

- Split string into a list

```Python
txt = "welcome to the jungle"

x = txt.split()

print(x)
```

- Replace space with another character
```Python
txt = "I like bananas"

x = txt.replace(" ", "")

print(x)
```

## Array operations 

- **Sort**: O(n log n)
```Python
sorted(list)
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

- Reverse a list:
```Python
list[::-1]
```

## Dictionary operations 

- Create **hash map**: O(n)
```Python
hashMap = {}

for i in range(len(s)):
    hashMap[s[i]] = 1 + hashMap.get(s[i], 0)
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


# 2. Two Pointers

- Always check if `while i < j`

# 3. Tree

- Recursive call O(h) -> Space complexity: O(h)

- Check if root is Null:

```Python
if not root: 
    return None
```

- Access left and right node: `root.left, root.right`

- DFS

- Build path from root to target: (No need for recursive call)

```Python
path = []

while root:
    path.append(root)
    if target.val < root.val:
        root = root.left
    elif target.val > root.val:
        root = root.right
    else:
        break
```