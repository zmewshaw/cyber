#!/bin/bash
app=0
explore=0
list=0
posts=0
search=0
admin=0
content=0
for month in access_logs_2020/*; do
	for log in $month/*; do
		uri=$(cat $log | awk '{print $7}' | sort | uniq -c | grep -v jsp | awk '{print $1}')
		((app+=$(echo $uri | awk '{print $1}')))
		((explore+=$(echo $uri | awk '{print $2}')))
		((list+=$(echo $uri | awk '{print $3}')))
		((posts+=$(echo $uri | awk '{print $4}')))
		((search+=$(echo $uri | awk '{print $5}')))
		((admin+=$(echo $uri | awk '{print $6}')))
		((content+=$(echo $uri | awk '{print $7}')))
	done
done
echo $app
echo $explore
echo $list
echo $posts
echo $search
echo $admin
echo $content
