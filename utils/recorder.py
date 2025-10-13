import pyaudio
import wave
import os

class Recorder:

    def __init__(self, save_folder=None):
        self.SAVE_FOLDER = "./recordings/"+save_folder+"/" if save_folder != None else "./recordings/"
        self.chunk = 1024
        self.FORMAT = pyaudio.paInt16
        self.channels = 1
        self.sample_rate = 8000

        if not (os.path.isdir(self.SAVE_FOLDER)):
            os.mkdir(self.SAVE_FOLDER)


    def record_audio(self,duration:int,file_name:str,input_device_id:int=None):

        # initialising pyaudio object
        p = pyaudio.PyAudio()
        print("Recording Audio....")
        
        # setting deafult audio device as input if none given 
        if input_device_id == None:
            input_device_id = p.get_default_input_device_info().get("index")

        # initialising audio stream from given input device
        s = p.open(
            rate= self.sample_rate,
            format=self.FORMAT,
            input_device_index=input_device_id,
            input=True,
            output=True,
            frames_per_buffer=self.chunk,
            channels= self.channels)
        
        frames = []

        # reading chunks for required duration.
        for i in range(int(self.sample_rate/self.chunk) * duration):
            data = s.read(self.chunk)
            frames.append(data)
        
        # stopping audio stream
        s.stop_stream()
        s.close()

        # saving the recorded data as .wav file
        wf = wave.open(self.SAVE_FOLDER+file_name,"wb")
        wf.setnchannels(self.channels)
        wf.setsampwidth(p.get_sample_size(self.FORMAT))
        wf.setframerate(self.sample_rate)
        wf.writeframes(b"".join(frames))
        wf.close()

        print("Done recording.")

        # stopping pyaudio object
        p.terminate()


    def check_input_device(self):
        p  = pyaudio.PyAudio()

        current_audio_device = p.get_default_input_device_info()
        print(f"Current audio device:\n  ID: {current_audio_device.get('index')}, Name: {current_audio_device.get('name')}\n\n")
        
        for i in range(p.get_device_count()):
            device_info = p.get_device_info_by_index(i)
            if device_info.get('maxInputChannels') > 0:
                print(f"  ID: {i}, Name: {device_info.get('name')}")

        p.terminate()


def main():
    filename = "trial.wav"
    duration = 5
    
    rec = Recorder()

    rec.record_audio(
        duration=duration,
        file_name=filename,
    )


if __name__ == "__main__":
    main()
