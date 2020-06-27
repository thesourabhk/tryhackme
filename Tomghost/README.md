# Room :- Tomcat

![image](https://imgur.com/Zo8qTLQ.png)

Apache Ghostcat is a new vulnerability with High-risk severity discovered by a security researcher of Chaitin Tech in Apache Jserv Protocol(AJP). AJP is an optimized version of the HTTP protocol in binary form and used in scenarios that require clustering or reverse proxies. By default, it is enabled on port 8009. By exploiting this vulnerability an attacker can read any web application files including source code. If the application allows file upload then an attacker can upload any files to the server including malicious Java Server Pages (JSP) and can gain system access.
To know more about this vulnerability, click [Here](https://blog.qualys.com/laws-of-vulnerabilities/2015/01/27/the-ghost-vulnerability)

---
## Penetration Testing Methodology

**Reconnaissance**
* nmap

**Exploitation**
* ajp shooter

**Previlege Elivation**
* GTFObins.github.io

**Capturing the flag**
* user.txt
* root.txt

---
### Nmap scan 
Use the nmap to get the details about the port 8009.
![image](https://imgur.com/QtZTdEk.png)

Once we get the open port 8009, use the exploit available on Github.

[![Github](https://upload.wikimedia.org/wikipedia/commons/b/bc/Pornhub-style_GitHub_logo.png)](https://github.com/00theway/Ghostcat-CNVD-2020-10487)

Now, check if the /WEB-INF/web.xml file is readable.
![image](https://imgur.com/F4VGnoE.png)

Once we are able to read the file we will get the credential of user skyfuck.
![image](https://imgur.com/Wb4vuGk.png)
Now use the same credentials to SSH.
  ![image](https://imgur.com/pvs2XwQ.png)
Now you can move to the Home directory to check the number of user and if you can login to the other.
     ![image](https://imgur.com/u0mE6jO.png)
After getting the user shell, it is time for privilege escalation.

After ls command, we will get a PGP file that needs to be decrypted using a passphrase to get the other user’s credentials.

Now transfer the files to the local system using SCP to decrypt the PGP file. For this use the user’s credentials which we got earlier.
![image](https://imgur.com/UZoq9qH.png)
Now use gpg2john to convert the tryhackme.asc file.
After converting the file use JohnTheRipper to crack it. Use rockyou.txt for the same.
![image](https://imgur.com/wRCooKF.png)
Use the cracked passphrase to decrypt the PGP file.
First import the crdential file to your system and decrypt it.
![image](https://imgur.com/0me8sKm.png)

Now use the new user’s credentials.
![image](https://imgur.com/IFFKNlu.png)
After logging in with user merlin do sudo -l.

User merlin has sudo access on zip so check the /usr/bin/zip privilege escalation. To perform privilege escalation we need to create any file and zip it. Then use the below command.
Checking for and exploit of zip on gtfobins.github.io we get the code to execut for previlege elevation.

![image](https://imgur.com/dR5ue8n.png)
copy the code and use it on the terminal to get a root access.
![image](https://imgur.com/iPGWXnG.png)

**Hurray we got the flags**
**_By Sourabh_**
 