# Program to control Tuya Zigbee devices
## Connects to Tuya cloud API
## Requires Tuya cloud to link with Apps like Smart Home
## First export a tuya-raw file from Tuya Cloud with 
## device list

## Then get the api key and secret from Tuya cloud
## and set it inside the tinytua.json file
## apiRegion is eu for my case, but I am located in Singapore
## apiDeviceID is not the same as the device id from the tuya-raw.json
## it is a unique id that identifies the app that I linked my devices ## to I guess

<!-- tinytuya.json
{
    "apiKey": "xxx",
    "apiSecret": "xx",
    "apiRegion": "eu",
    "apiDeviceID": "xx"
} -->