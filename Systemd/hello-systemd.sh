#!/bin/bash

touch ~/hello
echo "Hello, this script is a service run by System.d on startup!" > ~/hello
echo "Or, it will be when you type systemctl enable hello.service" >> ~/hello
echo "You may also want to ensure you HAVE hello.service in the right place." >> ~/hello
echo "You know what? It's kinda complicated." >> ~/hello