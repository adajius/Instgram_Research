from InstagramAPI import InstagramAPI
import time
from datetime import datetime
media_id = '1917494302427126132'#MERCY JOHNSON SALT....RESULT2
#media_id = '1903596981109045703' MERCY JOHNSON MORNING FRESH

# stop conditions, the script will end when first of them will be true
until_date = '2018-11-31'
count = 1350

API = InstagramAPI("ifyadaji", "123PASSword")
API.login()
API.getUsernameInfo("1334300193")
has_more_comments = True
max_id = ''
comments = []

while has_more_comments:
    _ = API.getMediaComments(media_id, max_id=max_id)
    # comments' page come from older to newer, lets preserve desc order in full list
    for c in reversed(API.LastJson['comments']):
        comments.append(c)
    has_more_comments = API.LastJson.get('has_more_comments', False)



    if has_more_comments:
            max_id = API.LastJson.get('next_max_id', '')
            time.sleep(2)

    lenc = len(comments)
    csvFile = "laura1.csv"
    csv = open(csvFile, "w", encoding="utf-8")
    columnTitleRow = "Commentsss\n"
    csv.write(columnTitleRow)

    for i in range(lenc):
        cc = comments[i]['text'] + "\n"
        csv.write(cc)