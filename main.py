from flask import Flask, render_template, request, jsonify
import random
import json
import os

app = Flask(__name__, template_folder='templates')
app = Flask(__name__)

# Charger les questions depuis le fichier JSON
def load_questions():
    with open('data/questions.json', 'r', encoding='utf-8') as f:
        return json.load(f)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get_question')
def get_question():
    questions = load_questions()
    question = random.choice(questions)
    return jsonify(question)

@app.route('/check_answer', methods=['POST'])
def check_answer():
    data = request.json
    question_id = data['id']
    user_answer = data['answer']
    
    questions = load_questions()
    question = next((q for q in questions if q['id'] == question_id), None)
    
    if not question:
        return jsonify({"correct": False, "message": "Question non trouvée."})
    
    correct = str(user_answer) == str(question['reponse'])
    return jsonify({"correct": correct, "correct_answer": question['reponse']})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 10000))
    app.run(host='0.0.0.0', port=port)