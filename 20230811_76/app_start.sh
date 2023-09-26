#!/bin/sh
tpid=`ps -ef |grep ftp_file_dispatcher.py |grep -v grep|awk '{print $2}'`
if [ ${tpid} ]; then
	echo 'app.py id is '${tpid}
	echo 'Stop app.py'
kill -15 $tpid
fi
sleep 5
echo $! >tpid
cd /home/developer/20230811_76
nohup python ftp_file_dispatcher.py > /dev/null 2>&1 &
echo 'Start ftp_file_dispatcher.py.py success!'
