## Name: The Watcher
#### Description: 
It was a cold winter night `tim3zapper` got a sudden message from his boss. `tim3zapper` has been asked to get the mail id of a famous photographer who will be invited for the airline event oraganized by example.com. Can you help `tim3zapper` with that?

#### Category: OSINT
#### Difficulty: Hard 
#### Author: D E V I N E R
---
## Solution:
As per the description our goal is to get the mail id of a famous photographer who will join the airline event, We can asume that the person we are talking about is a famous photographer and mostly deals with airline photos.
We are also given an username `tim3zapper`, It's quite basic to search for twitter first. 
Just a quick search will give you this user's twitter account. 
![Image](https://i.imgur.com/CR5GXLU.png)
Now, If you go through his tweets thoroughly, We will observe these details:
![Image](https://i.imgur.com/7NF6Uru.png)
- Someone is trying to attack him. 
- The logs says, The attacker is a creator and he is talking about network

We can't figure out anything till this point, But if we check other tweets. We get this
![Image](https://i.imgur.com/qtdNK0b.png)

He is talking about backups, and one/more of his tweets are deleted. But, The interesting thing to notice is, He has mentioned about being a **`Sic Mundus`** aka Traveller as per a popular web series named **DARK** [Go through This website](https://dark-netflix.fandom.com/wiki/Sic_Mundus)
Link the two things we got as of now, Deleted and Traveller! What could it be? Time traveller? Yes it is, It's talking about web archives (Easy Peasyy) 
Well, We got a snapshot for it!
![Image](https://i.imgur.com/7OGRgK8.png)

If you check that out, You can see there is an extra tweet which was deleted before.
![Image](https://i.imgur.com/e4kIY2I.png)
What we got now?
- Another username `sullyth3h4x0r` 
- If you want to hire him , Then contact his friend `lmao`

We have an username but we really don't know what to do with it! You can do many things, But i will stick to the intended way of solving this Challenge. If you remember, We got to know that The attcker was a `creator` and he was attacking the `network` and also we got a username. 
So if we try to put those two words together, We can think of [Ello.com](https://ello.co/) as it is also known as **"The Creators Network"** [You can also use unsername search tools like `sherlock`]

Now, we got the ello account of user [sullyth3h4x0r](https://ello.co/sullyth3h4x0r)
![Image](https://i.imgur.com/N38anTb.png)

This user has posted two pictures and one of the pictures's description says it all :)
![Image](https://i.imgur.com/2d7mNHx.jpg)
Do a reverse image search and you will get the Photographer name i.e) **Agustin Anaya** but you won't actually get the mail id from that website. So you need to **TRY HARDER!**

![Image](https://i.imgur.com/zKN9dAV.jpg)
Boom! We got `lmao`'s username, Again do the same! Guess or use sherlock to get this user's account!

You will further get the insta account by this username `tjake_lmao` and we are said, this guy will give us strong hint to solve this challenge!
![Image](https://i.imgur.com/SmJMtwx.png)
We get a mail id, Other than this! There are many rabit holes present in this insta account, Don't fall for it! I Repeat, Don't fall for it!

Remember, There was a tweet mentioning about `lmao` ? If we need to contact The 1337 h4x0r we need to contact `lmao` ?
What are you waiting for? Mail him and see what he gives you! 
![Image](https://i.imgur.com/SRB4Ik4.png)
If you mail him anything, he will revert back with the above mail giving you a strong Hint **"Just jumped off runway 26L"** 
Now, If you give a simple google search **`"Agustin Anaya Just jumped off runway 26L"`** 
![Image](https://i.imgur.com/kkLWpt3.png)
Link for the above picture, http://www.dutchops.com/photo_big.asp?id=967
![Image](https://i.imgur.com/Af2iNcN.png)
Hover over `Contact Photographer` and you will get the Mail Id of **Agustin Anaya**

Flag: vulncon{m.venema@dutchops.com}


