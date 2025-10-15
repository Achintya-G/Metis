from utils.recorder import Recorder
from os import listdir,getcwd
from time import sleep

def record_new_word(word:str,duration:int,repetitions:int):
    r = Recorder(word)

    for i in range(repetitions):
        input("Hit a key to start recording.")
        sleep(0.2)
        
        r.record_audio(duration=duration,file_name=f"{word}{i}.wav")
        print(f"Progres ({i+1}/{repetitions})")

def record_background_audio(duration:int):
    r = Recorder('Background')

    files = [f for f in listdir(getcwd()+'/recordings/Background/')]
    i = 1 + len(files) # janky ahh solution but no one is ever gonna touch this :p

    r.record_audio(duration=duration,file_name=f"background{i}.wav")

def main():
    print("\n\nWhat type of data are you going to record?")
    print('''1. New word\n2. background audio\n''')
    choice = input("(1 / 2 / anything other key to exit):")
    match choice:
        case '1': 
            word = input("Enter the word : ")
            duration = int(input("Enter the duration (seconds) : "))
            repetitions = int(input("Number of times to record : "))
            record_new_word(word=word,duration=duration,repetitions=repetitions)
        case '2':
            duration = int(input("Enter the duration (seconds) : "))
            record_background_audio(duration=duration)
        case _:
            return 0
    return 1
    

    
    

if __name__ == "__main__":
    i = 1
    while i:
        i = main()
    print("Exiting program.")