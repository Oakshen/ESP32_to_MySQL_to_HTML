# ESP32 物联网控制系统

[English](README.md) | [中文](#项目概述)

## 项目概述

一个通过 MySQL 数据库将 ESP32 连接到网页界面的智能家居控制系统。

### 系统组件

- ESP32 微控制器
- 带 MySQL 和 PHP 的 Web 服务器
- HTML 网页界面

### 文件结构

```tree
.
├── src/
│   ├── sendData.ino    # ESP32 程序代码
│   ├── recvData.py     # 服务器端数据接收器
│   └── readMySQL.php   # 数据查询接口
└── html/
    └── test.html       # Web 控制界面
```

### 项目说明

这是一个小项目，将 `src` 文件夹中的 `sendData.ino` 部署在 ESP32 上。ESP32 将数据发送到服务器，服务器上部署了 `recvData.py` 来接收数据并存储在 MySQL 数据库中。HTML 网页源码调用 `readMySQL.php` 文件来改变 HTML 中的显示状态。

### 项目结构

- `src/sendData.ino`：部署在 ESP32 上的 Arduino 程序
- `src/recvData.py`：部署在服务器上的 Python 脚本，用于接收数据并存储在 MySQL 中
- `src/readMySQL.php`：由 HTML 网页调用的 PHP 脚本，用于从 MySQL 读取数据并更新显示

### 设置说明

1. **ESP32 设置**：
    - 在 Arduino IDE 中打开 `sendData.ino`
    - 配置 WiFi 凭证和服务器详细信息
    - 将程序上传到 ESP32

2. **服务器设置**：
    - 确保服务器上安装了 Python 和 MySQL
    - 运行 `recvData.py` 以开始监听传入数据
    - 将 `readMySQL.php` 放置在 Web 服务器的根目录中

3. **网页设置**：
    - 确保 Web 服务器配置为运行 PHP
    - 将 HTML 文件放置在 Web 服务器的根目录中
    - 访问网页以查看状态更新