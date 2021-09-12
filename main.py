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
  "createdAtMs": 1631409513589,
  "passages": [
    {
      "name": "Start",
      "tags": "0",
      "id": "1",
      "text": "For the 3 years that you've been alive, every decision \nhas been made for you, such as how to dress, shower, \nplay, etc. On one summer morning, you decide it was time to\nstart making decisions for yourself, starting with what to wear.\n\nclothe1 - A red flannel with jeans \nclothe2 - a lime green shirt with shorts\nclothe3 - A black jacket with sweatpants\nclothe0 - Who needs clothes?\n\n[[clothe1->clothe1]]\n[[clothe2->clothe2]]\n[[clothe3->clothe3]]\n[[clothe0->clothe0]]\n\n[[end->end]]",
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
        },
        {
          "linkText": "end",
          "passageName": "end",
          "original": "[[end->end]]"
        }
      ],
      "hooks": [],
      "cleanText": "For the 3 years that you've been alive, every decision \nhas been made for you, such as how to dress, shower, \nplay, etc. On one summer morning, you decide it was time to\nstart making decisions for yourself, starting with what to wear.\n\nclothe1 - A red flannel with jeans \nclothe2 - a lime green shirt with shorts\nclothe3 - A black jacket with sweatpants\nclothe0 - Who needs clothes?"
    },
    {
      "name": "Death",
      "tags": "0",
      "id": "2",
      "text": "You are dead.\n\nType restart to start from beginning\n\n[[restart->Start]]",
      "links": [
        {
          "linkText": "restart",
          "passageName": "Start",
          "original": "[[restart->Start]]"
        }
      ],
      "hooks": [],
      "cleanText": "You are dead.\n\nType restart to start from beginning"
    },
    {
      "name": "clothe1",
      "tags": "10",
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
      "tags": "5",
      "id": "4",
      "text": "You look absolutely disgusting, but points for trying to be creative\n\n+ 5 Points!\n\nType cont to continue!\n\n[[cont->classroom]]",
      "links": [
        {
          "linkText": "cont",
          "passageName": "classroom",
          "original": "[[cont->classroom]]"
        }
      ],
      "hooks": [],
      "cleanText": "You look absolutely disgusting, but points for trying to be creative\n\n+ 5 Points!\n\nType cont to continue!"
    },
    {
      "name": "clothe3",
      "tags": "5",
      "id": "5",
      "text": "Its literally 90 degrees outside, you quickly realize this\nonce you stepped out and a pool of sweat starts piling\naround you. Yet pride made you stick with it.\n\n+ 5 Points!\n\nType cont to continue!\n\n[[cont->classroom]]",
      "links": [
        {
          "linkText": "cont",
          "passageName": "classroom",
          "original": "[[cont->classroom]]"
        }
      ],
      "hooks": [],
      "cleanText": "Its literally 90 degrees outside, you quickly realize this\nonce you stepped out and a pool of sweat starts piling\naround you. Yet pride made you stick with it.\n\n+ 5 Points!\n\nType cont to continue!"
    },
    {
      "name": "clothe0",
      "tags": "0",
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
      "tags": "0",
      "id": "7",
      "text": "You are playing with your favorite toy in class one day.\nThis toy is the best thing in the world.\nYou would consider dying for this toy.\n\nRoger McGee sees you having fun, and decides\nhe also wanted a piece of that. \nHe quickly swipes the toy from your hands.\n\nfight - Start fighting him.\nscream - Throw a tantrum\nteacher - tell the teacher\n\n[[fight->fight]]\n[[scream->scream]]\n[[teacher->teacher]]",
      "links": [
        {
          "linkText": "fight",
          "passageName": "fight",
          "original": "[[fight->fight]]"
        },
        {
          "linkText": "scream",
          "passageName": "scream",
          "original": "[[scream->scream]]"
        },
        {
          "linkText": "teacher",
          "passageName": "teacher",
          "original": "[[teacher->teacher]]"
        }
      ],
      "hooks": [],
      "cleanText": "You are playing with your favorite toy in class one day.\nThis toy is the best thing in the world.\nYou would consider dying for this toy.\n\nRoger McGee sees you having fun, and decides\nhe also wanted a piece of that. \nHe quickly swipes the toy from your hands.\n\nfight - Start fighting him.\nscream - Throw a tantrum\nteacher - tell the teacher"
    },
    {
      "name": "fight",
      "tags": "0",
      "id": "8",
      "text": "You decide the fists are the only solution to this problem.\nYou have options where to hit:\n\nstomach\nface\ngroin\n\nType gandhi to go back\n\n[[stomach->stomach]]\n[[face->face]]\n[[groin->groin]]\n[[gandhi->classroom]]",
      "links": [
        {
          "linkText": "stomach",
          "passageName": "stomach",
          "original": "[[stomach->stomach]]"
        },
        {
          "linkText": "face",
          "passageName": "face",
          "original": "[[face->face]]"
        },
        {
          "linkText": "groin",
          "passageName": "groin",
          "original": "[[groin->groin]]"
        },
        {
          "linkText": "gandhi",
          "passageName": "classroom",
          "original": "[[gandhi->classroom]]"
        }
      ],
      "hooks": [],
      "cleanText": "You decide the fists are the only solution to this problem.\nYou have options where to hit:\n\nstomach\nface\ngroin\n\nType gandhi to go back"
    },
    {
      "name": "scream",
      "tags": "-5",
      "id": "9",
      "text": "you decided to throw a tantrum \n\nyour crush called you a crybaby\n\nthis was the same day you decided you\nwanted a mullet\n\n-5 Points\n\nType cont to continue\n[[cont->hungry]]",
      "links": [
        {
          "linkText": "cont",
          "passageName": "hungry",
          "original": "[[cont->hungry]]"
        }
      ],
      "hooks": [],
      "cleanText": "you decided to throw a tantrum \n\nyour crush called you a crybaby\n\nthis was the same day you decided you\nwanted a mullet\n\n-5 Points\n\nType cont to continue"
    },
    {
      "name": "teacher",
      "tags": "0",
      "id": "10",
      "text": "You told your teacher about the situation.\n\nShe seems obviously bothered by you\n\nType cont to continue\n[[cont->hungry]]",
      "links": [
        {
          "linkText": "cont",
          "passageName": "hungry",
          "original": "[[cont->hungry]]"
        }
      ],
      "hooks": [],
      "cleanText": "You told your teacher about the situation.\n\nShe seems obviously bothered by you\n\nType cont to continue"
    },
    {
      "name": "stomach",
      "tags": "5",
      "id": "11",
      "text": "You punched his stomach, leaving him winded.\nHe did not take your toys after that,\nand everyday he allowed you\nto have first pick toy. \n\n5 Points!\n\nType cont to continue\n[[cont->hungry]]",
      "links": [
        {
          "linkText": "cont",
          "passageName": "hungry",
          "original": "[[cont->hungry]]"
        }
      ],
      "hooks": [],
      "cleanText": "You punched his stomach, leaving him winded.\nHe did not take your toys after that,\nand everyday he allowed you\nto have first pick toy. \n\n5 Points!\n\nType cont to continue"
    },
    {
      "name": "face",
      "tags": "-5",
      "id": "12",
      "text": "You punched his face, reopening stiches he had recieved by\nother kids punching his face. \n\nMom sold your Xbox after that\n\n-5 Points\n\nType cont to continue\n[[cont->hungry]]",
      "links": [
        {
          "linkText": "cont",
          "passageName": "hungry",
          "original": "[[cont->hungry]]"
        }
      ],
      "hooks": [],
      "cleanText": "You punched his face, reopening stiches he had recieved by\nother kids punching his face. \n\nMom sold your Xbox after that\n\n-5 Points\n\nType cont to continue"
    },
    {
      "name": "groin",
      "tags": "-10",
      "id": "13",
      "text": "You decide to play it cheaply and hit his groin. \nNo one approached you in recess after that,\nand now all the other kids cover their groin\nwhen they are around you.\n\nWhere is the honor?\n\nType cont to continue\n[[cont->hungry]]",
      "links": [
        {
          "linkText": "cont",
          "passageName": "hungry",
          "original": "[[cont->hungry]]"
        }
      ],
      "hooks": [],
      "cleanText": "You decide to play it cheaply and hit his groin. \nNo one approached you in recess after that,\nand now all the other kids cover their groin\nwhen they are around you.\n\nWhere is the honor?\n\nType cont to continue"
    },
    {
      "name": "hungry",
      "tags": "0",
      "id": "14",
      "text": "You are in your room thinking about the moon,\nand how it sort of looks like a big gray pile of cheese.\n\nYou then realize you have not ate since breakfast, and\ndinner has not been called for.\n\n\nmom - Find and ask your Mom for dinner\ncook - Do it yourself!\nstarve - Hope that you'll get food another time\n\n\n[[mom->mom]]\n[[cook->cook]]\n[[starve->Death]]",
      "links": [
        {
          "linkText": "mom",
          "passageName": "mom",
          "original": "[[mom->mom]]"
        },
        {
          "linkText": "cook",
          "passageName": "cook",
          "original": "[[cook->cook]]"
        },
        {
          "linkText": "starve",
          "passageName": "Death",
          "original": "[[starve->Death]]"
        }
      ],
      "hooks": [],
      "cleanText": "You are in your room thinking about the moon,\nand how it sort of looks like a big gray pile of cheese.\n\nYou then realize you have not ate since breakfast, and\ndinner has not been called for.\n\n\nmom - Find and ask your Mom for dinner\ncook - Do it yourself!\nstarve - Hope that you'll get food another time"
    },
    {
      "name": "mom",
      "tags": "5",
      "id": "15",
      "text": "Finding your mom in her bed, you approach her and ask about\ndinner. She then looks at you with confusion, like\na stranger just asked her to tie his shoe for him, but \nhas flip flops on. \n\nAfter a moment, she realizes that dinner needs to be\nmade for you, and decides to make you a peanut butter\nand jelly sandwich.\n\nShe forgot to peanut butter\n\nand the jelly\n\njust gave you bread.\n\nTasted funny.\n\n5 Points!\n\ntype cont to continue\n[[cont->grad]]",
      "links": [
        {
          "linkText": "cont",
          "passageName": "grad",
          "original": "[[cont->grad]]"
        }
      ],
      "hooks": [],
      "cleanText": "Finding your mom in her bed, you approach her and ask about\ndinner. She then looks at you with confusion, like\na stranger just asked her to tie his shoe for him, but \nhas flip flops on. \n\nAfter a moment, she realizes that dinner needs to be\nmade for you, and decides to make you a peanut butter\nand jelly sandwich.\n\nShe forgot to peanut butter\n\nand the jelly\n\njust gave you bread.\n\nTasted funny.\n\n5 Points!\n\ntype cont to continue"
    },
    {
      "name": "cook",
      "tags": "-5",
      "id": "16",
      "text": "You decided you wanted to cook for yourself. You picked up a package\nof instant noodles, but you forgot to add the water. Now\nyou're left with a burnt slab of noodles and a broken microwave.\n\n-5 Points\n\ntype cont to continue\n[[cont->grad]]",
      "links": [
        {
          "linkText": "cont",
          "passageName": "grad",
          "original": "[[cont->grad]]"
        }
      ],
      "hooks": [],
      "cleanText": "You decided you wanted to cook for yourself. You picked up a package\nof instant noodles, but you forgot to add the water. Now\nyou're left with a burnt slab of noodles and a broken microwave.\n\n-5 Points\n\ntype cont to continue"
    },
    {
      "name": "grad",
      "tags": "0",
      "id": "17",
      "text": "You have graduated High School!\nMom forgot to go to the ceremony. \n\nIt is time for you to take the next\nchapter in your life! \n\ncollege - Go to college!\nhome - Stay home for Mom\njob - Find a job\n\n[[college->college]]\n[[home->home]]\n[[job->job]]",
      "links": [
        {
          "linkText": "college",
          "passageName": "college",
          "original": "[[college->college]]"
        },
        {
          "linkText": "home",
          "passageName": "home",
          "original": "[[home->home]]"
        },
        {
          "linkText": "job",
          "passageName": "job",
          "original": "[[job->job]]"
        }
      ],
      "hooks": [],
      "cleanText": "You have graduated High School!\nMom forgot to go to the ceremony. \n\nIt is time for you to take the next\nchapter in your life! \n\ncollege - Go to college!\nhome - Stay home for Mom\njob - Find a job"
    },
    {
      "name": "college",
      "tags": "-5",
      "id": "18",
      "text": "You decided to attend your local college, and became\nroommates with your best friend Roger McGee.\nBut quickly got expelled for forgetting assignments\n\nYou then found a job that at the Moon Pie factory\n\n-5 Points\n\ntype cont to continue\n[[cont->clock]]",
      "links": [
        {
          "linkText": "cont",
          "passageName": "clock",
          "original": "[[cont->clock]]"
        }
      ],
      "hooks": [],
      "cleanText": "You decided to attend your local college, and became\nroommates with your best friend Roger McGee.\nBut quickly got expelled for forgetting assignments\n\nYou then found a job that at the Moon Pie factory\n\n-5 Points\n\ntype cont to continue"
    },
    {
      "name": "home",
      "tags": "5",
      "id": "19",
      "text": "You stay home to help your Mom, as\nher condition got worse and worse.\n\nAs you are picking out her clothes \nto wear for the day, you realize that\neverything just went full circle.\n\nTo pay to help your mother, you start working\nat the Moon Pie factory.\n\n5 Points\n\ntype cont to continue\n[[cont->clock]]",
      "links": [
        {
          "linkText": "cont",
          "passageName": "clock",
          "original": "[[cont->clock]]"
        }
      ],
      "hooks": [],
      "cleanText": "You stay home to help your Mom, as\nher condition got worse and worse.\n\nAs you are picking out her clothes \nto wear for the day, you realize that\neverything just went full circle.\n\nTo pay to help your mother, you start working\nat the Moon Pie factory.\n\n5 Points\n\ntype cont to continue"
    },
    {
      "name": "job",
      "tags": "5",
      "id": "20",
      "text": "You quickly found a job at the Moon Pie factory.\nYou forgot to wear the company shirt on the first day,\nyou now have the nickname \"Shirty\"\n\n5 Points\n\ntype cont to continue\n[[cont->clock]]",
      "links": [
        {
          "linkText": "cont",
          "passageName": "clock",
          "original": "[[cont->clock]]"
        }
      ],
      "hooks": [],
      "cleanText": "You quickly found a job at the Moon Pie factory.\nYou forgot to wear the company shirt on the first day,\nyou now have the nickname \"Shirty\"\n\n5 Points\n\ntype cont to continue"
    },
    {
      "name": "clock",
      "tags": "0",
      "id": "21",
      "text": "You are sitting at your Mom's house after\nhelping getting grocerys. You stare at a clock for \na while, before you realize it is not on the right time.\n\nOr not even ticking at all. \n\nfix - Attempt to fix it\nleave - Leave it\nclock - Get her a new clock\n\n[[fix->momd]]\n[[leave->momd]]\n[[clock->momd",
      "links": [
        {
          "linkText": "fix",
          "passageName": "momd",
          "original": "[[fix->momd]]"
        },
        {
          "linkText": "leave",
          "passageName": "momd",
          "original": "[[leave->momd]]"
        },
        {
          "linkText": "clock",
          "passageName": "momd",
          "original": "[[clock->momd"
        }
      ],
      "hooks": [],
      "cleanText": "You are sitting at your Mom's house after\nhelping getting grocerys. You stare at a clock for \na while, before you realize it is not on the right time.\n\nOr not even ticking at all. \n\nfix - Attempt to fix it\nleave - Leave it\nclock - Get her a new clock"
    },
    {
      "name": "momd",
      "tags": "0",
      "id": "22",
      "text": "Your mother died later that day, \n\nShe got hit by a train\n\nType cont to continue\n\n[[cont->stuff]]",
      "links": [
        {
          "linkText": "cont",
          "passageName": "stuff",
          "original": "[[cont->stuff]]"
        }
      ],
      "hooks": [],
      "cleanText": "Your mother died later that day, \n\nShe got hit by a train\n\nType cont to continue"
    },
    {
      "name": "stuff",
      "tags": "0",
      "id": "23",
      "text": "You had the will to everything she owned.\n\nsell - Sell her stuff\nlook - Look through her things\n\n[[sell->why]]\n[[look->look]]",
      "links": [
        {
          "linkText": "sell",
          "passageName": "why",
          "original": "[[sell->why]]"
        },
        {
          "linkText": "look",
          "passageName": "look",
          "original": "[[look->look]]"
        }
      ],
      "hooks": [],
      "cleanText": "You had the will to everything she owned.\n\nsell - Sell her stuff\nlook - Look through her things"
    },
    {
      "name": "why",
      "tags": "-5",
      "id": "24",
      "text": "You sold all your mothers stuff to a clown for\n$20 and a banana pie\n\n-5 Points\n\nType cont to continue\n[[cont->doctor]]",
      "links": [
        {
          "linkText": "cont",
          "passageName": "doctor",
          "original": "[[cont->doctor]]"
        }
      ],
      "hooks": [],
      "cleanText": "You sold all your mothers stuff to a clown for\n$20 and a banana pie\n\n-5 Points\n\nType cont to continue"
    },
    {
      "name": "look",
      "tags": "5",
      "id": "25",
      "text": "You find a book filled with memories of your late\nparents. You find one picture of your mom with\nRonald Reagan, with a little booger on his nose. \n\nYou noticed that the pages look like they were\nrained on.\n\nYou also find a ingredient list for \npeanut butter and jelly sandwich.\n\n\n5 Points\n\nType cont to continue\n[[cont->doctor]]",
      "links": [
        {
          "linkText": "cont",
          "passageName": "doctor",
          "original": "[[cont->doctor]]"
        }
      ],
      "hooks": [],
      "cleanText": "You find a book filled with memories of your late\nparents. You find one picture of your mom with\nRonald Reagan, with a little booger on his nose. \n\nYou noticed that the pages look like they were\nrained on.\n\nYou also find a ingredient list for \npeanut butter and jelly sandwich.\n\n\n5 Points\n\nType cont to continue"
    },
    {
      "name": "doctor",
      "tags": "0",
      "id": "26",
      "text": "You go to the doctors for whatever reason, and \nthe results you cannot remember. You got home\nby someone who claimed to be Roger. Do I know a\nRoger?\n\nThe doctor says I should take these pills, Roger\nexplains. \n\npills - Take the pills\nno - no pills\n\n[[pills->pills]]\n[[no->no]]",
      "links": [
        {
          "linkText": "pills",
          "passageName": "pills",
          "original": "[[pills->pills]]"
        },
        {
          "linkText": "no",
          "passageName": "no",
          "original": "[[no->no]]"
        }
      ],
      "hooks": [],
      "cleanText": "You go to the doctors for whatever reason, and \nthe results you cannot remember. You got home\nby someone who claimed to be Roger. Do I know a\nRoger?\n\nThe doctor says I should take these pills, Roger\nexplains. \n\npills - Take the pills\nno - no pills"
    },
    {
      "name": "pills",
      "tags": "5",
      "id": "27",
      "text": "You took the pill.\nTasted like moondust.\n\n5 Points\n\ntype cont to continue\n[[cont->2]]",
      "links": [
        {
          "linkText": "cont",
          "passageName": "2",
          "original": "[[cont->2]]"
        }
      ],
      "hooks": [],
      "cleanText": "You took the pill.\nTasted like moondust.\n\n5 Points\n\ntype cont to continue"
    },
    {
      "name": "no",
      "tags": "-5",
      "id": "28",
      "text": "we do not take candy from strangers\n\nyou ended up at the hospital again\n\n-5 Points\n\ntype cont to continue\n[[cont->2]]",
      "links": [
        {
          "linkText": "cont",
          "passageName": "2",
          "original": "[[cont->2]]"
        }
      ],
      "hooks": [],
      "cleanText": "we do not take candy from strangers\n\nyou ended up at the hospital again\n\n-5 Points\n\ntype cont to continue"
    },
    {
      "name": "walk",
      "tags": "0",
      "id": "29",
      "text": "You decided to go on a walk. \n\nWhere to?\n\npark - Park\ntrain - Train tracks\n\n[[park->park]]\n[[train->train]]",
      "links": [
        {
          "linkText": "park",
          "passageName": "park",
          "original": "[[park->park]]"
        },
        {
          "linkText": "train",
          "passageName": "train",
          "original": "[[train->train]]"
        }
      ],
      "hooks": [],
      "cleanText": "You decided to go on a walk. \n\nWhere to?\n\npark - Park\ntrain - Train tracks"
    },
    {
      "name": "park",
      "tags": "5",
      "id": "30",
      "text": "The park was beautiful today\n\nYou forgot your way back so you kicked rocks around\nuntil you found something familiar.\n\n5 Points!\n\ntype cont to continue\n[[cont->passout]]",
      "links": [
        {
          "linkText": "cont",
          "passageName": "passout",
          "original": "[[cont->passout]]"
        }
      ],
      "hooks": [],
      "cleanText": "The park was beautiful today\n\nYou forgot your way back so you kicked rocks around\nuntil you found something familiar.\n\n5 Points!\n\ntype cont to continue"
    },
    {
      "name": "train",
      "tags": "0",
      "id": "31",
      "text": "You sat at the train tracks for a while\n\nleave - go back home\nstay - stay on the tracks\n\n[[leave->passout]]\n[[stay->Death]]",
      "links": [
        {
          "linkText": "leave",
          "passageName": "passout",
          "original": "[[leave->passout]]"
        },
        {
          "linkText": "stay",
          "passageName": "Death",
          "original": "[[stay->Death]]"
        }
      ],
      "hooks": [],
      "cleanText": "You sat at the train tracks for a while\n\nleave - go back home\nstay - stay on the tracks"
    },
    {
      "name": "passout",
      "tags": "0",
      "id": "32",
      "text": "Going back home you realize that both your legs stopped working.\n\nWhile you were on the ground you saw a bee on a flower, and thought\ntoday was such a beautiful day.\n\ntype cont to continue\n[[cont->end]]",
      "links": [
        {
          "linkText": "cont",
          "passageName": "end",
          "original": "[[cont->end]]"
        }
      ],
      "hooks": [],
      "cleanText": "Going back home you realize that both your legs stopped working.\n\nWhile you were on the ground you saw a bee on a flower, and thought\ntoday was such a beautiful day.\n\ntype cont to continue"
    },
    {
      "name": "end",
      "tags": "0",
      "id": "33",
      "text": "You are now in a room full of concerned faces,\nYou have no idea whats going on\nWhere you are\nHow you are\nWhat you are\nWhen you are\nWho you are\n\nAll you know is that you have one decision left.\n\nlive\ndie\n\n[[live->live]]\n[[die->die]]",
      "links": [
        {
          "linkText": "live",
          "passageName": "live",
          "original": "[[live->live]]"
        },
        {
          "linkText": "die",
          "passageName": "die",
          "original": "[[die->die]]"
        }
      ],
      "hooks": [],
      "cleanText": "You are now in a room full of concerned faces,\nYou have no idea whats going on\nWhere you are\nHow you are\nWhat you are\nWhen you are\nWho you are\n\nAll you know is that you have one decision left.\n\nlive\ndie"
    },
    {
      "name": "live",
      "tags": "0",
      "id": "34",
      "text": "You chose to live\n\n[[restart->Start]]",
      "links": [
        {
          "linkText": "restart",
          "passageName": "Start",
          "original": "[[restart->Start]]"
        }
      ],
      "hooks": [],
      "cleanText": "You chose to live"
    },
    {
      "name": "die",
      "tags": "0",
      "id": "35",
      "text": "You chose to die\n\n[[restart->Start]]",
      "links": [
        {
          "linkText": "restart",
          "passageName": "Start",
          "original": "[[restart->Start]]"
        }
      ],
      "hooks": [],
      "cleanText": "You chose to die"
    },
    {
      "name": "Untitled Passage",
      "tags": "",
      "id": "36",
      "text": "You lived a good life, and you really did not want\\nto ruin a perfect day.\\nYou got up and roamed the earth countless times\\nYou read every book\\nHad many relationships\\nBecame a god to the human race\\nYou learned every language\\nYou learned everything that could\\nbe learned\\nYou saw everything that\\ncould be seen\\nYou saw as the sun ate the earth\\nYou saw as the sun disappeared.\\nYou saw all the other stars disappeared.\\nAnd now all you see is darkness.\\nOnly then you believed it was finally time.\\nThis ending is one of 4 endings based on score\\nType restart to start again",
      "links": [],
      "hooks": [],
      "cleanText": "You lived a good life, and you really did not want\\nto ruin a perfect day.\\nYou got up and roamed the earth countless times\\nYou read every book\\nHad many relationships\\nBecame a god to the human race\\nYou learned every language\\nYou learned everything that could\\nbe learned\\nYou saw everything that\\ncould be seen\\nYou saw as the sun ate the earth\\nYou saw as the sun disappeared.\\nYou saw all the other stars disappeared.\\nAnd now all you see is darkness.\\nOnly then you believed it was finally time.\\nThis ending is one of 4 endings based on score\\nType restart to start again"
    },
    {
      "name": "2",
      "tags": "0",
      "id": "37",
      "text": "You are in your room thinking about the moon,\nand how it sort of looks like a big gray pile of cheese.\n\nYou then realize you have not ate since breakfast, and\ndinner has not been called for.\n\n\nmom - Find and ask your Mom for dinner\ncook - Do it yourself!\nstarve - Hope that you'll get food another time\n\n\n[[mom->what]]\n[[cook->what]]\n[[starve->what]]",
      "links": [
        {
          "linkText": "mom",
          "passageName": "what",
          "original": "[[mom->what]]"
        },
        {
          "linkText": "cook",
          "passageName": "what",
          "original": "[[cook->what]]"
        },
        {
          "linkText": "starve",
          "passageName": "what",
          "original": "[[starve->what]]"
        }
      ],
      "hooks": [],
      "cleanText": "You are in your room thinking about the moon,\nand how it sort of looks like a big gray pile of cheese.\n\nYou then realize you have not ate since breakfast, and\ndinner has not been called for.\n\n\nmom - Find and ask your Mom for dinner\ncook - Do it yourself!\nstarve - Hope that you'll get food another time"
    },
    {
      "name": "what",
      "tags": "0",
      "id": "38",
      "text": "What were you thinking about?\n\nType cont to continue\n\n[[cont->walk]]",
      "links": [
        {
          "linkText": "cont",
          "passageName": "walk",
          "original": "[[cont->walk]]"
        }
      ],
      "hooks": [],
      "cleanText": "What were you thinking about?\n\nType cont to continue"
    },
    {
      "name": "Untitled Passage 1",
      "tags": "",
      "id": "39",
      "text": "You decided you haven't led a good life,\\nand wanted to see it all before you did.\\nYou got up and roamed the earth countless times\\nYou read every book\\nHad many relationships\\nBecame a god to the human race\\nYou learned every language\\nYou learned everything that could\\nbe learned\\nYou saw everything that\\ncould be seen\\nYou saw as the sun ate the earth\\nYou saw as the sun disappeared.\\nYou saw all the other stars disappeared.\\nAnd now all you see is darkness.\\nBut at the end, you still didn't feel  satisfied.\\nThis ending is one of 4 endings based on score\\nType restart to start again",
      "links": [],
      "hooks": [],
      "cleanText": "You decided you haven't led a good life,\\nand wanted to see it all before you did.\\nYou got up and roamed the earth countless times\\nYou read every book\\nHad many relationships\\nBecame a god to the human race\\nYou learned every language\\nYou learned everything that could\\nbe learned\\nYou saw everything that\\ncould be seen\\nYou saw as the sun ate the earth\\nYou saw as the sun disappeared.\\nYou saw all the other stars disappeared.\\nAnd now all you see is darkness.\\nBut at the end, you still didn't feel  satisfied.\\nThis ending is one of 4 endings based on score\\nType restart to start again"
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
	print("----------------------------------------------")
	print("Score: " + str(score))
	print(current_location["cleanText"])
	if current_location["name"] == "live":
		if score < 30:
			print("You decided you haven't led a good life,\nand wanted to see it all before you died.\nYou got up and roamed the earth countless times\nYou read every book\nHad many relationships\nBecame a god to the human race\nYou learned every language\nYou learned everything that could\nbe learned\nYou saw everything that\ncould be seen\nYou saw as the sun ate the earth\nYou saw as the sun disappeared.\nYou saw all the other stars disappeared.\nAnd now all you see is darkness.\nBut at the end, you still didn't feel  satisfied.\nThis ending is one of 4 endings based on score\nType restart to start again")
		if score >= 30:
			print("You lived a good life, and you really did not want\nto ruin a perfect day.\nYou got up and roamed the earth countless times\nYou read every book\nHad many relationships\nBecame a god to the human race\nYou learned every language\nYou learned everything that could\nbe learned\nYou saw everything that\ncould be seen\nYou saw as the sun ate the earth\nYou saw as the sun disappeared.\nYou saw all the other stars disappeared.\nAnd now all you see is darkness.\nOnly then you believed it was finally time.\nThis ending is one of 4 endings based on score\nType restart to start again")
	if current_location["name"] == "die":
		if score < 30:
			print("You are dead.\nType restart to start from beginning")
		if score >= 30:
			print("You decided you lived a good life.\nYou decided it was time to go.\nThe last thing you see is the moon.\nThis ending is one of 4 endings based on score\nType restart to start again")




def get_input():
	response = input("What is your decision? ")
	response = response.strip()
	return response

def update(current_location, location_label, response, score):
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
	if response == "quit":
		break
	location_label = update(current_location, location_label, response, score)
	current_location = find_current_location(location_label)
	if "tags" in current_location:
		score = score + int(current_location["tags"])
		if current_location["name"] == "Start": 
			score = 0
	render(current_location, score)
	response = get_input()
