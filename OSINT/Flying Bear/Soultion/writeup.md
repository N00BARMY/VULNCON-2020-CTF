## Name: Flying Bear
#### Description: 
`maniac` has given me this number `A25BF4`, and asked me to find the related address. I think one of his challenges has an answer to what this number could be!

Flag Format: vulncon{full_address_with_underscore_remove_comma}

#### Category: OSINT
#### Difficulty: Easy 
#### Author: D E V I N E R
---
## Solution:
This challenge is somewhat depended on **numb3r_m4gic**, A Miscellaneous challenge made by `maniac`. But you could have also solved this without the hint given by `numb3r_m4gic`'s Flag but, It would be a bit hard. 
Anyway the first one is recomended, i.e) Solve ***numb3r_m4gic***, Get the flag as well as the only hint to solve this epic challenge :)
So the Flag for CAPacity is: vulncon{JVXWIZJNKNPUQZLYMNXWIZI} decoding the content with *base32 decode* give us **"Mode-S_Hexcode"**
Now, You have a hex number which basically refers to [Mode-S Hexcode](https://en.wikipedia.org/wiki/Aviation_transponder_interrogation_modes)
Time to lookup for Mode-S Hexcode to get the exact address of the owner. 
Every Mode-s lookup tool available in Internet will prolly not give you what you want, so you must try 2-5 different lookup website :)
Finally you will get this website [Link](http://www.milradiocomms.com/search_mil_hexcodes.php?type_of_search=hex_search&sea)
Give it the number you have and Boom! 
![Image](https://i.imgur.com/UsRqEm8.png)
Make sure you copy and paste it exactly as it is!
Flag : vulncon{PO_BOX_699_ROSE_HILL_NC_284580699}
