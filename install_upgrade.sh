#!/bin/bash

arg1=$1

if [ $arg1 ]
then
echo "We have an arg"
echo $arg1
if [ $arg1 == "-h" ]
then
echo "This script takes in an argument at command line, uses apt to update the pacckage, if the package is not installed updates it, if the argument is -h then it echos what the program does and that the user can supply an argument, else uses apt to update and upgrade automatically (no pushing of y)"
else
apt install $arg1
fi
else
echo "No arg provided"
apt update
apt upgrade
fi
