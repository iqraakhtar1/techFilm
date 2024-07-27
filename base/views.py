from django.shortcuts import render
from .models import Audio
# Create your views here.
import os

def home(request):
    context = {}
    return render(request, 'base/home.html', context)

def text(request):
    try:
        os.remove("hello.mp3")
    except:
        pass
    text = request.POST.get('text')
    try:
        import gtts

        tts = gtts.gTTS(text)
        tts.save("hello.mp3")
        # if request.method == 'POST':
        #     Audio.objects.create(
        #         record = audio
        #     )
        
    except:
        pass


    print(text)
    context = {'text':text}
    return render(request, 'base/text.html', context)

def voice(request):
    context = {}
    return render(request, 'base/voice.html', context)

def login(request):
    context = {}
    return render(request, 'base/login.html', context)

