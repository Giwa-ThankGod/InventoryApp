import requests

BASE_URL = 'https://text-translator2.p.rapidapi.com'
headers = {
	"content-type": "application/x-www-form-urlencoded",
	"X-RapidAPI-Key": "ed9d133ce5msheed192e1aaa3916p1e1ec4jsn6f2154264862",
	"X-RapidAPI-Host": "text-translator2.p.rapidapi.com"
}

def getLanguages(language_type):
    url = f"{BASE_URL}/getLanguages"
    response = requests.get(url=url, headers=headers)
    languages = response.json()['data']['languages']

    for language in languages:
        if language['name'] == language_type.title():
            return language['code']
        

def translate(source, target, text):
    url = f"{BASE_URL}/translate"

    payload = {
        "source_language": source,
        "target_language": target,
        "text": text
    }

    response = requests.post(url, data=payload, headers=headers)

    return response.json()['data']['translatedText']

def main():
    print("-------------------------------------WELCOME TO FOLAN LANGUAGE TRANSLATOR ----------------------------------")
    
    source_language = input('Enter source language: ')
    target_language = input('Enter target language: ')
    text = input('Enter text: ')

    source_language = getLanguages(source_language)
    target_language = getLanguages(target_language)

    # print(source_language, target_language)

    translated_text = translate(source_language, target_language, text)

    print(f'text: {text}')
    print(f'translated_text: {translated_text}')


if __name__ == '__main__':
    main()
