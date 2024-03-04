# # # # # # #
import time
import datetime
import json
x = datetime.datetime.now()

## -- Setting Up Functions & Variables -- ##
site_url = "https://status.shroom.ink/#"
img_url = "./src/img/status/"
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

def read_last_color():
    with open("last_color.txt", 'r+') as f:
        return f.read()

def replace_last_color(new_color):
    with open("last_color.txt", 'r+') as f:
        f.seek(0)
        f.truncate()
        f.write(new_color)

def add_content(content):
    global code
    code += content

## -- Getting User Input -- ##
message = input("Status Update:\n    ")
q_image = input("\nWould you like to add an image (y or n)? ")
if q_image == "y":
    image = input("Image file: ")
    c_image = input("Image Caption:\n    ")
color = input("\nWhat color do you want? Last color: " + read_last_color() + "\npurple, green, green-alt, blood, blood-alt, pink, pink-alt, black, white\n    ")

## -- Iterating Status ID / Count -- ##

with open('site/_data/x.json', 'r+') as f:
    data = json.load(f)
    data['num'] += 1
    f.seek(0)
    json.dump(data, f, indent=4)
    f.truncate()

## -- Creating the HTML -- ##
add_content('\n\n<article class="{0}" id="{1}">'.format(color, str(data["num"])))
add_content('\n<h2><a target="_top" href="{0}{1}">{2}</a></h2>'.format(site_url, str(data["num"]), x.strftime("%Y-%m-%d")))
add_content('\n<p class="time">&#x1F555;{0}</p>'.format(x.strftime("%H:%M")))
add_content('\n<p class="content">{0}</p>'.format(message))
if q_image == "y":
    add_content('\n<figure><img loading="lazy" src="{0}{1}"><figcaption>{2}</figcaption></figure>'.format(img_url, image, c_image));
add_content('\n</article>')

replace_last_color(color)

## -- Injecting the HTML -- ##
try:
    code_prepender("site/_includes/status.html", code)
    code_replacer("site/_includes/latest_status.html", code)
    print("\nEntry " + str(data["num"]) + " written. <3")
except:
    print("\nAn error has occurred.")
finally:
    print("-------")
