
current_movies = {'The Awakening':'11:00am',
                  'Harry Potter':'2:40pm',
                  'The Shining':'4:00pm',
                  'Ferris Buehler': '6:30pm'}

print("We're showing the following movies:")
for key in current_movies:
    print(key)
movies = input("What movie would you like the showtime for?\n")

showtime = current_movies.get(movies)
if showtime == None:
    print("The requested movie isn't playing")
else:
    print(movies, 'is playing at', showtime)    
