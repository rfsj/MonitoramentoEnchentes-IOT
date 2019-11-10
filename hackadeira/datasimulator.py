import requests
import random
from datetime import datetime
import time
import json

#LEVEL1 = ([0] * 10) + ([1] * 30)
#LEVEL2 = ([1] * 50) + ([0] * 60)

def generatedata():
    
    now = datetime.now()
    payload = {
        "level1" : random.randrange(1),
        "rain" : random.randrange(5),
        "level2" : random.randrange(1),
        "time" : now.strftime("%Y-%d-%mT%H:%M:%SZ")
    }
    #if LEVEL1 == [] or LEVEL2 == []:
    #    LEVEL1 = ([0] * 10) + ([1] * 30)
    #    LEVEL2 = ([1] * 50) + ([0] * 60)
        
    return payload

index = 0
while True:
    payload = generatedata()
    headers = {'content-type': 'application/json'}
    r = requests.post("http://10.0.202.214:9200/hackadeira3/_doc/{}".format(index), data=json.dumps(payload), headers=headers)
    print(r.text)
    index += 1
    time.sleep(1)