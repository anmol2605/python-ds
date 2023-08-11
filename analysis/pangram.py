str = input('Enter a string: ')
alphabet = 'abcdefghijklmnopqrstuvwxyz'
flag = True
for char in alphabet:
    if char not in str:
        flag = False
if (flag ==True):
    print("pangram")
else:
    print("0")
