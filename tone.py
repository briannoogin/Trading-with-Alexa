import requests
import json
 
def analyze_tone(text):
    username = 'acmprojectsalexa@gmail.com'
    password = 'Acmprojects1!'
    watsonUrl = 'https://gateway.watsonplatform.net/tone-analyzer/api'
    headers = {"content-type": "text/plain"}
    data = text
    try:
        r = requests.post(watsonUrl, auth=(username,password),
         data=data)
        return r.text
    except:
        return False
 
def welcome():
    message = "Welcome to the IBM Watson Tone Analyzer\n"
    print(message + "-" * len(message) + "\n")
    message = "How it works"
    print(message)
    message = "The service uses linguistic analysis to detect emotional cues"
    print(message)
    print()
    print("Have fun!\n")
 
def display_results(data):
    data = json.loads(str(data))
    print(data)
    for i in data['document_tone']['tone_categories']:
        print(i['category_name'])
        print("-" * len(i['category_name']))
        for j in i['tones']:
            print(j['tone_name'].ljust(20),(str(round(j['score'] * 100,1)) + "%"		).rjust(10))
        print()
    print()
 
def main():
    welcome()
     
    data = input("Enter some text to be analyzed for tone analysis by IBM Watson	 (Q to quit):\n")
    if len(data) >= 1:
        if data == 'q'.lower():
            exit
        results = analyze_tone(data)
        if results != False:
            display_results(results)
            exit
        else:
            print("Something went wrong")
 
main()
