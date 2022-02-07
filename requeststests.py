import requests
import simplejson as json
from io import BytesIO
from PIL import Image

#parameters to be sent for get reuest
# params = {"q": "pizza"}

# #pings/grabs info from passed parameters
# r = requests.get("http://bing.com/search", params=params)

# #test to print status from the pinged parameter
# print("status:", r.status_code)

# #get content of page requested
# # print(r.text)

# #writing printed content into html code
# f = open("./page.html", "w+")
# f.write(r.text)


#Returning images and information from binary

# r = requests.get("https://miro.medium.com/max/3150/1*83gxJM3OJJQxXFiXhRL3JQ.png")

# print("status", r.status_code)

# #return image from binary code that is received, content is binary data

# image = Image.open(BytesIO(r.content))



# print(image.size, image.format, image.mode)

# #saving image to desired pathway
# path = "./image." + image.format

# try: 
#     image.save(path, image.format)
# except IOError:
#     print ("Can't save image")


# Posting data from requests

# my_data = {"name": "Anthony", "email": "anthony@example.com"}

# r = requests.post("http://www.w3schools.com/php/welcome.php", data=my_data)

# f = open("myfile.html", "w+")
# f.write(r.text)


# Posting to JSON

# url = "https://www.googleapis.com/urlshortner/v1/url"
# payload = {"longUrl": "http://example.com"}
# headers = {"Content-Type": "application/json"}
# r = requests.post(url, json=payload, headers=headers)

# print(json.loads(r.text)["error"]["code"])