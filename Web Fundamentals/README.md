# Web Fundamentals

## TASK 5-Mini ctf

---
## Making HTTP requests

You can make HTTP requests in many ways, including without browsers! For CTFs, you'll sometimes need to use cURL or a programming language as this allows you to automate repetitive tasks.

## Intro to curl

Curl is a tool to transfer data from or to a server, using one of the supported protocols (DICT, FILE, FTP, FTPS, GOPHER, HTTP, HTTPS, IMAP, IMAPS, LDAP, LDAPS, MQTT, POP3, POP3S, RTMP, RTMPS, RTSP, SCP, SFTP, SMB, SMBS, SMTP, SMTPS, TELNET and TFTP). The command is designed to work without user interaction.

Curl offers a busload of useful tricks like proxy support, user authentication, FTP upload, HTTP post, SSL connections, cookies, file transfer resume, Metalink, and more.We will be using curl command here, if any doubts use **curl --help**.

---

### 1.What's the GET flag?

The best way to do this is simply make GET request to the web server with path /ctf/get.

```
curl http://<ip>:8081/ctf/get
```
![image](https://miro.medium.com/max/614/1*o7-cNPcl5ZEIl2hEZklnHw.png)

### 2.What's the POST flag?
```
curl http://<ip>:8081/ctf/post -X POST -d "flag_please"
```

### 3.What’s the “Get a cookie” flag?

This can also be done in your browser by devlopers tools or simply press F12.If you are using firefox the cookies should be in storage tab.

```
curl http://<ip>:8081/ctf/getcookie -c cookielist.txt
```
![image](https://miro.medium.com/max/700/1*ZTPEN0HnCRAlF5cPRDkAYA.png)

### 4.What's the "Set a cookie" flag?

```
curl http://<ip>:8081/ctf/sendcookie --cookie flagpls=flagpls
```

Another way of doing this by devlopers tool.Set a cookie with name "flagpls" and value "flagpls" in your devtools and make a GET request to /ctf/sendcookie.

![image](https://miro.medium.com/max/700/1*hQITVjGU49VXceKFmtL1jg.png)



