## Name: Punishment
#### Description: 
Mr.BEAN was working on his school assignment, But unfortunately, his Lil Sister deleted that assignment file. As Mr.BEAN failed to submit the assignment on time, He will be punished heavily. Anyway, He has an exclusive excuse, but he needs to prove his innocence anyhow! Can you extract the date/time his assignment was deleted? 

Flag Format: vulncon{yyyy/mm/dd_hh:mm:ss_UTC}

#### Category: Forensics
#### Difficulty: Hard 
#### Author: D E V I N E R
#### Given file: [Link]()
---
## Solution:
As per the description given we came to know that the challenge is revolving around a deleted file (Whaterver the file maybe). We also got a file with lots of hex data.
Go to this [link](https://tomeko.net/online_tools/hex_to_file.php?lang=en)
Paste the hex you got and convert it to file, You can now use `file` command to see what type of file it is. 
As it is a zip file we need to convert it to `.zip` extension.
Extracting it will give you a file named `$I4A67FE.docx`, It is quite unusuall to see a filename starting with **$**
On further research we will come across a research paper stating **"$I Parse"** [Link](https://df-stream.com/recycle-bin-i-parser/)

Going through that research paper, We need to download the tool in windows and load the file , This will give us the time, date and min when the file was deleted. Cool isn't it??

Flag: vulncon{2020/11/04_21:01:14_UTC}
