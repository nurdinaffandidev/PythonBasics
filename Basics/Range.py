# Range - a special immutable sequence type
r = range(100, 110)
print(f"r: {r}")
print(f"r type: {type(r)}")
print(f"r length: {len(r)}")
print(f"r index 0 = {r[0]}")
print(f"r index -1 = {r[-1]}")
# print(r[11]) # IndexError: range object index out of range
print(f"index of 105 in r = {r.index(105)}")