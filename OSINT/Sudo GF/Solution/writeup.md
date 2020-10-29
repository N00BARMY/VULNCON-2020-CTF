## Name: Sudo GF
#### Description: 
Hey mate, We have got intel that `r3curs1v3_pr0xy's` pseudo girlfriend is no more Anonymous. We also came to know that `r3curs1v3_pr0xy` has been running a secret Automotive company and her GF `Sabia` has been dealing with most of his company's operation. Our Agents have also informed us that she has completed her graduation from `University of Groningen`. Anyways, `Sabia` has been assigned to carry on this operation and you will get your flag from her. Good Luck Champ!!

#### Category: OSINT
#### Difficulty: Medium 
#### Author: D E V I N E R
---
## Solution:
What we have got so far? 
From the challenge description we came to know these points:
- Someone named `Sabia`, We don't know what is her Last name anyway :(
- `Sabia` is graduated from `University of Groningen`
- The company we are talking about is an **Automotive Company**
- Last but not the least, **r3curs1v3_pr0xy** has a GF, and that's NOT IMPORTANT. [We Don't Care]

As we are dealing with a *Company* so prolly something has to do with [LinkedIn](linkedin.com)
Id we use this keyword `"sabia University of Groningen"` in LinkedIn, We get a user from **Rotterdam, South Holland, Netherlands**
![Image](https://i.imgur.com/urGsFSg.png)
She is working in a comapny named `Avratra` which is indeed an Automotive Company. 
Further recon will lead you to her [Github](https://github.com/0x9710sabia) :)
Only 3 repo, And you won't get anything in the commits. But, there is a repo named `public-gist` and it has a wiki page.
![Image](https://i.imgur.com/hOdhrJg.png)

So, Sabia loves gist and git both. I thought her only love is `r3curs1v3_pr0xy` LMAO
Jokes Apart, We also got her hex encoded pass `xcVVtmsZpV`, But we don't know where to use it :(
Check all her gists. We got this interestinng stuff.
![Image](https://i.imgur.com/fN2n1Xk.png)
The last point is interesting, Check if you can do something with that. Moreover we can also see a comment saying **"secret_key.pub is still public :("**
We can do something with that, Let's go for it!
![Image](https://i.imgur.com/PYZP49O.png)
We got the `secret_key` but something is redacted from it. The domain name!
Check it's Revisions and Boom!
![Image](https://i.imgur.com/ZRs7yDk.png)

Now we know this key has been generated from [Keybase.io](https://keybase.io/)
Now, let's try to decode the PGP key and see what we get!
I am using this online [decoder](https://cirw.in/gpg-decoder/) to decode the PGP key.
![Image](https://i.imgur.com/eJqB0jz.png)
We got the KeyId, Let's head over to keybase and see who generated this key and what we get from there :)
BOOM!! We got a user again `sabiaafk`
![Image](https://i.imgur.com/nekkjqW.png)

Yeah, She is `Sabia` again, `r3curs1v3_pr0xy's` GF and she has something in her BIO
![Image](https://i.imgur.com/QbMuP5f.png)

okay again we got a random text but if we read it again and again, we can assume that maybe it has something to do with pastebin.
Let's go to this link: https://pastebin.com/YTrc68ub
But, It is pass protected. Remember we got a password from wiki page? Try that?? Oh Yeaah!

Got the flag xD

Flag: vulncon{k3ybase_&_g1thub_pgp_4r3_d3adly_c0mb0}
```
WARNING: That beautiful lady doesn't exist! So don't fall for her, that picture was taken from https://thispersondoesnotexist.com/
```
