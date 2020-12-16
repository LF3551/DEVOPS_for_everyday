
from itertools import permutations
import enchant
print (enchant.list_languages())
d = enchant.Dict("ru_RU")
op = set()

inp='юасрлт'
lettr = [x.lower() for x in inp]

for n in range (3, len(inp)):
    for y in list(permutations(lettr,n)):
        z = ''.join(y)
        if d.check(z):
            op.add(z)
            #print(len(op))
            word_2 = []
            word_3 = []
            word_4 = []
            word_5 = []
            word_6 = []
            word_7 = []
            word_8 = []
            for line in op:
                if len(line) == 2:
                    word_2.append(line)
                if len(line) == 3:
                    word_3.append(line)
                if len(line) == 4:
                    word_4.append(line)
                if len(line) == 5:
                    word_5.append(line)
                if len(line) == 6:
                    word_6.append(line)
                if len(line) == 7:
                    word_7.append(line)
                if len(line) == 8:
                    word_8.append(line)
print('words with 2 letters')
print(word_2)
print('words with 3 letters')
print(word_3)
print('words with 4 letters')
print(word_4)
print('words with 5 letters')
print(word_5)
print('words with 6 letters')
print(word_6)
print('words with 7 letters')
print(word_7)
print('words with 8 letters')
print(word_8)
