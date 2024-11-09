#!/bin/bash -ex

# tweekit.sh - tweeks the sd card
# enable ssh
# setup user/pw
# add ssh keys
# config.txt

# mount sdcard's p1 (boot) and p2 (/ root)
# ./fixit.sh user password [/path/to/rootfs] [/path/to/bootfs]

user=$1
password=$2

mntdir=/media/${USER}
mntdir=/media

rootfs=${3:-${mntdir}/rootfs}
bootfs=${4:-${mntdir}/bootfs}

# sanity checks to make sure the image is mounted where we say it is.

if  [ ! -d "${bootfs}/overlays/" ]; then
    echo ${bootfs}/overlays/ does not exist.
    exit
fi

if  [ ! -d "${rootfs}/root/" ]; then
    echo ${rootfs}/root/ does not exist.
    exit
fi

# define user/password
# pre-seed raspios's "make a new user" process
# https://www.raspberrypi.com/news/raspberry-pi-bullseye-update-april-2022/
crypt_pas=$(echo ${password} | openssl passwd -6 -stdin)
printf "%s:%s" ${user} ${crypt_pas} > ${bootfs}/userconf.txt

# enable ssh,
sudo touch ${bootfs}/ssh

# setup ssh keys
sudo mkdir -p ${rootfs}/root/.ssh
sudo ssh-keygen -f ${rootfs}/root/.ssh/id_rsa
sudo mkdir -p ${rootfs}/home/${user}/.ssh
sudo ssh-keygen -f ${rootfs}/home/${user}/.ssh/id_rsa

# scp  videoteam@slf.sytes.net:.ssh/id_rsa.pub .
sudo cp id_rsa.pub ${rootfs}/root/.ssh/authorized_keys
sudo chown -R --reference=${rootfs}/root ${rootfs}/root/.ssh

sudo cp id_rsa.pub ${rootfs}/home/${user}/.ssh/authorized_keys
sudo chown -R --reference=${rootfs}/home/${user} ${rootfs}/home/${user}/.ssh

