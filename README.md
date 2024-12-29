# ESP32 IoT Control System

[English](#english) | [中文](README_CN.md)

## Project Overview
You can visit this [URL](https://blog.csdn.net/weixin_44002696/article/details/124502124) for more content
A smart home control system that connects ESP32 to a web interface through MySQL database.

### Components

- ESP32 microcontroller
- Web server with MySQL & PHP
- HTML web interface

### File Structure

```tree
.
├── src/
│   ├── sendData.ino    # ESP32 code
│   ├── recvData.py     # Server-side data receiver
│   └── readMySQL.php   # Data query interface
└── html/
    └── test.html       # Web control interface
```

## English

### Project Overview

This is a small project that involves deploying `sendData.ino` from the `src` folder on an ESP32. The ESP32 sends data to a server where `recvData.py` is deployed to receive the data and store it in a MySQL database. The `readMySQL.php` file is called by the HTML web page to change the display status in the HTML.

### Project Structure

- `src/sendData.ino`: Arduino sketch to be deployed on ESP32
- `src/recvData.py`: Python script to be deployed on the server to receive data and store it in MySQL
- `src/readMySQL.php`: PHP script called by the HTML web page to read data from MySQL and update the display

### Setup Instructions

1. **ESP32 Setup**:
    - Open `sendData.ino` in the Arduino IDE
    - Configure the WiFi credentials and server details
    - Upload the sketch to the ESP32

2. **Server Setup**:
    - Ensure Python and MySQL are installed on the server
    - Run `recvData.py` to start listening for incoming data
    - Place `readMySQL.php` in the web server's root directory

3. **Web Page Setup**:
    - Ensure the web server is configured to run PHP
    - Place the HTML files in the web server's root directory
    - Access the web page to see the status updates

---
