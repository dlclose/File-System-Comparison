import os

for i in range(500):
    os.system("sudo dd if=/dev/urandom of=/mnt/ext4/newfile bs=1M count=10 iflag=fullblock 2>> out.txt")
