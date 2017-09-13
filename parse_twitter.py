import iPhone8
import pandas as pd

DATA_FILE = "iphone.json"

#data = "[{0}]".format(",".join[l for l in open(DATA_FILE).readlines()])

dataframe = pd.read_json(DATA_FILE)

#print("Successfully imported", len(df), "tweets")

"""
for line in open('iphone.json'):
    try:
        tweet.append(json.loads(line))
    except:
        pass
"""
