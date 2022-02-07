import requests

#parameters to be sent for get reuest
params = {"q": "pizza"}

#pings/grabs info from passed parameters
r = requests.get("http://bing.com/search", params=params)

#test to print status from the pinged parameter
print("status:", r.status_code)

#get content of page requested
# print(r.text)

#writing printed content into html code
f = open("./page.html", "w+")
f.write(r.text)