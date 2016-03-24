#!/bin/bash

if [ $# -lt "1" ] ; then
    echo "usage: $0 <endpoint>"
    exit -1
fi

endpoint=$1
priv_key=93a16fea6455a62efd7af5b70b33fe853ee0c9a8
pub_key=f28cee0df52d38e16d477eea4fe0ac6d

curl 'gateway.marvel.com'"$endpoint"'?apikey='"$pub_key"'&ts=1&hash='$(echo -n 1$priv_key$pub_key | md5sum | grep -o "[0-9a-z]*")
