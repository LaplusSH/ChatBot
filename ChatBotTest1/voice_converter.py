from TTS.api import TTS

def convert_voice(input_file, output_file):
    # TTS 모델 초기화
    tts = TTS("tts_models/multilingual/multi-dataset/your_tts")
    
    # 음성 변환 실행
    tts.tts_to_file(
        text="", 
        file_path=output_file,
        speaker_wav=input_file,
        language="ko"
    )

# 사용 예시
input_audio = "input.wav"  # 원본 음성 파일
output_audio = "output.wav"  # 변환된 음성이 저장될 파일
convert_voice(input_audio, output_audio) 