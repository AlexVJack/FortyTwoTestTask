#!/bin/bash
_command="python manage.py objects_list"
_date_now=$(date '+%d-%m-%Y')
_dir="."
_file="$_dir/$_date_now.dat"
chmod 777 $_dir
$_command 2>> $_file