import os

import spacy
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

model_directory = os.path.dirname(os.path.realpath(__file__)) + "/model"

nlp = spacy.load(model_directory)


@app.route('/getNormalizedClassLabel', methods=["POST"])
def getNormalizedName():
    labeled = nlp(request.get_json().get("originalName"))
    return jsonify(makeDictionaryFromLabels(labeled))


def makeDictionaryFromLabels(labeled):
    result = {}
    for ent in labeled.ents:
        result[str(ent.label_).lower()] = ent.text
    return result


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
