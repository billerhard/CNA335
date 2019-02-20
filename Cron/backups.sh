#!/bin/bash

cd /home/pi/backups
if [ -f "backup" ]
then
cp backup backup.old
fi
tail /var/log/syslog > backup