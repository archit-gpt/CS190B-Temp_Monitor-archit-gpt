Project: Make a device that sends an alert to your phone when the temperature is outside of a certain range. This is intended for applications such as monitoring the temperature of one’s fridge for food regulation purposes, or perhaps maintaining the internal temperature of one’s household on a seasonal basis.\

Details:\
Uses raspberry pi\
Thermometer\
Sends text (Clicksend SMS API)\
Hardware components:\
Raspberry Pi\
Temperature Sensor\
Wi-Fi module \
Software components:\
Python\
External libraries:\
RPi.GPIO\
Requests\
PyOWM (OpenWeatherMap API)\

Implementation Plan:\
Connect the temperature sensor to the Raspberry Pi.\
Write Python code to read the temperature data from the sensor\
If the temperature is outside of a certain range specified by the user, send the user a text alert\
The alert can be sent using an API call, which can be set up to send a notification to your phone (Clicksend SMS API)
