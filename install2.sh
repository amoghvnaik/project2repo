sudo curl -L "https://github.com/docker/compose/releases/download/1.24.0/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
cd project2/service1
sudo apt install python3-pip
pip3 install virtualenv
python3 -m virtualenv venv
. venv/bin/activate
pip3 install -r requirements.txt
python3
from application import db
db.create_all()
exit()
deactivate
