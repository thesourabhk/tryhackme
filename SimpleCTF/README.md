# SimpleCTF


### TASK 1 & 2
First let's begin with nmap scan and see what we can find-
```
nmap -sC -A -Pn-  $IP
```

![image](https://www.secjuice.com/content/images/2020/08/image.png)

From nmap scan we know that 2 port under 1000 are running.
And ssh is running on higher port.

### TASK 3
lets access the machine with web browser but we get the default page(basically nothing).
So we see two interesting things:

1.Anonymous FTP login
2.robots.txt file

WE can see robots.txt by attaching it to the url but nothing peculiar is there.
So let's fire up gobuster and search for any hidden directory.

![image](https://www.secjuice.com/content/images/2020/08/image-3.png)

lets search the hidden directories.There is one intresting directory with name simple with valid response code.So check it-

![image](https://www.secjuice.com/content/images/2020/08/image-5.png)

Accessing the simple directory we come to know that there is a Content Management System (CMS). Let’s find out more information about this cms. I am going use searchsploit to check if I find any vulnerabilities against this service

![image](https://www.secjuice.com/content/images/2020/08/image-6.png)

Looking at the searchsploit result we find tons of vulnerabilities. The question asked in the challenge is the CVE number. So searching more against the cms service I bumped across exploit DB and it showed me the CVE number associated with this vulnerability, also when I compared the results with the searchsploit data I decided to go for the SQL injection vulnerability

![image](https://www.secjuice.com/content/images/2020/08/image-7.png)

So,now we have got the CVE.

### TASK 4

The application is vulnerable to SQL vulnerability.

### TASK 5 & 6

Now let’s exploit the vulnerability and see if we can find the username and password. So I am going to use the exploit I found via searchsploit. Navigate to the exploit filesystem and use the parameters as shown below. Wait for a while and you will get the username and password.

![image](https://www.secjuice.com/content/images/2020/08/image-8.png)

I am using rockyou here,but you can use any wordlist you have.

Now the exploit used will give us the username and password.Now that we have our username and password, remember that our Nmap scan results also pointed out to the ssh service which was running on port 2222 so let’s try logging in the machine using ssh on port 2222.
_note:I have not included the screenshot as I want you to try this by yourself and only refer this when needed._

![image](https://www.secjuice.com/content/images/2020/08/image-9.png)

### TASK 7

Now find the flag or just list the contents. we find out our user flag as shown below

![image][https://www.secjuice.com/content/images/2020/08/image-10.png]

### TASK 8

We have one more user other than mitch but we can't switch to it
![image](https://www.secjuice.com/content/images/2020/08/image-11.png)

### TASK 9

Let’s find out a way to get escalate our privileges. So we come to know that the user Mitch can run vim. We can use vim to escalate our privileges.

![image](https://www.secjuice.com/content/images/2020/08/image-12.png)

### TASK 10

Let’s run vim to escalate our privilege via a bash shell.

![image](https://www.secjuice.com/content/images/2020/08/image-13.png)

Now go to the root directory and find our final flag.

![image](https://www.secjuice.com/content/images/2020/08/image-14.png)