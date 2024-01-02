import json
from datetime import datetime

with open('result2.json', 'r', encoding='utf-8', errors='ignore') as file:
    data = json.load(file)  # Read the file as JSON

with open("_chat.txt", 'w', encoding="utf-8") as record:
    to_print = ""
  
    for message in data['messages']:
        if message['type'] == 'message':
            date = datetime.strptime(message['date'], '%Y-%m-%dT%H:%M:%S')
            formatted_date = date.strftime('%m/%d/%y, %H:%M:%S')
            formatted_text = message['text']
            file_ = message.get('file')
            photo_ = message.get('photo')

            if file_:
                try:
                    to_print += f"[{formatted_date}] {message['from']}: <attached: {message['file'].split('/')[1]}>" + "\n"
                except IndexError:
                    pass
            elif photo_:
                to_print += f"[{formatted_date}] {message['from']}: <attached: {message['photo'].split('/')[1]}>" + "\n"
            else:            
                if isinstance(formatted_text, list):
                    formatted_ = ""
                    for i in formatted_text:
                        if isinstance(i, dict):
                            t = i.get('text')
                            if t:
                                formatted_ += i['text'].strip()
                        else:
                            formatted_ += i.strip() 
                    to_print += f"[{formatted_date}] {message['from']}: {formatted_}" + "\n"

                else:
                    to_print += f"[{formatted_date}] {message['from']}: {formatted_text}" + "\n"

    record.write(to_print)
