import random
import string



def get_random_string(length):
    
    result_str = ''.join(random.choice(string.ascii_letters + string.digits) for i in range(length))
    return result_str

f = open("uwu.txt", "a")
for i in range(10000):
    uwuu = get_random_string(8)
    f.write(uwuu + '\n')
    print(uwuu)
f.close()

