import requests
url = "https://safeut.test.med.utah.edu/apidemo/RestService/Quote"
req = requests.get(url)
return_value = req.json()
print(req.status_code)
print(return_value)

#Results
#200
#If I agreed with you we’d both be wrong.

