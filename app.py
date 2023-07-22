from googletrans import Translator
from flask import Flask, request
from collections.abc import Iterable

translator = Translator()

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello, World!'


@app.route('/api', methods=['POST'])
def api():
    try:
        data = request.json
        translations = None
        if data['src']:
            translations = translator.translate(data['data'], src=data['src'],
                                                dest=data['dest'])
        else:
            translations = translator.translate(data['data'], dest=data['dest'])
        if not isinstance(translations, Iterable):
            return translations.text
        results = list()
        for translation in list(translations):
            results.append(translation.text)
    except:
        print("translate expection")
        return []

    return results


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
