animations = {
    "Pokemon": "Pikachu",
    "Digimon": "Agumon",
    "Yugioh": "Black Magician"
}

word = input()

if word in animations:
    print(animations[word])
else:
    print("I don't know")

print(animations.get(word, "I don't know"))