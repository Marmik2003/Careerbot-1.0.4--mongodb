import pymongo
from pymongo import MongoClient
from random import choice
from datetime import datetime

now = datetime.now()

cluster = MongoClient("mongodb+srv://root:1234@careerbot.i0gdj.mongodb.net/<dbname>?retryWrites=true&w=majority")
db = cluster["res_data"]
collection = db["res_data"]

def chat_reply(msg):
    query = {'input':msg}
    try:
        doc = collection.find(query)
        output_list =[]
        for message in doc:
            output_list.append(message)
        random_msg = choice(output_list)
        return random_msg['output']
    except IndexError:
        garbage_collection = db["unknown_inputs"]
        unkn_inpt_dict = {'input':msg,'Date & Time':now}
        garbage_collection.insert_one(unkn_inpt_dict)
        return 'Sorry, I don\'t know about that. But, I stored it in my database so that my developers can review that!'
