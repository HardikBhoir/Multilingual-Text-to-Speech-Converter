# Multilingual Text-to-Speech Converter

## Project Description
This is a web-based Text-to-Speech (T2S) application that converts text input into natural-sounding speech in five languages: English, Spanish, French, German, and Italian. Using AWS Polly for voice synthesis and hosted on an AWS EC2 instance, this application is built with Python's Flask framework and integrated with the Boto3 SDK for interaction with AWS services.

## Features
- **Multilingual Support**: Converts text to speech in English, Spanish, French, German, and Italian.
- **Natural Voices**: Uses AWS Polly’s neural voices for high-quality, lifelike speech.
- **User-Friendly Interface**: Web-based, easy-to-use interface with real-time audio playback.
- **Scalable**: Hosted on AWS EC2, ensuring performance across diverse devices.

## Tech Stack
- **Backend**: Python, Flask, Boto3 SDK
- **Frontend**: HTML, CSS, JavaScript
- **Cloud Services**: AWS Polly for text-to-speech, AWS EC2 for hosting

## Prerequisites
- Python 3.6+
- AWS Account with Polly and EC2 access
- AWS CLI and Boto3 SDK installed

## Setup Instructions

1. **Clone this repository**:
   git clone https://github.com/your-username/your-repo-name.git
   cd your-repo-name

2. **Install dependencies**:
    pip install -r requirements.txt

3. **Configure AWS CLI (if not already configured)**:
    aws configure
    - boto3 and AWS profile setup should be done before running this
    - Also your AWS profile name must need to change in 'app.py' and 'poly.py' files.

4. **Run the Flask app**:
    python app.py



## Deployment on AWS EC2

- Launch an EC2 Instance: Start an Ubuntu EC2 instance and install necessary dependencies (Python, Flask, Boto3).
- Deploy the Code: Upload or clone this repository on the EC2 instance.
- Run the Flask App: Start the app with python app.py.
- Access the App: Visit the public IP address of your EC2 instance in a browser.