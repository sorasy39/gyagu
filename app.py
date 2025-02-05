from flask import Flask, render_template, jsonify
import requests

app = Flask(__name__)

# DeepL APIキー
API_KEY = 'e8dfad96-87f8-42a7-a13d-aae04d3997a2:fx'

# DeepLで翻訳する関数
def translate_text(text, target_language='JA'):
    url = "https://api-free.deepl.com/v2/translate"
    params = {
        'auth_key': API_KEY,
        'text': text,
        'target_lang': target_language
    }
    
    response = requests.post(url, data=params)
    result = response.json()
    return result['translations'][0]['text']

# ランダムジョークを取得する関数
def get_joke():
    response = requests.get("https://official-joke-api.appspot.com/jokes/random")
    
    # レスポンスが成功したか確認
    if response.status_code == 200:
        joke = response.json()  # JSON形式で返ってくる
        print(joke)  # レスポンスを表示して確認する
        
        if joke:  # ジョークが存在するか確認
            # 原文の英語ジョーク
            setup_en = joke['setup']
            punchline_en = joke['punchline']
            
            # 英語のジョークを日本語に翻訳
            setup_ja = translate_text(setup_en)
            punchline_ja = translate_text(punchline_en)
            
            return {
                'setup_en': setup_en, 'punchline_en': punchline_en,
                'setup_ja': setup_ja, 'punchline_ja': punchline_ja
            }
        else:
            return {"setup_en": "ジョークが見つかりませんでした。", "punchline_en": "", "setup_ja": "", "punchline_ja": ""}
    else:
        return {"setup_en": "ジョークを取得できませんでした。", "punchline_en": "", "setup_ja": "", "punchline_ja": ""}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_joke')
def get_joke_route():
    joke = get_joke()
    return jsonify(joke)  # JSONで返す

if __name__ == '__main__':
    app.run(debug=True)



#http://127.0.0.1:5000/