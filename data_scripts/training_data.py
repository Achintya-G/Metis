from utils.recorder import Recorder

def record_new_word(word:str,duration:int,repetitions:int):
    r = Recorder(word)
    for i in range(repetitions):
        r.record_audio(duration=duration,file_name=f"{word}{i}.wav")

def record_background_audio(duration:int,):
    pass

def main():
    print("What type of data are you going to record?")
    print('''
          1. New word\n
          2. background audio\n
          ''')
    choice = int(input("(1 / 2 / anything other key to exit):"))
    print(choice)
    match choice:
        case 1:
            word = input("Enter the word : ")
            duration = int(input("Enter the duration (seconds) : "))
            repetitions = int(input("Number of times to record : "))
            record_new_word(word=word,duration=duration,repetitions=repetitions)
        case 2:
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