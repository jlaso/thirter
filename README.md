## install

- create these two folders with enough permissions for the user you going to run docker
    - /opt/data/tshirter/postgres
    - /opt/data/tshirter/postgres-backup
    - /opt/data/tshirter/home/root
    
- duplicate .env.sample as .env and fill the data with the one that matches with your system
- duplicate web/.env.sample as web/.env and fill the data with the one that matches with your system

- create a rule in your /etc/hosts that points tshirter.local to 127.0.0.1

- create network `web` if you don't have it yet `docker network create web`

## build containers

```
docker-compose buid
docker-compose up -d
```

## ssh into containers

```
docker-compose exec web /bin/bash
./manage.py migrate
./manage.py createsuperuser
```

## check if all works

visit in the browser [tshirter.local](http://tshirter.local)