sudo add-apt-repository -y cloud-archive:stein
sudo add-apt-repository -y cloud-archive:rocky
sudo apt update && apt -y dist-upgrade
sudo apt install -y python3-openstackclient

sudo apt-get install -y rabbitmq-server
pip3 install –upgrade pip
pip3 install celery==4.1.1
pip3 install flask
pip3 install flower

ssh-keygen -t rsa -N '' -f ~/.ssh/id_rsa

git clone https://github.com/GallonSong/ACC_lab3.git
celery flower -A tasks --workdir /home/ubuntu/ACC_lab3/ --port=8080
