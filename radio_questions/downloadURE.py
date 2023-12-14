from calendar import c
from time import sleep
from bs4 import BeautifulSoup
import requests
import json
from datetime import datetime

giturl = 'https://raw.githubusercontent.com/aruznieto/data.api.anrn.dev/main/radio_questions'

with open('questionsElectricidad.json', 'r') as fcc_file:
    fcc_data = json.load(fcc_file)

thirtyCounter = 0
#file = open('questions.json', 'w')
while thirtyCounter < 50:
    # URL of the page to be scraped
    url = 'https://www.ure.es/examenes/electricidad-y-radioelectricidad/'
    text = requests.get(url).text
    soup = BeautifulSoup(text, 'html.parser')
    questions = soup.find_all('div', class_="quiz-question")
    foundCount = 0
    for question in questions:
        imagQ = question.find_all('div', class_="quiz-question-image-holder")
        imagA = question.find_all('div', class_="quiz-question-answer-image-holder")
        q = question.find_all('div', class_="quiz-question-title")[0].text
        q = q.replace('"', "'").replace('\n', '').replace('\r', '').replace('\t', '').replace("                ", "").replace("            ", "")

        found = False
        for que in fcc_data:
            if que['question'] == q:
                if ('questionImage' not in que) or (que['questionImage'] == ''):
                    if len(imagQ) > 0:
                        date = datetime.now().timestamp()
                        path = f'imagesElectricidad/{date}.png'
                        with open(f'./{path}', 'wb') as handler:
                            img_data = requests.get(imagQ[0].find_all('img')[0]['data-src']).content
                            handler.write(img_data)
                        que['questionImage'] = f'{giturl}/{path}'
                if ('answerImage' not in que) or (len(que['answerImage']) == 0):
                    if len(imagA) > 0:
                        que['answerImage'] = []
                        for i in range(len(imagA)):
                            date = datetime.now().timestamp()
                            path = f'imagesElectricidad/{date}.png'
                            with open(f'./{path}', 'wb') as handler:
                                img_data = requests.get(imagA[i].find_all('img')[0]['data-src']).content
                                handler.write(img_data)
                            que['answerImage'].append(f'{giturl}/{path}')
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
while thirtyCounter < 50:
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
                if len(imagQ) > 0:
                    date = datetime.now().timestamp()
                    path = f'imagesNormativa/{date}.png'
                    with open(f'./{path}', 'wb') as handler:
                        img_data = requests.get(imagQ[0].find_all('img')[0]['data-src']).content
                        handler.write(img_data)
                    que['questionImage'] = f'{giturl}/{path}'
                if len(imagA) > 0:
                    que['answerImage'] = []
                    for i in range(len(imagA)):
                        date = datetime.now().timestamp()
                        path = f'imagesNormativa/{date}.png'
                        with open(f'./{path}', 'wb') as handler:
                            img_data = requests.get(imagA[i].find_all('img')[0]['data-src']).content
                            handler.write(img_data)
                        que['answerImage'].append(f'{giturl}/{path}')
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