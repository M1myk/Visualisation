import eel
import pyowm


owm = pyowm.OWM("454099604a84745f8218dae3b0a5bf36")


@eel.expose
def get_weather(place):
    mgr = owm.weather_manager()

    observation = mgr.weather_at_place(city)
    w = observation.weather

    temp = w.temperature('celsius')['temp']

    return " В місті " + city + " зараз " + str(temp) + " градусів!"
eel.init("web")
eel.start("main.html", size=(700, 700))
