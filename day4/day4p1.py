import hashlib
import re

key = "iwrupvqb"
num = 0

while True:
    encoded = hashlib.md5()
    new_key = key+str(num)
    encoded.update(new_key)
    hash = encoded.hexdigest()
    if re.match(r"^00000", hash):
        print "Done"
        break
    num += 1

print num
