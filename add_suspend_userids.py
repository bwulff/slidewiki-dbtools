import sys
import argparse
import pymongo

parser = argparse.ArgumentParser(description='Load user IDs from STDIN into the collection for users that are to be suspended.')
parser.add_argument('url', type=str, help='URL of the MongoDB server')
args = parser.parse_args()

client = MongoClient(args.url)

for line in sys.stdin:
    user_id_str = line.strip()
    try:
        user_id = int(user_id_str)
        client['slidewiki'].insert_one({'_id':int(user_id)})
    except ValueError:
        print("ERROR: Bad user id sting: '{}'".format(user_id_str))
