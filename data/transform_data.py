import json
import csv
with open('./output_train.jsonl') as json_file:
    json_list = list(json_file)

with open('./keywords.json') as fp:
    keywords = json.load(fp)
    
train_data = []
cnt = 0

keyword_list = []
for k in keywords['song']:
    keyword_list.append(k)
for k in keywords['transportation']:
    keyword_list.append(k)
for k in keywords['attraction']:
    keyword_list.append(k)
for k in keywords['restaurant']:
    keyword_list.append(k)
for k in keywords['hotel']:
    keyword_list.append(k)
for k in keywords['movie']:
    keyword_list.append(k)

with open('source.csv', 'w', newline='', encoding='utf-8') as csvfile, open('target.csv', 'w', newline='', encoding='utf-8') as targetfile:
    writer1 = csv.writer(csvfile)
    writer2 = csv.writer(targetfile)
    for json_str in json_list:
        result = json.loads(json_str)
        for i in range(len(result["dialog"]) - 2):
            for k in keyword_list:
                if k in result["dialog"][i+2]:
                    writer1.writerow([cnt, result["dialog"][i], result["dialog"][i+2]])
                    writer2.writerow([cnt, result["dialog"][i+1]])
                    cnt += 1
                    break