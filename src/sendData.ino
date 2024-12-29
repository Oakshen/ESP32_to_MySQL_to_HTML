#include <WiFi.h>
#include <WiFiClient.h>
#include <Wire.h>

const char *ssid = "xxxxxx";
const char *password = "xxxxxxx";

const char *host = "你的服务器地址";//注意是公网地址
const int port = your_port;

int lasti = 0;//从串口接受来的数据

void setup()
{
    Serial.begin(115200);
    Serial.print("connecting to");
    Serial.println(ssid);
    WiFi.begin(ssid, password);

    //判断WiFi是否连接成功
    while (WiFi.status() != WL_CONNECTED)
    {
        delay(500);
        Serial.print(".");
    }
    Serial.println("");
    Serial.println("WiFi connected with IP address:");
    Serial.println(WiFi.localIP());
}

void loop()
{
    String Load_status="YYNNNNY";//定义的七个用电器状态，Y表示开启，N表示关闭
    delay(1000);
    Serial.print("connecting to");
    Serial.print(host);

    WiFiClient client; 
    //判断是否连接上服务器
    if (!client.connect(host, port))
    {
        Serial.println("connection failed");
        return;
    }
    client.print(Load_status); //发送数据
}
