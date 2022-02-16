import os

for i in range(250):
    os.system("sudo dd if=/dev/urandom of=/mnt/ext4/newfile bs=100M count=1 iflag=fullblock 2>> out.txt")
