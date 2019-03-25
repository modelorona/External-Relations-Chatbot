#!/usr/bin/env bash

set -e

#rm -rf /home/ubuntu/dissertation

#git clone git@gitlab.com:modelorona/dissertation.git
cd /home/ubuntu/dissertation
git add .
git stash
git pull

cd /home/ubuntu/dissertation/client
npm install
echo "after install"
npm run build
echo "after build"

#source ~/projectenv/bin/activate
cd ~/dissertation/server
echo "after cd"

kill `cat pid.txt`

echo "after killing 5000 listener"
pip3 install -r requirements.txt
echo "after pip3 install"
flask run &> output.log &
echo "after running application"
echo $! > pid.txt

exit
