import requests
from bs4 import BeautifulSoup
import re
import json

response = requests.get("https://demun.github.io/vscode-tutorial/shortcuts/")
soup = BeautifulSoup(response.text, 'html.parser')
data = {}

# dict형식에 맞도록 데이터 추출
# {
#     "동작":[
#        { 
#             "키":"...",
#             "명령":"...",
#             "명령ID":"..."
#         }
#     ]
# }

h2_tags = soup.find_all('h2')
for h2 in h2_tags:
    key = h2.text.strip()  # h2 태그의 텍스트를 key로 사용
    data[key] = []

    # 현재 h2 태그의 다음 sibling이 테이블인 경우 데이터 추출
    table = h2.find_next_sibling('table')
    if table:
        tbody = table.find('tbody')
        if tbody:
            rows = tbody.find_all('tr')
            for row in rows:
                columns = row.find_all('td')
                value1 = columns[0].text.strip()
                value2 = columns[1].text.strip()
                value3 = columns[2].text.strip()
                if value1 == "할당되지 않음":
                    continue
                data[key].append({
                    "키": value1,
                    "명령": value2,
                    "명령 ID": value3
                })


# 문자열 전처리
for key in data.copy().keys():
    new_key = re.sub(r"[^\uAC00-\uD7A3\s]", "", key)
    data[new_key] = data[key]
    del data[key]
for key, item_list in data.items():
    for item in item_list:
        text = item["명령"]
        pattern = r"\([^)]*\)"
        new_text = re.sub(pattern=pattern, repl='', string=text).strip()
        item["명령"] = new_text

# json파일 저장
datasets_path = "./datasets/"
jsonFile_name = "indata.json"
with open(datasets_path+jsonFile_name, "w", encoding='utf-8') as json_file:
    for key, item_list in data.items():
        for item in item_list:
            input_josa = "를"
            response_josa = "는"
            last_word_k = item['명령'][-1]
            if (ord(last_word_k)-ord("가")) % 28 != 0:
                input_josa = "을"
                response_josa = "은"
            inputs = f"vscode에서 {item['명령']}{input_josa} 하려면 어떻게 해야해?"
            response = f"vscode에서 {item['명령']}{response_josa} {key}동작이며, {item['키']}으로 수행할 수 있습니다. 명령 ID는 {item['명령 ID']}입니다."
            data = {"inputs": inputs, "response": response}
            json.dump(data, json_file, ensure_ascii=False)
            json_file.write("\n")