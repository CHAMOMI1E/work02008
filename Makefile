start_linux: #start on linux mint
    sudo docker-compose down
	python -m venv .venv
	.venv/bin/python -m pip install --upgrade pip
	.venv/bin/pip install -r requirements.txt
	sudo docker-compose up --build -d
	sleep 5
	flask db upgrade
	flask run

start_windows:
    docker-compose down
	python -m venv .venv
	.venv/bin/python -m pip install --upgrade pip
	.venv/bin/pip install -r requirements.txt
	docker-compose up --build -d
	sleep 5
	flask db upgrade
	flask run