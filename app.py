from flask import Flask, render_template, request, redirect, send_from_directory, url_for
from werkzeug.utils import secure_filename
# from src.utils import *
import requests
import os
from azure.cognitiveservices.vision.customvision.prediction import CustomVisionPredictionClient
from msrest.authentication import ApiKeyCredentials

from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient

key_vault_name = "triof-vault"
key_vault_uri = f"https://{key_vault_name}.vault.azure.net/"
# The name of the secret you added in the Key Vault
secret_key = "customvision-key-caro"
secret_url = "customvision-uri-caro"
secret_id = "custom-vision-project-id-caro"

credential = DefaultAzureCredential(
    managed_identity_client_id="bd9d102a-6b4a-4f69-aa2b-71b2947fa1d0"
)
secret_client = SecretClient(vault_url=key_vault_uri, credential=credential)

prediction_key = secret_client.get_secret(secret_key).value
prediction_url = secret_client.get_secret(secret_url).value
project_id = secret_client.get_secret(secret_id).value

prediction_credentials = ApiKeyCredentials(
    in_headers={"Prediction-key": prediction_key})
predictor = CustomVisionPredictionClient(
    prediction_url, prediction_credentials)


publish_iteration_name = "Iteration1"

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/uploads/'


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/start', methods=['GET', 'POST'])
def insert():
    # open_waste_slot()
    if request.method == 'POST':
        if 'file' not in request.files:
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            return redirect(request.url)
        if file:
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)
            return render_template('insert.html', filename=filename)
    else:
        return render_template('insert.html')


@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)


@app.route('/waste/pick-type', methods=['POST', 'GET'])
def pick_type():
    filename = request.form.get('filename')
    filename = f"static/uploads/{filename}"
    url = prediction_url
    headers = {
        'Content-Type': 'application/octet-stream',
        'Prediction-Key': prediction_key
    }
    # print(url)
    # print(prediction_url)
    # print(prediction_key)

    with open(filename, 'rb') as image_data:
        result = predictor.classify_image(
            project_id, publish_iteration_name,
            image_data.read())
        print(result)

    # with open(filename, 'rb') as image_data:
    #     response = requests.post(url, headers=headers, data=image_data)
    #     result = response.json()
    # print(filename)
    # print(json.dumps(result, indent=4))
    prediction = result.predictions[0].tag_name
    # print(prediction)

    return render_template('type.html', prediction=prediction)


@app.route('/confirmation', methods=['POST'])
def confirmation():
    prediction = request.form.get('prediction')
    print(prediction)
    # waste_type = request.form['type']
    # process_waste(waste_type)
    return render_template('confirmation.html', prediction=prediction)


if __name__ == "__main__":
    app.run(debug=True)
