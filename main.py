from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"message": "GenixAI Backend is live!"})

@app.route('/generate-video', methods=['POST'])
def generate_video():
    data = request.json
    prompt = data.get("prompt")
    voice_url = "https://voice.ai/dummy.mp3"
    bgm_url = "https://bgm.ai/music.mp3"
    video_url = "https://pexels.com/video.mp4"
    return jsonify({
        "video_url": video_url,
        "voice_url": voice_url,
        "bgm_url": bgm_url
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
