from flask import Flask, render_template, request, jsonify
import pandas as pd
import pickle
import json
import os

app = Flask(__name__)

# Load models and column info
def load_models():
    models = {}
    models['exercise'] = pickle.load(open('models/exercise_pipeline.pkl', 'rb'))
    models['equipment'] = pickle.load(open('models/equipment_pipeline.pkl', 'rb'))
    models['diet'] = pickle.load(open('models/diet_pipeline.pkl', 'rb'))
    
    with open('column_info.json', 'r') as f:
        column_info = json.load(f)
    
    return models, column_info

models, column_info = load_models()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/recommend', methods=['POST'])
def recommend():
    try:
        # Get form data
        form_data = request.form.to_dict()
        
        # Prepare input DataFrame
        input_data = {
            'Sex': [form_data['sex']],
            'Age': [int(form_data['age'])],
            'Hypertension': [form_data['hypertension']],
            'Diabetes': [form_data['diabetes']],
            'BMI': [float(form_data['bmi'])],
            'Fitness Goal': [form_data['fitness_goal']]
        }
        input_df = pd.DataFrame(input_data)
        
        # Get predictions
        exercises = models['exercise'].predict(input_df)[0]
        equipment = models['equipment'].predict(input_df)[0]
        diet = models['diet'].predict(input_df)[0]
        
        # Format results
        results = {
            'user_info': form_data,
            'recommendations': {
                'exercises': exercises.split(', '),
                'equipment': equipment.split(' and '),
                'diet': diet
            }
        }
        
        return render_template('results.html', results=results)
    
    except Exception as e:
        return render_template('index.html', error=str(e))

if __name__ == '__main__':
    app.run(debug=True)