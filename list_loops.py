songs = ["ROCKSTAR", "Do It", "For the Night"]
print(songs[1:3])

songs[0] = "Sunflower"
print(songs)

songs.extend(["One of Us", "Loud Pipes"])
songs.insert(1, "Run")
print(songs)

songs.remove("For the Night")
print(songs)

for song in songs:
    print(song)
print()
for i in range(len(songs)):
    print(songs[i])
print()

animals = ["Cat", "Snake", "Ferret"]
animals.append("Owl")
print(animals[2])
del animals[0]
for animal in animals:
    print(animal)