#!/bin/bash

cd /home/work/

export WORKON_HOME=/home/work/env-wrapper

echo "---------------------------------"
echo 'active the virtualenvwrapper'
echo "---------------------------------"
source /usr/bin/virtualenvwrapper.sh


echo "---------------------------------"
echo 'creating the virtual environment:env-database...'
echo "---------------------------------"
mkvirtualenv env-database

echo "---------------------------------"
echo 'show virtual environment:'
echo "---------------------------------"
lsvirtualenv -b


#激活虚拟环境，进行初始化操作（按照必须的包）
export WORKON_HOME=/home/work/env-wrapper

echo ---------------------------------
echo 'active the virtualenvwrapper'
echo ---------------------------------
source /usr/bin/virtualenvwrapper.sh

echo ---------------------------------
echo 'change to virtualenv:env-excel'
echo ---------------------------------
workon env-database

pip install MySQL-python

