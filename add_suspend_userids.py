import sys
import argparse
import pymongo

parser = argparse.ArgumentParser(description='Load user IDs from STDIN into the collection for users that are to be suspended.')
parser.add_argument('url', type=str, help='URL of the MongoDB server')
parser.add_argument('--db', dest='dbname', default='slidewiki', help='name of the database')
args = parser.parse_args()

client = MongoClient(args.url)

print("writing user IDs to collection {}.useridsforsuspension".format(args.dbname))

for line in sys.stdin:
    user_id_str = line.strip()
    try:
        user_id = int(user_id_str)
        client[args.dbname].useridsforsuspension.insert_one({'_id':int(user_id)})
    except:
        print("Failed to insert id {}".format(line))
