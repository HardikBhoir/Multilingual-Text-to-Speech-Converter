from flask import Flask, render_template, request, url_for
import boto3
import os
from tempfile import gettempdir
from contextlib import closing
import shutil

app = Flask(__name__)

# AWS Polly client setup
session = boto3.session.Session(profile_name='AWS_Profilename')
client = session.client(service_name='polly', region_name='us-east-1')

@app.route('/')
def index():
    return render_template('index.html')  # Render the main HTML page

@app.route('/synthesize', methods=['POST'])
def synthesize():
    text = request.form['text']  # Get the entered text
    response = client.synthesize_speech(VoiceId='Joanna', OutputFormat='mp3', Text=text, Engine='neural')
    
    if "AudioStream" in response:
        output_path = os.path.join(gettempdir(), "speech.mp3")
        with closing(response['AudioStream']) as stream:
            with open(output_path, "wb") as file:
                file.write(stream.read())
        
        # Move the file to the static folder so it can be accessed by the browser
        static_audio_path = os.path.join('static', 'speech.mp3')
        shutil.copyfile(output_path, static_audio_path)
        
        # Serve the audio file in the webpage
        audio_url = url_for('static', filename='speech.mp3')
        return render_template('index.html', audio_url=audio_url, text=text)  # Pass the text back to the template
    else:
        return "Could not synthesize speech", 500

if __name__ == '__main__':
    app.run(debug=True)
