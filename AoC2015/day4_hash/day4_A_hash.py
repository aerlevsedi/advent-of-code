import hashlib

file = open("task4_hash_input.txt")
word = file.readline()

for i in range(0, 100000000) :
    msg = word + str(i)
    res = hashlib.md5(msg.encode('utf-8')).hexdigest()
    if res.startswith("000000") :
        print(i)
        break

