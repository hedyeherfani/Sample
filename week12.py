# Hedyeh Erfani
# Final project
# 05/30/20

import requests


def fetch_data(zip=None, city=None):
    baseUrl = "http://api.openweathermap.org/data/2.5/weather"
    apiid = "7c89b2d25149a9c0c65de991a2f3e506"

    # Gives the user the option of receiving weather from zip code or city name
    if zip is not None:
        baseUrl += "?zip=" + str(zip)
    else:
        baseUrl += "?q=" + str(city)

    # Appends the api id and formats the temperature unit as Fahrenheit

    baseUrl += "&appid=" + str(apiid) + "&units=imperial"
    r = requests.get(baseUrl)
    return r


def showResult(resp):
    # User has entered appropriate response/no errors happened, program will display the weather forecast
    if resp.status_code == 200:
        data = resp.json()
        print(data['name'])
        print(f"""{data['name']} Weather Forecast:
        The current temperature is {data['main']['temp']} degrees.
        There will be {data['weather'][0]['description']} with wind speed of {data['wind']['speed']} m/s. 
        The pressure is {data['main']['pressure']} hPA.  
        The humidity is {data['main']['humidity']}%.
        Minimum Temp will be {data['main']['temp_min']} degrees and maximum temp will be {data['main']['temp_max']} degrees.

        """)
    # User did not enter an appropriate response/an error happened
    else:
        print("The request has failed, please try again Error Code : ", resp.status_code)


def main():
    while True:

        # Display choices for the user
        option = int(input("Your options :\n1. Enter Zip Code\n2. Enter City Name\n3. Exit\n"))

        # Get zip code from the user for the weather forecast
        if option == 1:

            try:
                queryData = int(input("Please enter your zip code : "))
                resp = fetch_data(queryData, None)
                showResult(resp)
            except Exception as ex:
                print("Error : ", ex)

        # Give the user the weather forecast based on their city
        elif option == 2:
            try:
                queryData = input("Enter city name : ")
                resp = fetch_data(None, queryData)
                showResult(resp)
            except Exception as ex:
                print("Error : ", ex)

        # Exit the program
        elif option == 3:
            break
        else:
            print("Your choice is not valid, try again some other time. \n")


if __name__ == "__main__":
    main()
