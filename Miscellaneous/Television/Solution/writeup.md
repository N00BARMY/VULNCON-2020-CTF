user will be provided with link.
```
https://mega.nz/file/UKYW1bLb#bA-qnL2D55GNlxjNNTlZ7TJgEY2mKBdiLbDL6yAPmwg
```
and this desc:

```
Crypton asked Rachel to send files using best encryption ever, But she an amateur radio operator she used ... method for picture transmission. In Result she got fired , Sed Life.
```

# Solution 

Lets download the file and lets see what is in that.

![image](https://i.imgur.com/tK2uCkt.png)


It has 1268 wav file. So lets combine it with the folowing script. You have to put all the wav file in a output folder and run this script outside that folder.

```
def merge():
    mergedFile = AudioSegment.empty()
    for i in range(1,1269):
        print(f'adding {i}')
        mergedFile += AudioSegment.from_wav(f'output/{i}.wav')
    mergedFile.export('merged.wav', format='wav')

#split()
merge()
```

It will merge all the wav file into one wav file. Lets play it .

In 14.19 it started giving unpleasent sound , lets read the description.It says the amateur radio operator used method for picture transmission. Lets search on google.

![image](https://i.imgur.com/S2ojJ5m.png)

we will get search result as slow scan television.
Lets search for sstv decoder on google.

We can decode it using Robot36 application on our phones.

![image](https://i.imgur.com/Z1oXZ6N.png)


Lets try to play the audio from 14.10 and try to decode it with robot36.

![image](https://i.imgur.com/g5wP8Aa.png)

vulncon{NothiN9_goe5_In_V4iN}


