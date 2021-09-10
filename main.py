#!/usr/bin/env python3
import sys
assert sys.version_info >= (3,9), "This script requires at least Python 3.9"

world = {
  "uuid": "3FAA8C3E-DDB1-42EA-9D6A-FFE2456D2D82",
  "name": "Decisions",
  "creator": "Twine",
  "creatorVersion": "2.3.14",
  "schemaName": "Harlowe 3 to JSON",
  "schemaVersion": "0.0.6",
  "createdAtMs": 1631105982477,
  "passages": [
    {
      "name": "Start",
      "tags": "",
      "id": "1",
      "text": "For the 3 years that you've been alive, every decision \nhas been made for you, such as how to dress, shower, \nplay, etc. On one summer morning, you decide it was time to\nstart making decisions for yourself, starting with what to wear.\n\nclothe1 - A red flannel with jeans \nclothe2 - a lime green shirt with shorts\nclothe3 - A black jacket with sweatpants\nclothe0 - Who needs clothes?\n\n[[clothe1->clothe1]]\n[[clothe2->clothe2]]\n[[clothe3->clothe3]]\n[[clothe0->clothe0]]",
      "links": [
        {
          "linkText": "clothe1",
          "passageName": "clothe1",
          "original": "[[clothe1->clothe1]]"
        },
        {
          "linkText": "clothe2",
          "passageName": "clothe2",
          "original": "[[clothe2->clothe2]]"
        },
        {
          "linkText": "clothe3",
          "passageName": "clothe3",
          "original": "[[clothe3->clothe3]]"
        },
        {
          "linkText": "clothe0",
          "passageName": "clothe0",
          "original": "[[clothe0->clothe0]]"
        }
      ],
      "hooks": [],
      "cleanText": "For the 3 years that you've been alive, every decision \nhas been made for you, such as how to dress, shower, \nplay, etc. On one summer morning, you decide it was time to\nstart making decisions for yourself, starting with what to wear.\n\nclothe1 - A red flannel with jeans \nclothe2 - a lime green shirt with shorts\nclothe3 - A black jacket with sweatpants\nclothe0 - Who needs clothes?"
    },
    {
      "name": "DEATH",
      "tags": "",
      "id": "2",
      "text": "You are dead.\nType rebirth to start from beginning\n\n[[rebirth->Start]]",
      "links": [
        {
          "linkText": "rebirth",
          "passageName": "Start",
          "original": "[[rebirth->Start]]"
        }
      ],
      "hooks": [],
      "cleanText": "You are dead.\nType rebirth to start from beginning"
    },
    {
      "name": "clothe1",
      "tags": "",
      "id": "3",
      "text": "Pretty tame, but it gets the job done\n\n+ 10 Points!\n\nType cont to continue!\n\n[[cont->classroom]]",
      "links": [
        {
          "linkText": "cont",
          "passageName": "classroom",
          "original": "[[cont->classroom]]"
        }
      ],
      "hooks": [],
      "cleanText": "Pretty tame, but it gets the job done\n\n+ 10 Points!\n\nType cont to continue!"
    },
    {
      "name": "clothe2",
      "tags": "",
      "id": "4",
      "text": "You look absolutely disgusting, but points for trying to be creative\n\n+ 10 Points!\n\nType cont to continue!\n\n[[cont->classroom]]",
      "links": [
        {
          "linkText": "cont",
          "passageName": "classroom",
          "original": "[[cont->classroom]]"
        }
      ],
      "hooks": [],
      "cleanText": "You look absolutely disgusting, but points for trying to be creative\n\n+ 10 Points!\n\nType cont to continue!"
    },
    {
      "name": "clothe3",
      "tags": "",
      "id": "5",
      "text": "Its literally 90 degrees outside, you quickly realize this\nonce you stepped out and a pool of sweat starts piling\naround you. Yet pride made you stick with it.\n\n+ 10 Points!\n\nType cont to continue!\n\n[[cont->classroom]]",
      "links": [
        {
          "linkText": "cont",
          "passageName": "classroom",
          "original": "[[cont->classroom]]"
        }
      ],
      "hooks": [],
      "cleanText": "Its literally 90 degrees outside, you quickly realize this\nonce you stepped out and a pool of sweat starts piling\naround you. Yet pride made you stick with it.\n\n+ 10 Points!\n\nType cont to continue!"
    },
    {
      "name": "clothe0",
      "tags": "",
      "id": "6",
      "text": "Yeah maybe try again\n\ntype nonaked to go back\n\n[[nonaked->Start]]",
      "links": [
        {
          "linkText": "nonaked",
          "passageName": "Start",
          "original": "[[nonaked->Start]]"
        }
      ],
      "hooks": [],
      "cleanText": "Yeah maybe try again\n\ntype nonaked to go back"
    },
    {
      "name": "classroom",
      "tags": "",
      "id": "7",
      "text": "Eat Chalk?\nYes or No?\n\n[[yes->DEATH]]\n[[no->Start]]",
      "links": [
        {
          "linkText": "yes",
          "passageName": "DEATH",
          "original": "[[yes->DEATH]]"
        },
        {
          "linkText": "no",
          "passageName": "Start",
          "original": "[[no->Start]]"
        }
      ],
      "hooks": [],
      "cleanText": "Eat Chalk?\nYes or No?"
    }
  ]
}


# ----------------------------------------------------------------

def find_current_location(location_label):
	if "passages" in world:
		for passage in world["passages"]:
			if location_label == passage["name"]:
				return passage
	return {}

# ----------------------------------------------------------------

def render(current_location, score):
	print("Score: " + str(score))
	print(current_location["cleanText"])

def get_input():
	response = input('')
	return response
      


def update(current_location, location_label, response):
	if response == "":
		return location_label
	for link in current_location["links"]:
		if link["linkText"] == response:
			return link["passageName"]

	print("What? Try again!")
	return location_label


# ----------------------------------------------------------------

location_label = "Start"
current_location = {}
response = ""
score=0

while True:
	if response == "QUIT":
		break
	location_label = update(current_location, location_label, response)
	current_location = find_current_location(location_label)
	if "score" in current_location:
		score = score + current_location["score"]
	render(current_location, score)
	response = get_input()
