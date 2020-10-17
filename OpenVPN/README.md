# OpenVPN


![alt text](https://miro.medium.com/max/700/1*Hkff7a_IV3HKPmOyf0sKkQ.png)


Description: A guide to connecting to our network using OpenVPN.

To get started download your configuration file from Access Machines in OpenVPN.See the picture to follow-


![alt text](https://miro.medium.com/max/700/1*J9Lb-oSAsVZAYqovfV5lyQ.png)

Then come the part to install OpenVPN ,if you already have it great.
Otherwise you can install it by following command-

## sudo apt-get install openvpn

You would have notice the configuration you downloaded is named as YourUserName.opvn
Once you have installed openvpn on your machine then go the the directory of that configuration file (using cd command) and there type following command as shown below-

## sudo openvpn Filename.ovpn

It will start connecting and when terminal show you regarding sequence completed as shown here

![alt text](https://miro.medium.com/max/700/1*-OslDkDUN0H3SyE7omyvvQ.png) 

Now you are connected to OpenVPN.For confirmation go to access page and you can see in network information it shows connected and you have an IP address

![alt text](https://miro.medium.com/max/548/1*YCCD0X5z-8S1jrRea1IpDQ.jpeg)

So we have completed the challenge and this would also help you in accessing the machines in next challenges you solve. 