import json
with open('./problemset.json','r',encoding='utf8')as fp:
    json_data = json.load(fp);

result=json_data["result"];

problems=result["problems"];
problemStatistics=result["problemStatistics"];

cnt=0;
for i in problems:
    cnt+=1;
    print(cnt,i);