#!/bin/sh               
tpid=`ps -ef |grep app.py |grep -v grep|awk '{print $2}'`
if [ ${tpid} ]; then
	echo ${tpid}
	kill -15 $tpid
fi

