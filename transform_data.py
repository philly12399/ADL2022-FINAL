import json
import csv
with open('./output_baseline.jsonl') as json_file:
    json_list = list(json_file)

with open('./final_project_scripts/keywords.json') as fp:
    keywords = json.load(fp)
    
train_data = []
cnt = 0

with open('source.csv', 'w', newline='') as csvfile, open('target.csv', 'w', newline='') as targetfile:
    writer1 = csv.writer(csvfile)
    writer2 = csv.writer(targetfile)
    for json_str in json_list:
        result = json.loads(json_str)
        for i in range(len(result["dialog"]) - 2):
            for k in keywords:
                if k in result["dialog"][i+2]:
                    writer1.writerow([cnt, result["dialog"][i], result["dialog"][i+2]])
                    writer2.writerow([cnt, result["dialog"][i+1]])
                    cnt += 1
                    break
