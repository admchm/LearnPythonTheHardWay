## Study Drill #3: 
## Find the Python documentation on lists and read about them. What other operations can you do to lists besides append?

# Answer: 
# search: python lists site:python.org:
# https://docs.python.org/3/library/stdtypes.html#lists

# s.append(x) - appends x to the end of the sequence (same as s[len(s):len(s)] = [x])
# s.clear() - removes all items from s (same as del s[:])
# s.copy() - creates a shallow copy of s (same as s[:])
# s.extend(t) or s += t - extends s with the contents of t (for the most part the same as s[len(s):len(s)] = t)
# s *= n - updates s with its contents repeated n times
# s.insert(i, x) - inserts x into s at the index given by i (same as s[i:i] = [x])
# s.pop() or s.pop(i) - retrieves the item at i and also removes it from s
# s.remove(x) - remove the first item from s where s[i] is equal to x
# s.reverse() - reverses the items of s in place