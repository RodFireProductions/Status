# # # # # # #
import time
import datetime
import json
x = datetime.datetime.now()

code = ""
image = ""
c_image = ""

def line_prepender(filename, line):
    with open(filename, 'r+', encoding="utf-8") as f:
        content = f.read()
        f.seek(0, 0)
        f.write(line.rstrip('\r\n') + '\n' + content)
        
def addContent(content):
    global code
    code += content

## --- ##
message = input("Status Update: \n    ")
q_image = input("\nWould you like to add an image (y or n)? ")
if q_image == "y":
    image = input("Image file: ")
    c_image = input("Image Caption: \n    ")
color = input("\nWhat color do you want?\npurple, green, green-alt, blood, blood-alt, pink, pink-alt, black, white\n    ")

## --- ##

with open('site/_data/x.json', 'r+') as f:
    data = json.load(f)
    data['num'] += 1 
    f.seek(0)       
    json.dump(data, f, indent=4)
    f.truncate()
    
addContent("\n\n<article class=\"" + color + "\" id=\"" + str(data["num"]) + "\">")
addContent("<div class=\"heading\">")
addContent("\n<h2>" + x.strftime("%Y-%m-%d") + "</h2>")
addContent("\n<p>&#x1F555;" + x.strftime("%H:%M") + "</p>")
addContent("</div>")
addContent("\n<p>" + message + "</p>")
if q_image == "y":
    addContent("\n<figure><img src=\"./src/img/status/"+ image + "\"><figcaption>" + c_image +"</figcaption></figure>")

addContent("\n</article>")

try:
    line_prepender("site/_includes/status.html", code)

finally:
    print("\nEntry " + str(data["num"]) + " written. <3")
    print("-------")
    
    
