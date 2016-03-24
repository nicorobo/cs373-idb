#!/bin/bash

if [ $# -lt "3" ] ; then
    echo "usage: $0 <url> <priv_key> <pub_key>"
    exit -1
fi

url=$1
priv_key=$2
pub_key=$3

curl "$url"'?apikey='"$pub_key"'&ts=1&hash='$(echo -n 1$priv_key$pub_key | md5sum | grep -o "[0-9a-z]*")
