import os

print(os.path.join('usr', 'bin', 'spam'))
print(os.getcwd())
# os.makedirs('./hello.txt')
print(os.path.abspath('.'))
print(os.path.getsize("./hello.txt"))
print(os.listdir("."))

totalsize = 0
# getting the combined size of all dirs and files in this dir
for filename in os.listdir("."):
    totalsize += os.path.getsize(os.path.join('.', filename))

print(totalsize)
