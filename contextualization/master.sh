sudo add-apt-repository -y cloud-archive:stein
sudo add-apt-repository -y cloud-archive:rocky
sudo apt update && sudo apt -y dist-upgrade
sudo apt install -y python3-openstackclient
sudo apt install python3-pip

sudo apt-get install -y rabbitmq-server
pip3 install –upgrade pip
pip3 install celery==4.1.1
pip3 install celery[redis]
pip3 install flask
pip3 install flower

ssh-keygen -t rsa -N '' -f ~/.ssh/id_rsa

sudo rabbitmqctl add_user js js
sudo rabbitmqctl add_vhost jsvhost
sudo rabbitmqctl set_permissions -p jsvhost js ".*" ".*" ".*"

# install redis https://redis.io/topics/quickstart
# put files under ~/ACC_lab3/data/
# update master IP in `celeryconfig.py`
# open ports for rabbitmq and redis

git clone https://github.com/GallonSong/ACC_lab3.git
celery worker -A tasks --workdir /home/ubuntu/ACC_lab3/ -D
celery flower -A tasks --workdir /home/ubuntu/ACC_lab3/ --port=8080

export FLASK_APP=twitter.py
flask run

# ps aux | grep **
# kill @@@
