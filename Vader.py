import csv

from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
analyser = SentimentIntensityAnalyzer()
has_more_comments = True
max_id = ''
comments = []
sentiment = []
combine = []

result_file = open('insta/aigbe_res6.csv', 'w', newline='')

# 'neg': 0.0, 'neu': 0.509, 'pos': 0.491, 'compound': 0.6997
with open('insta/aigbe6.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    line_count = 0
    for row in csv_reader:
        comments.append(row)
        for i in row:
            calc = str(analyser.polarity_scores(i))
            result_file.write(calc)
            result_file.write('\n')


