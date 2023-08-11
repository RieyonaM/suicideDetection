from flask import Flask, request, jsonify
from flask_cors import CORS
import base64
app = Flask(__name__)
CORS(app)

@app.route('/upload', methods=['POST'])
def upload_audio():
    print(request.form)
    try:
        txt = request.form['text']
        # audio_data = base64.b64decode(audio_data)
        text=text_translate(txt).text
        return jsonify({"text":text})
    except Exception as e:
        print("Error processing audio:", str(e))
        return jsonify({"text":str(e)})
    


from googletrans import Translator

def text_translate(txt):
    translator=Translator()
    trns_text=translator.translate(txt,dest="en")
    return trns_text



if __name__ == '__main__':
    app.run(debug=True)