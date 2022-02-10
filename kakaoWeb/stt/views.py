from django.shortcuts import render, redirect
import requests
import json
import os
import wave
import speech_recognition as sr
from .models import Recommend_history
from django.http import Http404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import RecomSerializer
import sys
sys.path.append('..')
from kakaoWeb.settings import BASE_DIR
from pathlib import Path


# Create your views here.
kakao_speech_url = "https://kakaoi-newtone-openapi.kakao.com/v1/recognize"
kakao_tts_url = 'https://kakaoi-newtone-openapi.kakao.com/v1/synthesize'
rest_api_key = os.environ.get('SECRET_KEY')
KEYWORD_KAKAO = '카카오'
headers = {
    "Content-Type": "application/octet-stream",
    "X-DSS-Service": "DICTATION",
    "Authorization": "KakaoAK " +str(rest_api_key),}
tts_headers = {
    'Content-Type' : 'application/xml',
    'Authorization' : 'KakaoAK ' + rest_api_key,}


def mainpage(request):
    return render(request, 'mainpage.html')


def intro(request):
    return render(request, 'recordTest.html')


def gate(request):
    return render(request, 'gate.html')


def kakao_stt( style, data):
    # 음성인식중일때, 'Say something, Recording 등의 메세지 필요'
    if style == 'file':
        filename = data
        with open(filename, 'rb') as fp:
            audio = fp.read()
    else:
        audio = data
    # 카카오 음성 api 요청
    try:
        res = requests.post(kakao_speech_url, headers = headers, data = audio)
    except :
        return "OS Error"
    # 요청에 실패했다면
    if res.status_code != 200:
        text = ''
        print('error! because ', res.json())
    else:
        try:
            result_json_string = res.text[res.text.index('{"type":"finalResult"'):res.text.rindex('}') + 1]
            text = json.loads(result_json_string).get('value')
        except ValueError as e:
            return "Value Error"
    # text를 model에 저장하기
    history = Recommend_history()
    history.recommend = text
    history.save()
    return text


def chat(request):
    AUDIO_FILE = os.path.join(BASE_DIR, 'kakaoWeb','static','wav','heykakao.wav')
    SAVE_FILE = os.path.join(BASE_DIR, 'kakaoWeb','static','wav','hello_kakao.wav')
    text = kakao_stt('file', AUDIO_FILE)
    result = None
    if KEYWORD_KAKAO in text :
        result = '네 안녕하세요 카카오 음성인식입니다.'
        data = f"<speak><prosody rate='slow' volume = 'soft'>{result}</prosody></speak>".encode('utf-8').decode('latin1')
        res = requests.post(kakao_tts_url, headers=tts_headers, data=data)
        with open(SAVE_FILE,'wb') as f:
            f.write(res.content)
    return render(request, 'chat.html', {'text':text, 'result':result})


def chat_two(request):
    SAVE_FILE = os.path.join(BASE_DIR, 'kakaoWeb','static','wav','hi.wav')
    try:
        audio = get_speech()
        text = kakao_stt('stream', audio)
    except :
        text = "OS Error"
    # text  = kakao_stt('stream',audio)
    print('음성인식 결과:', text)
    if text == 'Value Error':
        return redirect('stt:error')
    elif text == 'OS Error':
        return redirect('stt:error_two')
    result = None
    if KEYWORD_KAKAO in text :
        result = '네 안녕하세요 카카오 음성인식입니다.'
        data = f"<speak><prosody rate='slow' volume = 'soft'>{result}</prosody></speak>".encode('utf-8').decode('latin1')
        res = requests.post(kakao_tts_url, headers=tts_headers, data=data)
        with open(SAVE_FILE,'wb') as f:
            f.write(res.content)
    return render(request, 'chat.html', {'text':text, 'result':result})

# 마이크로 음성 수집하기
# 함수 정의부
def get_speech():
    #마이크에서 음성 추출하는 객체
    recognizer = sr.Recognizer()
    #마이크 설정
    microphone = sr.Microphone(sample_rate = 16000)
    qA
    #마이크 소음 수치 반영
    with microphone as source :
        recognizer.adjust_for_ambient_noise(source)
        print("소음 수치 반영하여 음성을 청취합니다. {}".format(recognizer.energy_threshold))
    #음성 수집
    with microphone as source :
        print("Say something")
        result = recognizer.listen(source)
        audio = result.get_raw_data()
    return audio


def error(request):
    return render(request, 'error.html')


def error_two(request):
    return render(request, 'error_two.html')
