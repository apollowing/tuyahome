#!/usr/bin/env python
# -*- coding: utf-8 -*-
import tinytuya
import argparse
import json

TUYA_CONFIG = r'tinytuya.json'
TUYA_RAW = r'tuya-raw.json'

def get_deviceid(name):
         # Open the JSON file in read mode
    with open(TUYA_RAW, 'r') as file:
        tuya_raw = json.load(file)

    for device in tuya_raw['result']:
        if device['name'] == 'Ceiling fan':
            id = device['id']
            print(id)


def get_args():
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--device_name",
        type=str,
        default='Zac Fan',
    )
    parser.add_argument(
        '--switch',
        type=int,
        default=1,
    )

    parser.add_argument(
        '--fan_speed',
        type=int,
        default=2,
    )


    args = parser.parse_args()

    return args


def main():
    # 引数解析 #################################################################
    args = get_args()
    device_name = args.device_name
    switch = args.switch
    fan_speed = args.fan_speed

    # Open the JSON file in read mode
    with open(TUYA_CONFIG, 'r') as file:
        config = json.load(file)

    tuya_link = tinytuya.Cloud(
            apiRegion=config["apiRegion"], 
            apiKey=config["apiKey"], 
            apiSecret=config["apiSecret"], 
            apiDeviceID=config["apiDeviceID"])

    # Open the JSON file in read mode
    with open(TUYA_RAW, 'r') as file:
        tuya_raw = json.load(file)

    print(config)
    
    print(f"Looking for device name : {device_name}")
    # print("raw tuya devices: ", tuya_raw['result'])

    device_def = [device for device in tuya_raw['result'] if device['name'] == device_name]
    print(device_def)

    if len(device_def) == 0:
        print("Device not found")
        return

    commands = {
        "commands": [
            { "code": "switch", "value": False if switch == 0 else True},
                {
                    "code": "fan_speed",
                    "value": fan_speed
                },

        ]
    }


    tuya_link.sendcommand(device_def[0]['id'], commands)


if __name__ == '__main__':
    main()
