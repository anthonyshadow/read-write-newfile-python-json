import simplejson as json
import os


#example use case for reading and writing a file would be a save point in a video game

#first parameter file we want to create, second parameter is what type of operations it will take on the file (r = read, w = write)
# newfile = open("newfile.txt","w+")

# string = "This is the content that will be written to the text file"

# newfile.write(string)


#first check if file exisits and if there is information in the file

if os.path.isfile("./ages.json") and os.stat("./ages.json").st_size != 0:
    old_file = open("./age.json", "r+")
    # opens old file as a python usable object
    data = json.loads(old_file.read())
    print("current age is", data["age"], "-- adding a year")
    data["age"] = data["age"] + 1
    print("new age is", data["age"])

#if File does not exist

else:
    old_file = open(".ages.json", "w+")
    data = {"name": "Anthony", "age": 26}
    print("No file was found, setting default age to", data["age"])

#if there is an old file already exisiting we need to seek to the 0 position so it doesnt just append data into the file
old_file.seek(0)
#now we want to write but we need to reconvert it back to a json object
old_file.write(json.dumps(data))
