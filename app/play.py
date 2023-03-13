from paddlespeech.cli.asr.infer import ASRExecutor

asr = ASRExecutor()
result = asr(audio_file="./data/en.wav")
print(result)

result = asr(audio_file="./data/zh.wav")
print(result)
