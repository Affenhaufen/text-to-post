# Some Cool Readme

some cool text

# Vosk example

run the following to transcribe the numbers.wav file:

```bash
vosk-transcriber -i audio_tests/numbers/numbers.wav -o audio_tests/numbers/numbers.txt
```

run docker server locally which takes .wav file:

```bash
docker run -d -p 2700:2700 alphacep/kaldi-de:latest
```

```bash
python3 test.py audio_tests/numbers/numbers.wav
```