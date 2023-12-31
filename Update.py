# # # # # # #
import time
import datetime
import json
x = datetime.datetime.now()

## -- Setting Up Functions & Variables -- ##
code = ""
image = ""
c_image = ""

def code_prepender(filename, code):
    with open(filename, 'r+', encoding="utf-8") as f:
        content = f.read()
        f.seek(0, 0)
        f.write(code.rstrip('\r\n') + '\n' + content)

def code_replacer(filename, code):
    with open(filename, 'r+', encoding="utf-8") as f:
        f.seek(0)
        f.truncate()
        f.write(code)

def addContent(content):
    global code
    code += content

## -- Getting User Input -- ##
message = input("Status Update:\n    ")
q_image = input("\nWould you like to add an image (y or n)? ")
if q_image == "y":
    image = input("Image file: ")
    c_image = input("Image Caption:\n    ")
color = input("\nWhat color do you want?\npurple, green, green-alt, blood, blood-alt, pink, pink-alt, black, white\n    ")

## -- Iterating Status ID / Count -- ##

with open('site/_data/x.json', 'r+') as f:
    data = json.load(f)
    data['num'] += 1
    f.seek(0)
    json.dump(data, f, indent=4)
    f.truncate()

## -- Creating the HTML -- ##
addContent("\n\n<article class=\"" + color + "\" id=\"" + str(data["num"]) + "\">")
addContent("\n<h2>" + x.strftime("%Y-%m-%d") + "</h2>")
addContent("\n<p class=\"time\">&#x1F555;" + x.strftime("%H:%M") + "</p>")
addContent("\n<p class=\"content\">" + message + "</p>")
if q_image == "y":
    addContent("\n<figure><img src=\"./src/img/status/"+ image + "\"><figcaption>" + c_image +"</figcaption></figure>")
addContent("\n</article>")


## -- Injecting the HTML -- ##
try:
    code_prepender("site/_includes/status.html", code)
    code_replacer("site/_includes/latest_status.html", code)
    print("\nEntry " + str(data["num"]) + " written. <3")
except:
    print("\nAn error has occurred.")
finally:
    print("-------")
