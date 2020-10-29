
user will be provided with a link and a description. 
```
https://mega.nz/file/C1Q0XR5a#Er4g7Tu4QVAHjSluTsOHX_xlZCPgdSMinw5cg0KR0qA
Desc:
Sometimes it is good to check  Least Significant Bit for hidden data ?
```
# Solution 

Download the file , it is a  wav file .

It is said that LSB has hidden data so that we can extract data from this code.
```
import wave
song = wave.open("audio.wav", mode='rb')
# Convert audio to byte array
frame_bytes = bytearray(list(song.readframes(song.getnframes())))

# Extract the LSB of each byte
extracted = [frame_bytes[i] & 1 for i in range(len(frame_bytes))]
# Convert byte array back to string
string = "".join(chr(int("".join(map(str,extracted[i:i+8])),2)) for i in range(0,len(extracted),8))
# Cut off at the filler characters
decoded = string.split("###")[0]

# Print the extracted text
print("Sucessfully decoded: "+decoded)
song.close()
```
After running the python script we get a mega link.
![image](https://i.imgur.com/hotF1br.png)

link:https://mega.nz/file/7oYC0RzZ#YlDr9jiF7tL8lhLdXpc8hOen21fhm8DoaOoNaeUWbTw

After downloading we got a zip file.

After unzipping their are many file , and all are encrypted.
By listing hidden directory , we got a misc file.
![image](https://i.imgur.com/PrVfZxt.png)


After searching for encfs encryption and how to bruteforce to get password using john , i got the commands.
![image](https://i.imgur.com/tnogq39.png)

commands: 
```
/usr/share/john/encfs2john.py file > pass
john --wordlist=/usr/share/wordlists/rockyou.txt pass
john --show pass
```
password:sarah

Let decrypt the files:

![image](https://i.imgur.com/PAFizZy.png)


```
encfs /file  /decrypt;
```
![image](https://i.imgur.com/JLOSazu.png)

It has many files , so lets grep all the files in  a txt file and search for vulncon flag.

![image](https://i.imgur.com/i5gTXMu.png)

```
grep -R . > ../vuln.txt
cat  vuln.txt  | grep vulncon
```

Flag:vulncon{4Lw4Y5_PU75_3nCRyp710N_wH1l3_5H4R1NG_F1L3}



