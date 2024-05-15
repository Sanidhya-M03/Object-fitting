#!/usr/bin/bash 
l=`sed -n -e "2p" $1 | awk 'BEGIN{FS=" "}{print $2}'`
L=`echo $l | bc`
echo $L > L.txt
b=`sed -n -e "3p" $1 | awk 'BEGIN{FS=" "}{print $2}' | bc`
B=`echo $b | bc`
echo $B > B.txt
s1=`sed -n -e "5p" $1 | awk 'BEGIN{FS=" "}{print $2}' | bc`
S1=`echo $s1 | bc`
echo $S1 > S1.txt
s2=`sed -n -e "6p" $1 | awk 'BEGIN{FS=" "}{print $2}' | bc`
S2=`echo $s2 | bc`
echo $S2 > S2.txt
s3=`sed -n -e "7p" $1 | awk 'BEGIN{FS=" "}{print $2}' | bc`
S3=`echo $s3 | bc`
echo $S3 > S3.txt
s4=`sed -n -e "8p" $1 | awk 'BEGIN{FS=" "}{print $2}' | bc`
S4=`echo $s4 | bc`
echo $S4 > S4.txt
c1=`sed -n -e "9p" $1 | awk 'BEGIN{FS=" "}{print $2}' | bc`
C1=`echo $c1 | bc`
echo $C1 > C1.txt
c2=`sed -n -e "10p" $1 | awk 'BEGIN{FS=" "}{print $2}' | bc`
C2=`echo $c2 | bc`
echo $C2 > C2.txt
c3=`sed -n -e "11p" $1 | awk 'BEGIN{FS=" "}{print $2}' | bc`
C3=`echo $c3 | bc`
echo $C3 > C3.txt
python3 test3.py  
