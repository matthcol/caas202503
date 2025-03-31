Linux bash:
```
docker run -d \
	--name pgmovies \
    -e POSTGRES_USER=movie \
	-e POSTGRES_PASSWORD=mysecretpassword \
	-e POSTGRES_DB=dbmovies \
	postgres
```

Powershell:
```
docker run -d `
	--name pgmovies `
    -e POSTGRES_USER=movie `
	-e POSTGRES_PASSWORD=mysecretpassword `
	-e POSTGRES_DB=dbmovies `
	postgres
```

## docker run vs exec

docker run : create a new container with a (default) command
docker exec: launch a command in an existing container

Example:
```
docker exec -it pgmovies bash
```

## mapping de port
```
docker run -d `
	--name pgmovies `
    -e POSTGRES_USER=movie `
	-e POSTGRES_PASSWORD=mysecretpassword `
	-e POSTGRES_DB=dbmovies `
    -p 5432:5432 `
	postgres
```

```
docker run -d `
	--name pgmovies `
    -e POSTGRES_USER=movie `
	-e POSTGRES_PASSWORD=mysecretpassword `
	-e POSTGRES_DB=dbmovies `
    -p 127.0.0.1:5433:5432 `
	postgres
```

Check network config:
```
docker ps
docker inspect pgmovies
```

## Composition docker
File: docker-compose.yml (custom)

docker compose up -d
docker compose down

docker compose ps
docker compose ps -a

docker compose start
docker compose start db 

docker compose stop
docker compose stop db 

docker compose exec -it db bash
docker exec -it postgres-db-1 bash

docker compose logs
docker compose logs db 

### Composition name
docker compose -p postgres exec -it db bash

-p : specify project name = composition name

docker compose -p movies up -d
docker compose -p movies down

docker compose -p movies up -d pgadmin4
docker compose -p movies down pgadmin4

### Atelier network
Lancer un CLI psql dans un conteneur provisoire qui se connecte à la base postgres,
au sein du sous réseau docker movies_default

docker run -it --network movies_default postgres:17 psql -U movie -d dbmovies -h db

### Volumes
docker compose -p movies exec -it db bash -c "ls -l /docker-entrypoint-initdb.d"  

docker compose -p movies exec -it db psql -U movie -d dbmovies -c " insert into movie (title, year) values ('Les Animaux Fantastiques', 2016);"
docker compose -p movies exec -it db psql -U movie -d dbmovies -c "select * from movie where title like 'Les Animaux%'"




