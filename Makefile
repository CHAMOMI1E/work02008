start: #start on linux mint
    sudo docker-compose down
	python3 -m venv .venv
	sudo docker-compose up --build -d
	.venv/bin/python3 -m pip install --upgrade pip
	.venv/bin/pip install -r requirements.txt
	sudo docker-compose up --build -d
	sleep 5
	.venv/bin/python3 main.py

test:
    docker-compose down
    docker-compose up --build -d