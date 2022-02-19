from email.mime import audio
from django.shortcuts import render
from django.http import HttpResponse
import pyttsx3
from playsound import playsound
import ffmpeg
import subprocess


#function for home page
def index(request):
    return render(request,'index.html')

#function for Getting audio from text and redirecting user to the next page
def Audio(request):
    text=request.GET['text']
    engine=pyttsx3.init()
    voice_type=request.GET['Voice']
    print(voice_type)
    if (voice_type=="Female"):
        engine.setProperty('voice','english_rp+f3')
    engine.setProperty('rate', 100)
    engine.save_to_file(text, 'test.mp3')
    engine.runAndWait()
    return render(request,'Audio.html')

def content(request):
    #getting video and audio as input from user
    video=request.GET['video']
    audio=request.GET['audio']
    
    #processing inputted audio and video
    new_audio=ffmpeg.input(audio)
    new_video=ffmpeg.input(video)

    #merging the the new audio and video and compressing it
    ffmpeg.concat(new_video, new_audio, v=1, a=1).output('final.mp4').run()
    return render(request,'Audio.html')


