import random
import re
import nltk
import json
import argparse
from nltk.chat.util import Chat, reflections
from class_information_helper import *

global json_data;
global classID;

reflections = {
    "am": "are",
    "was": "were",
    "i": "you",
    "i'd": "you would",
    "i've": "you have",
    "i'll": "you will",
    "my": "your",
    "are": "am",
    "you've": "I have",
    "you'll": "I will",
    "your": "my",
    "yours": "mine",
    "you": "me",
    "me": "you"
}

conversationals = [
    [r'(.*)(difficult)|(hard)|(easy)|(challenging)|(rigorous)(.*)',

        [
         "According to my data, it is an average difficulty of {0} out of 5.",
         "The average response is {0} out of 5.",
         "Depends, do you think {0}/5 is manageable?"
        ]
    ],
    [r'(.*)(how fun)|( fun )|(rating)|(.*)',

     [
         "{0}",
     ]
     ]
]



class ChatBot:
    def __init__(self, reviews):
        self.reviews = reviews['reviews']
        self.classID = None

    def respond(self, statement):
        response = self.analyze_question(statement)
        if response is None:
            return "I'm sorry I couldn't find any information. Did you enter the Course ID?"
        else:
            return response

    def reflect(self,fragment):
        tokens = fragment.lower().split()
        for i, token in enumerate(tokens):
            if token in reflections:
                tokens[i] = reflections[token]
        return ' '.join(tokens)

    def analyze_question(self, statement):
        if self.extract_class(statement):
            for pattern, responses in conversationals:
                match = re.search(pattern.lower(), statement.lower().rstrip(".!"))
                if match:
                    response = random.choice(responses)
                    return response.format(self.get_class_info(self.classID, match.group(0)))


    def extract_class(self, statement):
        tokens = statement.lower().split()
        for i, token in enumerate(tokens):
            if token[-4:].isdigit():
                self.classID = token[-4:]
                return True


    def get_class_info(self, class_id, indicator):
        if any(item in indicator for item in ['easy','hard','difficult','challenging','rigorous']):
            arg = 'difficulty'
        elif any(item in indicator for item in ['fun','rating','good']):
            arg = 'rating'

        switcher = {
            'difficulty': get_difficulty(class_id, self.reviews),
            'rating': get_rating(class_id, self.reviews)
        }

        func = switcher.get(arg)
        return func





