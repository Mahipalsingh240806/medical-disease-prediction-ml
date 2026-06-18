from flask import Flask, render_template, request
import joblib

model = joblib.load("disease_model.pkl")

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("predict.html")


@app.route('/predict', methods=['GET','POST'])
def predict():

    prediction = None

    if request.method == "POST":

        Age = int(request.form['Age'])
        Gender = int(request.form['Gender'])
        BMI = float(request.form['BMI'])
        BloodPressure = float(request.form['BloodPressure'])
        GlucoseLevel = float(request.form['GlucoseLevel'])
        Cholesterol = float(request.form['Cholesterol'])
        HeartRate = float(request.form['HeartRate'])
        FamilyHistory = int(request.form['FamilyHistory'])
        Alcohol = int(request.form['Alcohol'])
        PhysicalActivity = int(request.form['PhysicalActivity'])
        Smoking = int(request.form['Smoking'])

        data = [[
            Age,
            Gender,
            BMI,
            BloodPressure,
            GlucoseLevel,
            Cholesterol,
            HeartRate,
            FamilyHistory,
            Alcohol,
            PhysicalActivity,
            Smoking
        ]]

        pred = model.predict(data)[0]

        disease_dict = {
            1: "Healthy",
            2: "Pre-Diabetes",
            3: "Hypertension",
            4: "Heart Disease",
            5: "Diabetes"
        }

        prediction = disease_dict.get(pred)

    return render_template(
        "predict.html",
        prediction=prediction
    )


if __name__ == "__main__":
    app.run(debug=True)