import time
import sys

# Fancy Birthday Song Generator using a FOR loop
# I chose a for loop because the song has a fixed structure
# and repeats a known number of times.

name = input("🎤 Enter the birthday person's name: ")

def sing_line(line):
    """Prints a line letter by letter like song lyrics"""
    for char in line:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.05)
    print()
    time.sleep(0.4)

print("\n🎶 Music starts playing... 🎶\n")
time.sleep(1)

# First part repeats
for _ in range(2):
    sing_line("🎵 Happy birthday to youuu~ 🎵")
    sing_line("🎵 Happy birthday to youuu~ 🎵")

# Name line
sing_line(f"🎂 Happy birthday dear {name}! 🎂")

# Ending
sing_line("🎉 Happy birthday to yooooouuu! 🎉")
sing_line("✨ May your days be bright and full of cheer ✨")
sing_line("🎁 Smiles, cake, and wishes all year! 🎁")

print("\n🎊 🎈 🎂 THE SONG IS OVER — CELEBRATE! 🎂 🎈 🎊")

#One bug I ran into was that the song lyrics were printing all at once instead of appearing letter by letter like real song lyrics.
# I fixed this by printing each character one at a time using a for loop and adding a small delay with the time module so the text appears gradually in the terminal


#I learned that for loop is better than a while loop when you know in advance how many times the loop should run.
#It is useful for repeating a task a fixed number of times, such as counting, printing patterns, or repeating lines in a song.

