import random
from playsound import playsound

#Song Database 
    # Format - "Song Title": r"Path\To\Song.mp3"
songs = {
    "50 Ways To Leave Your Lover": r"C:\Users\Lord Van\Documents\Guess the Song!\50 Ways To Leave Your Lover.mp3",
    "Billie Jean": r"C:\Users\Lord Van\Documents\Guess the Song!\Billie Jean.mp3",
    "Bones": r"C:\Users\Lord Van\Documents\Guess the Song!\Bones.mp3",
    "Cant Take My Eyes Off Of You": r"C:\Users\Lord Van\Documents\Guess the Song!\Cant Take My Eyes Off Of You.mp3",
    "Clint Eastwood": r"C:\Users\Lord Van\Documents\Guess the Song!\Clint Eastwood.mp3",
    "Crawl": r"C:\Users\Lord Van\Documents\Guess the Song!\Crawl.mp3",
    "Crazy": r"C:\Users\Lord Van\Documents\Guess the Song!\Crazy.mp3",
    "Creep": r"C:\Users\Lord Van\Documents\Guess the Song!\Creep.mp3",
    "Day N Nite": r"C:\Users\Lord Van\Documents\Guess the Song!\Day N Nite.mp3",
    "Everything I Own": r"C:\Users\Lord Van\Documents\Guess the Song!\Everything I Own.mp3",
    "Fireflies": r"C:\Users\Lord Van\Documents\Guess the Song!\Fireflies.mp3",
    "House Of The Rising Sun": r"C:\Users\Lord Van\Documents\Guess the Song!\House Of The Rising Sun.mp3",
    "I Think Were Alone Now": r"C:\Users\Lord Van\Documents\Guess the Song!\I Think Were Alone Now.mp3",
    "Ironic": r"C:\Users\Lord Van\Documents\Guess the Song!\Ironic.mp3",
    "Pumped Up Kicks": r"C:\Users\Lord Van\Documents\Guess the Song!\Pumped Up Kicks.mp3",
    "Rather Be": r"C:\Users\Lord Van\Documents\Guess the Song!\Rather Be.mp3",
    "Riptide": r"C:\Users\Lord Van\Documents\Guess the Song!\Riptide.mp3",
    "Royals": r"C:\Users\Lord Van\Documents\Guess the Song!\Royals.mp3",
    "September": r"C:\Users\Lord Van\Documents\Guess the Song!\September.mp3",
    "Should I Stay Or Should I Go": r"C:\Users\Lord Van\Documents\Guess the Song!\Should I Stay Or Shoul I Go.mp3",
    "Smells Like Teen Spirit": r"C:\Users\Lord Van\Documents\Guess the Song!\Smells Like Teen Spirit.mp3",
    "Stay With Me": r"C:\Users\Lord Van\Documents\Guess the Song!\Stay With Me.mp3",
    "Stay": r"C:\Users\Lord Van\Documents\Guess the Song!\Stay.mp3",
    "Under Pressure": r"C:\Users\Lord Van\Documents\Guess the Song!\Under Pressure.mp3",
    "Worlds Smallest Violin": r"C:\Users\Lord Van\Documents\Guess the Song!\Worlds Smallest Violin.mp3"
}

score = 0
played_songs = set()  # Tracks played songs

def play_song(song_path):
    playsound(song_path)

def ask_guess(correct_song_name):
    global score
    guess = input("Guess the song?: ")
    if guess.lower() == correct_song_name.lower():
        print("Correct!🎉")
        score += 1
    else:
        print(f"Wrong! The correct answer was: {correct_song_name}")

# Main game loop
if __name__ == "__main__":
    print("Welcome to the 'Guess the Song' Game!")
    print("It's 15s per song so try to guess what song is playing. Type your answer and hit Enter.")
    
    while True:
        # If all songs have been played, resets the played list and score
        if len(played_songs) == len(songs):
            print("Congratulations! All songs have been played! Resetting the list and your score.")
            played_songs.clear()
            score = 0  # Resets the score

        # Randomly selects a song that hasn't been played yet
        correct_song_name, song_path = random.choice(list(songs.items()))
        while correct_song_name in played_songs:
            correct_song_name, song_path = random.choice(list(songs.items()))

        # Plays the song
        play_song(song_path)
        played_songs.add(correct_song_name)  # Marks the song as played

        # Asks for a guess after the song ends
        ask_guess(correct_song_name)

        # Shows the current score
        print(f"Your current score is: {score}")

        # Asks if the player wants to play again
        play_again = input("Do you want to play again? (yes/no): ")
        if play_again.lower() != "yes":
            break

    print("Thanks for playing! Your final score is:", score)
