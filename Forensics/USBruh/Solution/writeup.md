# WRITEUP - USBruh

### Step 1 : Tool Installation
**usbrip** is a simple forensics tool with command line interface that lets you keep track of USB device artifacts (i.e., USB event history) on UNIX machines.

**Installation** :
```sh
$ git clone https://github.com/snovvcrash/usbrip
```
or 
```sh
$ pip install sudo -H python3 -m pip install --upgrade usbrip
```


### Step 2 : Tool Usage

Run to get list of passable args :
```sh
$ sudo usbrip --help
```

Run to get **Events** which come under **Violations** Banner :

```sh
$ sudo usbrip events violations manf-details.json --file ./system.log
```


### Step 3 : Analyzing/Output
After the Analyzing is done, prompt appears asking **Output** type, Select
* **Terminal stdout (standard output)**

##### 1 - Event Violations Output Table : 
![violations](https://i.postimg.cc/L698sQvT/violations.png)

##### 2 - Analyzing Violations :
**Serial Number(s)** are **MD5 Hash(s)**
Reverse **MD5** to get **plain text**. 

* 6864f389d9876436bc8778ff071d1b6c - **my**
* df53ca268240ca76670c8566ee54568a - **computer**
* f58e6a506c76fc2c90a7d29cbc631c2f - **dead**

### Flag :
Do not forget format the flag by adding underscore(s) **_** in-between the words.

**Flag : vulncon{my_computer_dead}**
