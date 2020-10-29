## Name: PollMor
#### Description: 
Morphy wanted to study about "Index of coincidence" so she went to `Dcode University` 
near searchbar Playstation. Professor PollMor gave her a critical assignment to complete before VULNCON CTF ends. Help Her to complete the assignment and get the flag :)

Flag Format: vulncon{words_seperated_by_underscore}

#### Category: Crypto
#### Difficulty: Easy 
#### Author: D E V I N E R
#### Given file: [Link]()
---
## Solution:
We need to focus on three things here, 
1. Index Of Coincidence
2. Dcode University (https://www.dcode.fr/)
3. Details given in the [cipher.txt]() file, i.e) '-', '.', ' ' (Basically represents morse code)

The given cipher text is something like this 
```
VEXCH881U3JPMLWO6TQ4MH5G5LNVUXGN86GWR1NZ8CA82AW7MLAY4UJ3E4K38335UBAUCQY6N4SJJ1RR6VBYSAOP9P9XBI35XSEPM4GHGFY39AWE9BJTBGZW93Q3Y2Y374JDFRF9AFE
```
With the details we have and some further investigation on what maybe the cipher is we come to know that this cipher is maybe [pollux cipher](https://www.dcode.fr/chiffre-pollux) 
We know the challenge name starts with **poll** and it must have something to do with *Coincidence Index* 
So, If we have a look at Pollux Cipher we came to know that `"A message encrypted with Pollux will have a minimum coincidence index"`

![Image](https://i.imgur.com/HJrOtUF.png)
Moreover, We can see we have some substitutions that we can use to decode it and we are given those values in [cipher.txt]() as well.
Putting everything on it's place gives us the flag :)
![Image](https://i.imgur.com/DaJt6is.png)

Flag: vulncon{P0llux_4nd_M0rse_ar3_br0th3rs}
