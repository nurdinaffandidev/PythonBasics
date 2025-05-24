from pathlib import Path
'''
 Absolute path:
 c:\ Program Files\Microsoft (microsoft)
 /usr/local/bin (linux/macOS)

 Relative path:
 path starting from current directory
'''
path = Path()
print(path.absolute())
print(path.exists())
print()

path1 = Path("emails")
# path1.mkdir()
# path1.rmdir()

path2 = Path()
# for file in path.glob("*"):
# for file in path.glob("*.*"):
for file in sorted(path.glob("*.py")):
    print(file)