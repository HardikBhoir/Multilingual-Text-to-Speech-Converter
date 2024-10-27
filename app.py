from flask import Flask, render_template, request, url_for
import boto3
import os
from tempfile import gettempdir
from contextlib import closing
import time
import shutil
from googletrans import Translator

app = Flask(__name__)

# AWS Polly client setup
session = boto3.session.Session(profile_name='AWS_Profilename')
polly_client = session.client(service_name='polly', region_name='us-east-1')

# Supported voices and their engines
voice_settings = {
    'en': {'VoiceId': 'Joanna', 'Engine': 'neural'},
    'es': {'VoiceId': 'Lucia', 'Engine': 'neural'},
    'fr': {'VoiceId': 'Celine', 'Engine': 'standard'},  # French doesn't support 'neural' for 'Celine'
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/synthesize', methods=['POST'])
def synthesize():
    text = request.form['text']
    target_language = request.form['language']

    # Translate text using googletrans
    translator = Translator()
    translated_text = translator.translate(text, dest=target_language).text

    # Get voice settings for the selected language
    if target_language in voice_settings:
        voice_id = voice_settings[target_language]['VoiceId']
        engine = voice_settings[target_language]['Engine']
    else:
        voice_id = 'Joanna'  # Fallback to English if language not supported
        engine = 'neural'

    # Synthesize speech
    response = polly_client.synthesize_speech(
        VoiceId=voice_id,
        OutputFormat='mp3',
        Text=translated_text,
        Engine=engine
    )

    if "AudioStream" in response:
        timestamp = int(time.time())
        output = os.path.join(gettempdir(), f"speech_{timestamp}.mp3")
        with closing(response['AudioStream']) as stream:
            with open(output, "wb") as file:
                file.write(stream.read())

        # Serve the audio file within the website
        audio_url = url_for('static', filename=f"speech_{timestamp}.mp3")

        # Copy the generated file to the static folder
        static_path = os.path.join('static', f"speech_{timestamp}.mp3")
        shutil.copy(output, static_path)

        return render_template('index.html', audio_url=audio_url)
    else:
        return "Could not synthesize speech", 500

if __name__ == '__main__':
    app.run(debug=True)

