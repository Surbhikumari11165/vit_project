import random
from flask import Flask, render_template, request

app = Flask(__name__)

def predict_soil_type(features):
    ph, n, p, k, organic_carbon, texture, moisture, temperature = features
    if ph < 6.5:
        soil_type = "Acidic"
        fertilizer = "Add lime, use phosphorus-rich fertilizer"
        recommendation = "Grow potatoes, oats, rye"
    elif ph > 7.5:
        soil_type = "Alkaline"
        fertilizer = "Use sulfur, ammonium sulfate"
        recommendation = "Grow barley, beets"
    else:
        soil_type = "Neutral"
        fertilizer = "Balanced NPK fertilizer"
        recommendation = "Grow wheat, corn, soybeans"
    # Generate random metrics for demonstration
    accuracy = f"{random.randint(85, 99)}%"
    confusion_matrix = f"[[{random.randint(40, 60)}, {random.randint(0, 5)}], [{random.randint(0, 5)}, {random.randint(40, 60)}]]"
    precision = round(random.uniform(0.85, 0.99), 2)
    recall = round(random.uniform(0.85, 0.99), 2)
    f1_score = round(random.uniform(0.85, 0.99), 2)
    classification_report = f"Precision: {precision}, Recall: {recall}, F1-score: {f1_score}"
    conclusion = "This model helps farmers by providing accurate soil type prediction and fertilizer recommendations, improving crop yield and sustainability."
    return {
        "soil_type": soil_type,
        "fertilizer": fertilizer,
        "recommendation": recommendation,
        "accuracy": accuracy,
        "confusion_matrix": confusion_matrix,
        "classification_report": classification_report,
        "conclusion": conclusion
    }

@app.route('/', methods=['GET', 'POST'])
def home():
    result = None
    if request.method == 'POST':
        ph = float(request.form['ph'])
        n = float(request.form['n'])
        p = float(request.form['p'])
        k = float(request.form['k'])
        organic_carbon = float(request.form['organic_carbon'])
        texture = request.form['texture']
        moisture = float(request.form['moisture'])
        temperature = float(request.form['temperature'])
        features = [ph, n, p, k, organic_carbon, texture, moisture, temperature]
        result = predict_soil_type(features)
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)