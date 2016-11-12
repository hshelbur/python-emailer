import requests

def get_emails():
    emails = {}

    try:
        email_file = open('emails.txt', 'r')

        for line in email_file:
            (email, name) = line.split(',')
            emails[email] = name.strip()
            
    except FileNotFoundError as err:
        print(err)

    return emails

def get_greeting():

    try:
        greeting_file = open('email_body.txt', 'r')

        greeting = greeting_file.read()

    except FileNotFoundError as err:
        print(err)

    return greeting



def get_weather_forecast():
    url = 'http://api.openweathermap.org/data/2.5/weather?q=ChapelHill,nc&units=imperial&appid=1e27bc4aba797f72503f9b125be36e4b'
    weather_request = requests.get(url)
    weather_json = weather_request.json()


    description = weather_json['weather'][0]['description']
    temp_max = weather_json['main']['temp_max']
    temp_min = weather_json['main']['temp_min']

    print(description)
    print(temp_min)
    print(temp_max)

def main():
    emails = get_emails()
    print(emails)

    greeting = get_greeting()
    print(greeting)

    get_weather_forecast()



main()
