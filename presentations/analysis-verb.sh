#!/bin/bash
delete=0
get=0
post=0
put=0
for month in access_logs_2020/*; do
	for log in $month/*; do
		verbs=$(cat $log | awk '{print $6}' | sort | uniq -c | awk '{print $1}')
		((delete+=$(echo $verbs | awk '{print $1}')))
		((get+=$(echo $verbs | awk '{print $2}')))
		((post+=$(echo $verbs | awk '{print $3}')))
		((put+=$(echo $verbs | awk '{print $4}')))
	done
done
echo $delete
echo $get
echo $post
echo $put
