import logging

from flask import Flask, render_template, request
import pandas as pd

import predictor


app = Flask(__name__)

def read_data(request_file):
    # This function does not work
    return pd.read_csv(request_file)

@app.route("/predict", methods=["GET", "POST"])
def predict():

    if request.method == "POST":
        # Make predictions
        if 'file' not in request.files:
            app.logger.info("No file")
            return "No file loaded"
        
        request_file = request.files.get('file')

        if request_file.filename == "":
            return "No file selected -- ERROR"

        #data = read_data(request_file=request_file)
        data = [[1.5, 4.3, 0.6, 1.2]]
        result = predictor.predict(data=data)
        return result

    return render_template("upload_data.html")

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000, threaded=True, use_reloader=False)


