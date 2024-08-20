# # # # # # #
import datetime
import json
date = datetime.datetime.now()

## -- Getting User Input -- ##
message = input("Status Update:\n    ")
q_image = input("\nWould you like to add an image (y or n)? ")

if q_image == "y":
    image = input("Image file: ")
    c_image = input("Image Caption:\n    ")

with open('site/_data/entries.json', 'r+', encoding='utf-8') as f:
        last_color = json.load(f)
        last_color = last_color["last_color"]
color = input("\nWhat color do you want? Last color: " + last_color + "\npurple, green, green-alt, blood, blood-alt, pink, pink-alt, black, white\n    ")

## -- Updating data -- ##

try:
    with open('site/_data/entries.json', 'r+', encoding='utf-8') as f:
        data = json.load(f)
        data["num"] += 1
        data["last_color"] = color

        new_entry = {};
        new_entry["id"] = data["num"]
        new_entry["time"] = date.strftime("%H:%M")
        new_entry["date"] = date.strftime("%Y-%m-%d")
        new_entry["color"] = color
        new_entry["content"] = message

        if q_image == "y":
            new_entry["image"] = [c_image, image]
        else:
            new_entry["image"] = None

        data["list"].append(new_entry)

        f.seek(0)
        json.dump(data, f, indent=4, ensure_ascii=False)
        f.truncate()

    print("\nEntry " + str(data["num"]) + " written. <3")
except Exception as e:
    print("\nAn error has occurred:")
    print(e)
finally:
    print("-------")
