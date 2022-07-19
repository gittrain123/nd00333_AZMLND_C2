import urllib.request
import json
import os
import ssl

def allowSelfSignedHttps(allowed):
    # bypass the server certificate verification on client side
    if allowed and not os.environ.get('PYTHONHTTPSVERIFY', '') and getattr(ssl, '_create_unverified_context', None):
        ssl._create_default_https_context = ssl._create_unverified_context

allowSelfSignedHttps(True) # this line is needed if you use self-signed certificate in your scoring service.

# Request data goes here
# The example below assumes JSON formatting which may be updated
# depending on the format your endpoint expects.
# More information can be found here:
# https://docs.microsoft.com/azure/machine-learning/how-to-deploy-advanced-entry-script
data =  {
  "Inputs": {
    "data": [
      {
        "age": 17,
        "job": "blue-collar",
        "marital": "married",
        "education": "university.degree",
        "default": "no",
        "housing": "yes",
        "loan": "yes",
        "contact": "cellular",
        "month": "may",
        "day_of_week": "mon",
        "duration": 971,
        "campaign": 1,
        "pdays": 999,
        "previous": 1,
        "poutcome": "failure",
        "emp.var.rate": -1.8,
        "cons.price.idx": 92.893,
        "cons.conf.idx": -46.2,
        "euribor3m": 1.299,
        "nr.employed": 5099.1
      },
      {
        "age": 87,
        "job": "blue-collar",
        "marital": "married",
        "education": "university.degree",
        "default": "no",
        "housing": "yes",
        "loan": "yes",
        "contact": "cellular",
        "month": "may",
        "day_of_week": "mon",
        "duration": 471,
        "campaign": 1,
        "pdays": 999,
        "previous": 1,
        "poutcome": "failure",
        "emp.var.rate": -1.8,
        "cons.price.idx": 92.893,
        "cons.conf.idx": -46.2,
        "euribor3m": 1.299,
        "nr.employed": 5099.1
      }
    ]
  },
  "GlobalParameters": {
    "method": "predict"
  }
}

body = str.encode(json.dumps(data))

url = 'http://41581ce1-4c68-42f2-aa77-5cf2998772be.southcentralus.azurecontainer.io/score'
api_key = 'Y04aAucipwr1HfkhST8QChxt6SPtgaP6' # Replace this with the API key for the web service

# The azureml-model-deployment header will force the request to go to a specific deployment.
# Remove this header to have the request observe the endpoint traffic rules
headers = {'Content-Type':'application/json', 'Authorization':('Bearer '+ api_key)}

req = urllib.request.Request(url, body, headers)

try:
    response = urllib.request.urlopen(req)

    result = response.read()
    print(result)
except urllib.error.HTTPError as error:
    print("The request failed with status code: " + str(error.code))

    # Print the headers - they include the requert ID and the timestamp, which are useful for debugging the failure
    print(error.info())
    print(error.read().decode("utf8", 'ignore'))
