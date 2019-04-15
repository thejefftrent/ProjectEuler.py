with open('ProjectEuler.py/p042_words.txt','r') as file:
    words = file.read()
words = words.replace('"','').split(',')

triangle = [1]
for i in range(2,100):
    triangle.append((triangle[len(triangle)-1]) + i)
count = 0
for word in words:
    s = 0
    for letter in word:
        s += (ord(letter) - 64)
    for tri in triangle:
        if tri == s:
            count += 1
            print(tri, word)
print(count)
