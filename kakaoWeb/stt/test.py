import requests
import json
#
# # 함수 정의부
def kakao_stt(app_key, stype, data):
    if stype == 'file':
        filename = data
        # rb = read byte
        with open(filename, 'rb') as fp:
            audio = fp.read()
    else:
        audio = data

    headers = {
        "Content-Type" : "application/octet_stream",
        "Authorization" : "KakaoAK " + app_key,
    }
    # 카카오 음성 url
    kakao_speech_url = "https://kakaoi-newtone-openapi.kakao.com/v1/recognize"
    # 카카오 음성 api 요청
    res = requests.post(kakao_speech_url, headers=headers, data=audio)
    #요청에 실패했다면
    if res.status_code != 200:
        text = ""
        print("error! because ", res.json())
    else:
        # print("음성인식 결과 : ", res.text)
        # print("시작위치 : ", res.text.index('{"type":"finalResult"'))
        # print("종료위치 : ", res.text.rindex('}')+1)
        # print("추출한 정보 : ", res.text[res.text.index('{"type":"finalResult"'):res.text.rindex('}')+1])
        result = res.text[res.text.index('{"type":"finalResult"'):res.text.rindex('}') + 1]
        text = json.loads(result).get('value')
    return text
#
# # #함수 호출부
KAKAO_APP_KEY = "40a58b9f558b7a2c831b0ad415237028"
# # AUDIO_FILE = 'res/jarvis/hello.wav'
# # text = kakao_stt(KAKAO_APP_KEY, 'file', AUDIO_FILE)
# # print(text)
#
#
# #마이크로 음성 수집하기
import speech_recognition as sr
#
# #함수 정의부
def get_speech():
    #마이크에서 음성을 추출하는 객체
    recognizer = sr.Recognizer()
    #마이크 설정
    microphone = sr.Microphone(sample_rate=16000)

    #마이크 소음 수치 반영
    with microphone as source :
        recognizer.adjust_for_ambient_noise(source)
        print('소음 수치 반영하여 음성을 청취합니다. {}'.format(recognizer.energy_threshold))

    # 음성 수집
    with microphone as source:
        print('Say something!')
        result = recognizer.listen(source)
        audio = result.get_raw_data()

    return audio
#

# # 함수 호출부
audio = get_speech()
text = kakao_stt(KAKAO_APP_KEY, 'stream', audio)
print('음성인식 결과:'+text)
#
# # 필요한 기능은 구현하고 def do()로 선언하기
# # import javis_food_recommender
# # javis_food_recommender.do()하면 바로 카톡 메세지가 보내질 수 있도록 하듯이..
#
# # .py를 수정하면 모듈을 reload 해주어야한다.
# # 예시는 아래와 같음.
# # from imp import reload
# # reload(javis_food_recommender)
# # import javis_food_recommender
# # javis_food_recommender.do()
#
#
#
# ## 음성인식 비서 실행하기
KEYWORD_STOCK = '주식'
KEYWORD_WEATHER = '날씨'
KEYWORD_KAKAO = '카카오'
#
# # 음성수집
# audio = get_speech()
#
# # STT
# command = kakao_stt(KAKAO_APP_KEY, 'stream', audio)
# print('명령어 : ' + command)
# print('명령을 수행합니다.')
#
# # 음성 분석
# if KEYWORD_KAKAO in command:
#     print('카카오를 실행합니다')
# else:
#     print('명령을 알 수 없습니다.')
#
#
# # 카카오 음성 tts
#
import os, wave
#
# url = 'https://kakaoi-newtone-openapi.kakao.com/v1/synthesize'
# key = '40a58b9f558b7a2c831b0ad415237028'
# headers = {
#     'Content-Type' : 'application/xml',
#     'Authorization' : 'KakaoAK ' + key,
# }
#
# #텍스트
# text = '안녕하세요, 제 이름은 카카오 음성 합성 API 입니다. 만나서 반가워요'
#
# # 입력한 텍스트를 변환하여 api를 호출
# data = f"<speak>{text}</speak>".encode('utf-8').decode('latin1')
# res = requests.post(url, headers=headers, data=data)
# #호출하며 불러온 결과값을 저장
# with open('hellow_kakao.wav','wb') as f:
#     f.write(res.content)

from IPython.display import Audio, display
import wave
# import pyaudio
#
#
# chunk = 1024
# path = 'hellwo_kakao.wav'
# with wave.open(path, 'rb') as f:
#     py = pyaudio.PyAudio()
#
#
# wn = Audio('hellow_kakao.wav', autoplay=True)
# display(wn)