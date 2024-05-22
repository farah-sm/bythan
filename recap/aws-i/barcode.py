barcode = "004LUJKTGVKHGVJ|003JHGJVKJHVYHB|002HGVKJHVHFCK|001LKYGLJHVJHB"

# Result output should be 
# 001LKYGLJHVJHB
# 002HGVKJHVHFCK
# 003JHGJVKJHVYHB
# 004LUJKTGVKHJHGVJ

v = list(barcode.split("|"))
v.sort()
for a in v:
    print(a)
