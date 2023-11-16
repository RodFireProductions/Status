# # # # # # #
import time
import datetime
import json
x = datetime.datetime.now()

code = ""

def line_prepender(filename, line):
    with open(filename, 'r+') as f:
        content = f.read()
        f.seek(0, 0)
        f.write(line.rstrip('\r\n') + '\n' + content)
        
def addContent(content):
    global code
    code += content

message = input("Status Update: \n    ")

with open('site/_data/x.json', 'r+') as f:
    data = json.load(f)
    data['num'] += 1 
    f.seek(0)       
    json.dump(data, f, indent=4)
    f.truncate()
    
addContent("\n\n<article id=\""+ str(data["num"]) + "\">")
addContent("\n<h2>" + x.strftime("%Y-%m-%d") + "</h2>")
addContent("\n<p>&#x1F555;" + x.strftime("%H:%M") + "</p>")
addContent("\n<p>" + message + "</p>")
addContent("\n</article>")

try:
    line_prepender("site/_includes/status.html", code)

finally:
    print("\nEntry " + str(data["num"]) + " written. <3")
    print("-------")
    
    
