# WRITEUP - Twerk it ak

### Step 1 : Fix File Header

  *  Use a **HEX Editor** and change file Header from **EXE to PNG** (you can see the HEX data says **Photoshop**, makes it obvious it's not a **EXE**).

  * Save as a **.png** file.


### Step 2 : Install TweakPNG

Let's Install **TweakPNG** (You can use any similar tool that lets you edit Image Data Chunks).
- **TweakPNG** is a low-level utility for examining and modifying PNG image files. http://entropymine.com/jason/tweakpng/


### Step 2 : Using TweakPNG

##### 1 - Import the Image File : 
 Goto **File** > **Open** > **Select Image**.
![Step 1](https://i.postimg.cc/y6GNp8vq/Step-1.png)

##### 2 - Analyze and Edit the Image :
You can see **6** different Data Chunks, after the file is analyzed.
The **pHYs** Chunk (google it's definition) says **2837x2837 pixels**.
![Step 1](https://i.postimg.cc/y6GNp8vq/Step-1.png)

Intresting when **IHDR** Chunk shows **1000x734 pixels**
If you've taken **Hint**, it's obvious you have to Edit the Dimensions of the image.
* Edit IHDR Chunk :
![Step 2](https://i.postimg.cc/CxTxYr3m/Step-2.png)
![Step 3](https://i.postimg.cc/QxRJDsNw/Step-3.png)

* Change pixel value from **734 to 1000**
![Step 4](https://i.postimg.cc/nzRqPfwd/Step-4.png)

Export the image and save it as a **.png** only.


### Step 2 : Export the Image 
Open the Exported Image to get the **Hidden Flag**
![Flag](https://i.postimg.cc/9QCK2GQv/time-to-twerk-ak.png)
**Flag : vulncon{th475_0n3_w4y_70_h1D3_1T}**

###### If you've Solved this Challenge, Congratulations :) .... If not, you've learned something new :)
