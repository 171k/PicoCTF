# Mob Psycho Writeup

This challenge is actually quite easy. It should fall into easy category...

> Description
> 
> Can you handle APKs?Download the android apk [here](https://artifacts.picoctf.net/c_titan/142/mobpsycho.apk).



> Hints
> 
> Did you know you can `unzip` APK files?
> 
> Now you have the whole host of shell tools for searching these files.



So the hints said that I should unzip and search for files..



I inspected the apk just incase

![Screenshot 2025-11-24 002330.png](Screenshot%202025-11-24%20002330.png)



So I unzip it and run a "find" command

![Screenshot 2025-11-24 004843.png](Screenshot%202025-11-24%20004843.png)

then I found the flag.txt, I read the file and get a hex `7069636f4354467b6178386d433052553676655f4e5838356c346178386d436c5f37343664666133397d` 



Decrypt those in cyberchef and get the flag:

`picoCTF{ax8mC0RU6ve_NX85l4ax8mCl_746dfa39}`



