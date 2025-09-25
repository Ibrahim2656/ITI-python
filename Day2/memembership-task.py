import time

# set using hash table then go the bucket and get it 
# list (liner search) o(n)
# using low memory bc list point to it
# using alot of memory 

n = 1_000_000
my_list = list(range(n))
my_set = set(range(n))


target = n - 1 #worst case


start = time.time()
for _ in range(100):
    target in my_list
end = time.time()
print(f"List membership: {end - start:.6f} seconds")


start = time.time()
for _ in range(100):
    target in my_set
end = time.time()
print(f"Set membership: {end - start:.6f} seconds")
