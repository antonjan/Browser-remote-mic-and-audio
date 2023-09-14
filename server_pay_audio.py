from flask import Flask, request, render_template
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload_audio', methods=['POST'])
def upload_audio():
    audio_data = request.data
    with open('uploaded_audio.wav', 'wb') as audio_file:
        audio_file.write(audio_data)
    return "Audio uploaded successfully"

@app.route('/play_audio')
def play_audio():
    os.system('aplay uploaded_audio.wav')  # Use 'aplay' for Linux, change accordingly for other OS

if __name__ == '__main__':
    app.run(host="0.0.0.0",ssl_context='adhoc',debug=True)

