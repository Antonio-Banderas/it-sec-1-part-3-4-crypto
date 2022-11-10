from passlib.hash import sha512_crypt

# hash to be cracked:
saltToSearch = "penguins"
password = "$6$penguins$eP.EvNiF2A.MmRVWNgGj5WSXKK8DAf7oeK8/kkbollee.F0T4KAy.QEgNAX.6wLQY1XHmSID/5VkeFiEaSA2b0"

# create database salted and hashed password database from 000-999
hashed_passwords = []

for x in range(0,1000):
  digit_password = ("%03d" % (x,))
  hash_and_salted = sha512_crypt.using(salt=saltToSearch, rounds=5000).hash(digit_password)
  hashed_passwords.append(hash_and_salted)

print("database size:",len(hashed_passwords))

# compare to find the correct digit
digit=""

for x in hashed_passwords:
  if(password == x):
    print("found it!: ")
    print(hashed_passwords.index(x))
    digit=hashed_passwords.index(x)

# proof
print("-----")
print("$6$penguins$eP.EvNiF2A.MmRVWNgGj5WSXKK8DAf7oeK8/kkbollee.F0T4KAy.QEgNAX.6wLQY1XHmSID/5VkeFiEaSA2b0", "original")
print(sha512_crypt.using(salt=saltToSearch, rounds=5000).hash(str(digit)), "replicate")
