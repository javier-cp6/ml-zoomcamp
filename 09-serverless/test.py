import requests

url = "http://localhost:8080/2015-03-31/functions/function/invocations"
# url = "https://<api_id>.execute-api.<region>.amazonaws.com/test/predict"  # API Gateway endpoint

data = {"url": "http://bit.ly/mlbookcamp-pants"}

result = requests.post(url, json=data).json()
print(result)
