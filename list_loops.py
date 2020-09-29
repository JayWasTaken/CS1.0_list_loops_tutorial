#Q1 task make list
songs = ["ROCKSTAR", "Do It", "For the Night"]

#Q2 task print first and last, then print songs 2 and 3
print(songs[0])
print(songs[2])

print(songs[1:3])

#Q3 task replace(update) song
songs[0] = "Sunflower"
print(songs)

#Q4 task add 3 songs, delete 1
songs.extend(["One of Us", "Loud Pipes"])
songs.insert(1, "Run")
print(songs)

songs.remove("For the Night")
print(songs)

#Q5 task compare loops
for song in songs:
    print(song)

for i in range(len(songs)):
    print(songs[i])

#Q6 task make list and do stuff with it, more info in README
animals = ["Cat", "Snake", "Ferret"]
animals.append("Owl")
print(animals[2])
del animals[0]
for animal in animals:
    print(animal)