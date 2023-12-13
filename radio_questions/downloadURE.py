from calendar import c
from time import sleep
from bs4 import BeautifulSoup
import requests
import json

with open('questionsElectricidad.json', 'r') as fcc_file:
    fcc_data = json.load(fcc_file)

thirtyCounter = 0
#file = open('questions.json', 'w')
while thirtyCounter < 10:
    # URL of the page to be scraped
    url = 'https://www.ure.es/examenes/electricidad-y-radioelectricidad/'
    text = requests.get(url).text
    soup = BeautifulSoup(text, 'html.parser')
    questions = soup.find_all('div', class_="quiz-question")
    foundCount = 0
    for question in questions:
        q = question.find_all('div', class_="quiz-question-title")[0].text
        q = q.replace('"', "'").replace('\n', '').replace('\r', '').replace('\t', '').replace("                ", "").replace("            ", "")

        found = False
        for que in fcc_data:
            if que['question'] == q:
                found = True
                foundCount += 1
                break
        if found:
            continue
        else:
            answers  = question.find_all('label', class_="quiz-question-answer-ctrl-lbl")
            a = ''
            b = ''
            c = ''
            d = ''
            i = 0
            for answer in answers:
                if i == 0:
                    a = answer.text
                elif i == 1:
                    b = answer.text
                elif i == 2:
                    c = answer.text
                elif i == 3:
                    d = answer.text
                i += 1
            fcc_data.append({
                "question": q,
                "answers": [
                    a,
                    b,
                    c,
                    d
                ],
                "correct": -1
            })
    if foundCount == 30:
        thirtyCounter += 1
    else:
        thirtyCounter = 0
#    sleep(1)
    print(f'Found {foundCount} questions already in the file. {thirtyCounter} times 30 questions found in a row. Electricidad y radioelectricidad. Preguntas totales: {len(fcc_data)}')
    with open('questionsElectricidad.json', 'w') as fcc_file:
        json.dump(fcc_data, fcc_file, indent=4, ensure_ascii=False)


### 2nd part

with open('questionsNormativa.json', 'r') as fcc_file:
    fcc_data = json.load(fcc_file)

thirtyCounter = 0
#file = open('questions.json', 'w')
while thirtyCounter < 10:
    # URL of the page to be scraped
    url = 'https://www.ure.es/examenes/reglamentacion/'
    text = requests.get(url).text
    soup = BeautifulSoup(text, 'html.parser')
    questions = soup.find_all('div', class_="quiz-question")
    foundCount = 0
    for question in questions:
        q = question.find_all('div', class_="quiz-question-title")[0].text
        q = q.replace('"', "'").replace('\n', '').replace('\r', '').replace('\t', '').replace("                ", "").replace("            ", "")

        found = False
        for que in fcc_data:
            if que['question'] == q:
                found = True
                foundCount += 1
                break
        if found:
            continue
        else:
            answers  = question.find_all('label', class_="quiz-question-answer-ctrl-lbl")
            a = ''
            b = ''
            c = ''
            d = ''
            i = 0
            for answer in answers:
                if i == 0:
                    a = answer.text
                elif i == 1:
                    b = answer.text
                elif i == 2:
                    c = answer.text
                elif i == 3:
                    d = answer.text
                i += 1
            fcc_data.append({
                "question": q,
                "answers": [
                    a,
                    b,
                    c,
                    d
                ],
                "correct": -1
            })
    if foundCount == 30:
        thirtyCounter += 1
    else:
        thirtyCounter = 0
#    sleep(1)
    print(f'Found {foundCount} questions already in the file. {thirtyCounter} times 30 questions found in a row. Reglamentación. Preuntas totales: {len(fcc_data)}')
    with open('questionsNormativa.json', 'w') as fcc_file:
        json.dump(fcc_data, fcc_file, indent=4, ensure_ascii=False)