#!/bin/sh
while true
do
     temp1=`i2cget -y 2 0x48 0`
     temp1F=$((($temp1*9/5) + 32))
     temp2=`i2cget -y 2 0x4a 0`
     temp2F=$((($temp2*9/5)+32))
    echo temp 1 = $temp1F temp 2  = $temp2F
    sleep 0.25s
done
