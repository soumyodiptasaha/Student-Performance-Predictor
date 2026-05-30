from flask import Flask, render_template, request
import joblib
import numpy as np

# Create Flask app
app = Flask(__name__)

# Load trained model
model = joblib.load("model.pkl")


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():

    studytime = float(request.form["studytime"])
    failures = float(request.form["failures"])
    absences = float(request.form["absences"])
    g1 = float(request.form["g1"])
    g2 = float(request.form["g2"])

    features = np.array([
        [studytime, failures, absences, g1, g2]
    ])

    prediction = model.predict(features)[0]

# Performance category + Grade
    if prediction >= 16:
        category = "Excellent 🌟"
        grade = "A"

    elif prediction >= 12:
        category = "Good 👍"
        grade = "B"

    elif prediction >= 8:
        category = "Average 📚"
        grade = "C"

    else:
        category = "Needs Improvement ⚠️"
        grade = "D"
# Student Status
    if prediction >= 16:
        status = "Outstanding Student 🏆"

    elif prediction >= 12:
        status = "Above Average Student ⭐"

    elif prediction >= 8:
        status = "Average Student 📚"

    else:
        status = "Needs Academic Support ⚠️"

    return render_template(
    "index.html",
    prediction=round(prediction, 2),
    category=category,
    grade=grade,
    status=status
)


import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)