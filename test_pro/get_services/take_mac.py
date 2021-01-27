from scapy.all import send, Ether, ARP, conf, srp, time, sr1
import os, sys
Victim_IP = input("Enter Victim IP for Take the mac Address : ")
Output_Interface = input("Output Interface : ")
ans, unans = srp(Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst=Victim_IP), timeout=2, iface=Output_Interface, inter=0.2)
print(ans)
print(unans)
for send, receive in ans:
    #print(send.summary())
    #print(send.show())
    #print(send.command())
    #print(receive.summary())
    #print(receive.show())
    #print(receive.command())
    #print(send.sprintf(r"%Ether.src%"))
    print(receive.sprintf(r"%Ether.src%"))
