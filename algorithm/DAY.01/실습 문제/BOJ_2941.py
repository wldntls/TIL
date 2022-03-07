croatia_alphabet = input()

croatia =['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']


for i in croatia:
    if i in croatia_alphabet:
        croatia_alphabet = croatia_alphabet.replace(i, '.')
print(len(croatia_alphabet))


# 크로아티아 알파벳 갯수 세기 (한개로 처리하여)

# 그냥 알파벳 세기
