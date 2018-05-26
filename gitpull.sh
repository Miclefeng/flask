#!/bin/bash

git pull origin master
if [ 0 -eq $? ];
then
    chown www:www -R /data/wwwroot/default/fisher
fi

