import argparse
import pymongo

parser = argparse.ArgumentParser(description='Load user IDs from a text file into the collection for users that are to be suspended.')
parser.add_argument('url', type=str, help='URL of the MongoDB server')
parser.add_argument('filename', type=str, help='text file to read user names from')

args = parser.parse_args()

client = MongoClient(args.url)

with open(filename, 'r') as file:
    for line in file:
        username = line.strip()
        user_id = None
        try:
            user = client['slidewiki'].      TODO    
        try:
            user_id = int(user_id_str)
            client['slidewiki'].insert_one({'_id':int(user_id)})
        except ValueError:
            print("ERROR: Bad user id string: '{}'".format(user_id_str))
