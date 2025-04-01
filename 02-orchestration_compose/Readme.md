
```
# project name = directory name
docker compose up -d           

# specify project name
docker compose -p moviefullstack up -d      

# specify env file
docker compose -p moviefullstack --env-file=.env-prod up -d

# specify composition file(s)
docker compose -p moviefullstack --env-file=.env-prod -f docker-compose1.yml -f docker-compose2.yml up -d
```


docker compose -p moviefullstack up -d
docker compose -p moviefullstack2 --env-file .env2 up -d   