import requests

url = "http://localhost:9696/predict"
# url = "http://localhost:8080/predict"  # Use port 8080 with Kubernetes
# url = "http://<external-ip>.<region>.elb.amazonaws.com/predict"  # Update with EC2 load balancer DNS name

data = {"url": "http://bit.ly/mlbookcamp-pants"}

result = requests.post(url, json=data).json()
print(result)
