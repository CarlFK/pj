#!/bin/bash -ex

# mkimg.sh - flashes and configs an SD card for pi

img_host=http://downloads.raspberrypi.org

d=2024-07-04
f=lite
# f=full

img_path=raspios_${f}_armhf/images/raspios_${f}_armhf-${d}
base_name=${d}-raspios-bookworm-armhf-${f}.img

zip_name=${base_name}.xz

# dev=mmcblk0
dev=sda

# sudo mkdir /var/cache/rpi; sudo chown ${USER} /var/cache/rpi
cache=/var/cache/rpi

(cd ${cache}
  wget -N ${img_host}/${img_path}/${zip_name}
)

for p in /dev/${dev}* # p?
    do pumount $p || true
done

# time zcat ${cache}/${zip_name}|sudo dcfldd of=/dev/$dev
time xz --decompress --stdout ${cache}/${zip_name}|sudo dcfldd of=/dev/$dev

# mount the partitions under /media/boot and /media/rootfs
sudo partprobe /dev/${dev}
sleep 1

# pmount ${dev}p1 bootfs
# pmount ${dev}p2 rootfs
pmount ${dev}1 bootfs
pmount ${dev}2 rootfs

df -h
