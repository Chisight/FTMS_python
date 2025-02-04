# Dictionary to hold characteristic descriptions
characteristic_descriptions = {
    "00002a05-0000-1000-8000-00805f9b34fb": "Service Changed/Alert",
    "00002a23-0000-1000-8000-00805f9b34fb": "System ID",
    "00002a24-0000-1000-8000-00805f9b34fb": "Model Number String",
    "00002a25-0000-1000-8000-00805f9b34fb": "Serial Number String",
    "00002a26-0000-1000-8000-00805f9b34fb": "Firmware Revision String",
    "00002a27-0000-1000-8000-00805f9b34fb": "Hardware Revision String",
    "00002a28-0000-1000-8000-00805f9b34fb": "Software Revision String",
    "00002a29-0000-1000-8000-00805f9b34fb": "Manufacturer Name String",
    "00002a50-0000-1000-8000-00805f9b34fb": "PnP ID",
    "00002acc-0000-1000-8000-00805f9b34fb": "Fitness Machine Feature", #duplicates flags from Treadmill Data
    "00002acd-0000-1000-8000-00805f9b34fb": "Treadmill Data",
    "00002ad3-0000-1000-8000-00805f9b34fb": "Training Status", #bytearray(b'\x00\x0d') while not paused/Quick Start, bytearray(b'\x00\x0e') during countdown to start/Pre-Workout, bytearray(b'\x00\x0f') while stopping/Post-Workout, bytearray(b'\x00\x01') when paused/idle. (value no difference between off and running, both show not paused, look at Treadmill Data instantaneousSpeed to differentiate)
    "00002ad4-0000-1000-8000-00805f9b34fb": "Supported Speed Range",
    "00002ad5-0000-1000-8000-00805f9b34fb": "Supported Inclination Range",
    "00002ad7-0000-1000-8000-00805f9b34fb": "Supported Heart Rate Range",
    "00002ad9-0000-1000-8000-00805f9b34fb": "Fitness Machine Control Point",
    "00002ada-0000-1000-8000-00805f9b34fb": "Fitness Machine Status",
    "d18d2c10-c44c-11e8-a355-529269fb1459": "YpooMiniProControlPointId",
    "0000fff4-0000-1000-8000-00805f9b34fb": "custom service UUID",
    "0000fff1-0000-1000-8000-00805f9b34fb": "custom service UUID",
    "0000fff2-0000-1000-8000-00805f9b34fb": "custom service UUID", #sending 01,00 runs motor full tilt
    "0000fff3-0000-1000-8000-00805f9b34fb": "custom service UUID",
    "02f00000-0000-0000-0000-00000000ff01": "custom service UUID",
    "02f00000-0000-0000-0000-00000000ff02": "custom service UUID",
    "02f00000-0000-0000-0000-00000000ff03": "custom service UUID",
    "02f00000-0000-0000-0000-00000000ff00": "custom service UUID",

}

FitnessMachineControlPoint = "00002ad9-0000-1000-8000-00805f9b34fb"
TrainingStatus = "00002ad3-0000-1000-8000-00805f9b34fb"
TreadmillData = "00002acd-0000-1000-8000-00805f9b34fb"
