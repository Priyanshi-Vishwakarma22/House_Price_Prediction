from flask import Flask, request, render_template

from src.pipeline.predict_pipeline import PredictPipeline, CustomData
import webbrowser
from threading import Timer
import os

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():

    try:

        # Get Form Data
        area = float(request.form.get("area"))
        bedrooms = int(request.form.get("bedrooms"))
        bathrooms = int(request.form.get("bathrooms"))
        stories = int(request.form.get("stories"))
        parking = int(request.form.get("parking"))

        mainroad = request.form.get("mainroad")
        guestroom = request.form.get("guestroom")
        basement = request.form.get("basement")
        hotwaterheating = request.form.get("hotwaterheating")
        airconditioning = request.form.get("airconditioning")
        prefarea = request.form.get("prefarea")
        furnishingstatus = request.form.get("furnishingstatus")


        # ===============================
        # Backend Validation
        # ===============================

        if bedrooms < 1 or bedrooms > 6:
            return render_template(
                "index.html",
                prediction_text="❌ Bedrooms must be between 1 and 6."
            )

        if bathrooms < 1 or bathrooms > 4:
            return render_template(
                "index.html",
                prediction_text="❌ Bathrooms must be between 1 and 4."
            )

        if stories < 1 or stories > 4:
            return render_template(
                "index.html",
                prediction_text="❌ Stories must be between 1 and 4."
            )

        if parking < 0 or parking > 3:
            return render_template(
                "index.html",
                prediction_text="❌ Parking must be between 0 and 3."
            )


        # Create CustomData Object
        data = CustomData(

            area=area,
            bedrooms=bedrooms,
            bathrooms=bathrooms,
            stories=stories,

            mainroad=mainroad,
            guestroom=guestroom,
            basement=basement,
            hotwaterheating=hotwaterheating,
            airconditioning=airconditioning,

            parking=parking,

            prefarea=prefarea,

            furnishingstatus=furnishingstatus

        )


        pred_df = data.get_data_as_data_frame()

        predict_pipeline = PredictPipeline()

        prediction = predict_pipeline.predict(pred_df)

        prediction_text = "₹ {:,.0f}".format(prediction[0])

        return render_template(
            "index.html",
            prediction_text=prediction_text
        )


    except Exception as e:

        return render_template(
            "index.html",
            prediction_text=f"Error: {str(e)}"
        )


if __name__ == "__main__":

    port = int(os.environ.get("PORT", 5000))

    # Sirf local machine par browser open karo
    if port == 5000:
        Timer(1.5, lambda: webbrowser.open(f"http://127.0.0.1:{port}")).start()

    app.run(
        host="0.0.0.0",
        port=port,
        debug=True,
        use_reloader=False
    )