# Hideme Writeup

This one is quite simple too.

> Description
> 
> Every file gets a flag.The SOC analyst saw one image been sent back and forth between two people. They decided to investigate and found out that there was more than what meets the eye [here](https://artifacts.picoctf.net/c/260/flag.png).



I downloaded the file and its just this plain image:

![flag.png](C:\Users\Razlan\CTF\Pico\Forensic\Writeup\Medium\Hideme\flag.png)



So we only need to perform image forensic on this png. The challenge name is "Hide Me" so obviously there is a file hidden inside this image.



I ran `binwalk flag.png` to check if there is anything inside the image and I was right. 



The output:

```bash
DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
0             0x0             PNG image, 512 x 504, 8-bit/color RGBA, non-interlaced
41            0x29            Zlib compressed data, compressed
39739         0x9B3B          Zip archive data, at least v1.0 to extract, name: secret/
39804         0x9B7C          Zip archive data, at least v2.0 to extract, compressed size: 2944, uncompressed size: 3095, name: secret/flag.png
42983         0xA7E7          End of Zip archive, footer length: 22

```

As we can see, there is a secret/flag.png hidden inside this image. So I ran `binwalk -e flag.png` to extract everything out.



![flag2.png](flag2.png)

and.. thats it. We got the flag!



flag: `picoCTF{Hiddinng_An_imag3_within_@n_ima9e_ad9f6587}`


