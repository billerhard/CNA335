#!/bin/bash

touch /home/bill/hello
echo "Hello, this script is a service run by System.d on startup!" > /home/bill/hello
echo "Or, it will be when you type systemctl enable hello.service" >> /home/bill/hello
echo "You may also want to ensure you HAVE hello.service in the right place." >> /home/bill/hello
echo "You know what? It's kinda complicated." >> /home/bill/hello