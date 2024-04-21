# Program to control Tuya Zigbee devices
This connects to Tuya cloud via API.
First requires Tuya cloud to link with the Smart Home app.
The zigbee and wifi devices are added to smart home app. 
Then export a tuya-raw.json file from Tuya Cloud with 
the device list.

There is another json file, tinytuya.json that stores the api
key and secret, and other configuration for accessing Tuya cloud. 
apiRegion is eu for my case, but I am located in Singapore.
apiDeviceID is not the same as the device id from the tuya-raw.json
it is a unique id that identifies the smart life app that linked
to my devices

<!-- tinytuya.json
{
    "apiKey": "xxx",
    "apiSecret": "xx",
    "apiRegion": "eu",
    "apiDeviceID": "xx"
} -->
