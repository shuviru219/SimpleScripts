#!/usr/bin/env bash

Servers_list=/opt/servers_list
PackageName="package-name"

for Host in $(< $Servers_list )
do
    echo "Installing package on $Host"
    ssh "${Host}"  apt-get -y install "${PackageName}"

done