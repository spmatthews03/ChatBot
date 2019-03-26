import json
import argparse
from ChatBot import ChatBot as cb

global json_data;


def read_json_file(filename):
    if filename:
        raw_json_file = open(filename, 'r', encoding='utf8')
        datastore = json.load(raw_json_file)
    return datastore


def main():
    parser = argparse.ArgumentParser(description='Process filename')
    parser.add_argument("--filename", type=str, required=True, help='filename with json data')
    args = parser.parse_args()
    json_data = read_json_file(args.filename)
    chatbot = cb(json_data)

    print("Hello I'm your OMSCS Central Chatbot. How may I help you?")
    while True:
        statement = input("> ")
        print(chatbot.respond(statement))

        if statement == "quit":
            break



if __name__ == '__main__':
    main()