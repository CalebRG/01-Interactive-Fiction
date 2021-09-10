#!/usr/bin/env python3
import sys
assert sys.version_info >= (3,9), "This script requires at least Python 3.9"

world = {
  "uuid": "91D32992-1C50-493A-8F92-2D81D4DCE6BE",
  "name": "DebugProject1",
  "creator": "Twine",
  "creatorVersion": "2.3.14",
  "schemaName": "Harlowe 3 to JSON",
  "schemaVersion": "0.0.6",
  "createdAtMs": 1631310389452,
  "passages": [
    {
      "name": "Start",
      "tags": "",
      "id": "1",
      "text": "score - pos score\nscore2 neg score\nend end\n\n[[score->posscore]]\n[[score2->negscore]]\n[[end->end]]",
      "links": [
        {
          "linkText": "score",
          "passageName": "posscore",
          "original": "[[score->posscore]]"
        },
        {
          "linkText": "score2",
          "passageName": "negscore",
          "original": "[[score2->negscore]]"
        },
        {
          "linkText": "end",
          "passageName": "end",
          "original": "[[end->end]]"
        }
      ],
      "hooks": [],
      "cleanText": "score - pos score\nscore2 neg score\nend end"
    },
    {
      "name": "posscore",
      "tags": "50",
      "id": "2",
      "text": "positive score\n\n[[start->Start]]",
      "links": [
        {
          "linkText": "start",
          "passageName": "Start",
          "original": "[[start->Start]]"
        }
      ],
      "hooks": [],
      "cleanText": "positive score"
    },
    {
      "name": "negscore",
      "tags": "-50",
      "id": "3",
      "text": "negative score\n[[start->Start]]",
      "links": [
        {
          "linkText": "start",
          "passageName": "Start",
          "original": "[[start->Start]]"
        }
      ],
      "hooks": [],
      "cleanText": "negative score"
    },
    {
      "name": "end",
      "tags": "",
      "id": "4",
      "text": "You are at the end\n\n1->endpos1\n1->endpos2\n2->negend1\n2->negend2\n\n[[1->endpos1]]\n[[1->endpos2]]\n[[2->negend1]]\n[[2->negend2]]",
      "links": [
        {
          "linkText": "1",
          "passageName": "endpos1",
          "original": "[[1->endpos1]]"
        },
        {
          "linkText": "1",
          "passageName": "endpos2",
          "original": "[[1->endpos2]]"
        },
        {
          "linkText": "2",
          "passageName": "negend1",
          "original": "[[2->negend1]]"
        },
        {
          "linkText": "2",
          "passageName": "negend2",
          "original": "[[2->negend2]]"
        }
      ],
      "hooks": [],
      "cleanText": "You are at the end\n\n1->endpos1\n1->endpos2\n2->negend1\n2->negend2"
    },
    {
      "name": "endpos1",
      "tags": "",
      "id": "5",
      "text": "pos score end",
      "links": [],
      "hooks": [],
      "cleanText": "pos score end"
    },
    {
      "name": "endpos2",
      "tags": "",
      "id": "6",
      "text": "pos score end 2",
      "links": [],
      "hooks": [],
      "cleanText": "pos score end 2"
    },
    {
      "name": "negend1",
      "tags": "",
      "id": "7",
      "text": "negend1",
      "links": [],
      "hooks": [],
      "cleanText": "negend1"
    },
    {
      "name": "negend2",
      "tags": "",
      "id": "8",
      "text": "negend2",
      "links": [],
      "hooks": [],
      "cleanText": "negend2"
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
