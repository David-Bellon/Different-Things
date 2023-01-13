# Different-Things
## Installation
- First download all the files from this repo. What you have to run is the file main_gui.py from the gui folder, do not change anything else. Once you have download it, it won't work because the models are not in this repo. So in order to access the models go to this drive folder: https://drive.google.com/drive/folders/1hzWBLmvei-kfJvSrpZxWutIs-kSthkhC?usp=sharing and download every file that is inside.
- Then with everything downloaded create a folder named models and put all the files from the drive link into that folder.
You use get something like this. (Forget all the other folders you don't have, they are venvs folder that you will have in a moment).
![image](https://user-images.githubusercontent.com/91338053/212155653-807a4492-24d3-4a0b-a0fb-f3e97941f4e0.png)
- Next install the requirements and if you want create a virtual env before so you will have the same folders.
- Extra thing: You may have problems with hugging face library or something. If that is the case just create a folder name cache (doesn't need to be where mine you can just create one in the C:\\User\.cache and it's fine) and change the path to that.  

## Usage
- As said before only run the main_gui.py file inside the gui folder. The first time it will take more time than usual, this is normal because is importing everything as well as if it's the first time you run the models and you have a GPU that use CUDA it will take time the first time.  
- So once the main window appear you will see something like this.
![image](https://user-images.githubusercontent.com/91338053/212170783-6dcccc05-f679-4b50-9179-5a69a4077524.png)  
Yes is an incredible main menu I know, now shut up cause is not the important thing.
- As you can see, you have four options to pick, Youtube Download app, a Face Tracking model, an Audio to Text model and a Chess Board if you want to play with stupid bots that will sacrifice their queen without reasons.  

### Youtube Download
As it says you can download any video from youtube to audio so you don't have to pay for Spotify. This is what you will get.
![image](https://user-images.githubusercontent.com/91338053/212171725-8c54494c-78ab-4556-b897-13b3f1076ef4.png)  
You may think this does not work, I would think the same just looking at it, but it does, yes I'm surprised as well.  
Nothing more special, it does what is says.  

### Face Tracking
It's a model that opens your webcam or the video device you have and looks for faces and draws a squre on its position. Like this.  
![image](https://user-images.githubusercontent.com/91338053/212297151-62da7e77-28b1-494c-bbea-39b4e1b71853.png)  
It does work well and with better cameras more. Just use GPU because if you try with cpu it's gonna be so laggy and it won't destroy your PC.

### Audio to Text
Pick the file that you want, has to be a mp3, mp4 or wav, select the model and then click transcribe and it will give you a pop up window with the text of your audio. The bigger the model you select the better the quality but the more VRAM it requires. Take a look.
![image](https://user-images.githubusercontent.com/91338053/212174179-a6074ef7-0ad7-4351-90ed-27ca28c5cce3.png)  
As you can see in the image if lets you record your audio up to ten second (if you want to change this duration go to the record_audio.py and change the seconds var to any number you want). And then it will give you the same pop up window with the text and the interval of the phrase.  
![image](https://user-images.githubusercontent.com/91338053/212174850-3226e287-7728-4c4a-b85f-2ace6eb038bb.png)  
It's cool I know :)  
And yes I know it not a good UI or whatever but I don't care it's just a little thing to show all this things.  
### Chess
Well is chess I don't know what you want me to say. You play with whites and a stupid IA tries to do something reasonable. As said before it really bad but thats the only way you are gonna feel good at chess so you are welcome.  
![image](https://user-images.githubusercontent.com/91338053/212178190-dbccde54-6ffe-47ea-8c16-2a585382608e.png)  

## End
I don't know how to end this so thats it, different things and some useful some less but yeah, things.  
Now, get out of here.


