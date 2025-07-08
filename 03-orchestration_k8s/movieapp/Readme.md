## configmap with SQL script
```
kubectl create configmap db-init-sql --from-file=sql/01-tables.sql 
kubectl get cm
kubectl get cm db-init-sql -o yaml
kubectl get cm db-init-sql -o json
kubectl get cm db-init-sql -o jsonpath='{.data}'
kubectl get cm db-init-sql -o jsonpath='{.data.*}'
kubectl get cm db-init-sql -o jsonpath='{.data.01-tables\.sql}'
```
NB: doc jsonpath for k8s
https://kubernetes.io/docs/reference/kubectl/jsonpath/

Autres solution: 
- post install: cp + exec psql
- initContainers + command psql

## pod + deployment db postgres
```
kubectl apply -f .\postgres.deployment.yml
kubectl get po,deploy
kubectl get pv,pvc
```

```
kubectl logs pod/db-75d445446c-v9bnp
kubectl logs -l app=db 
```

```
kubectl exec -it db-75d445446c-v9bnp -- bash
psql -U movie -d dbmovies
\l
\d
create table t();
```

```
kubectl delete pod -l app=db
```

```
kubectl exec -it db-75d445446c-ccf5g -- bash
psql -U movie -d dbmovies
\d
```


## add a configmap after first creation
- delete deploy
- delete pvc
- apply config

## copy + exec psql
```
kubectl cp  02-data-persons.sql.gz db-64655b48fb-mm2gw:/tmp
kubectl cp  .\03-data-movies.sql.gz db-64655b48fb-mm2gw:/tmp
kubectl exec -it db-64655b48fb-mm2gw -- bash
...
psql -U movie -d dbmovies -f 02-data-persons.sql
gunzip -c 03-data-movies.sql.gz | psql -U movie -d dbmovies
...
```

TODO: à programmer comme job

## configmap as env
```
kubectl create configmap db-env --from-literal=POSTGRES_USER=movie --from-literal=POSTGRES_DB=dbmovies 
kubectl get cm
kubectl get cm db-env -o json    # or yaml
kubectl get cm db-env -o jsonpath='{.data}'

kubectl create configmap db-env2 --from-env-file=.env
kubectl get cm db-env2 -o jsonpath='{.data}'
```
## secret
```
kubectl create secret generic db-secret '--from-literal=POSTGRES_PASSWORD=eR*%@aq~&qsfgD23'
```
## api
```
kubectl apply -f .\api.deployment.yml
kubectl get po,deploy,svc
minikube service api-service
```
open navigator with http://127.0.0.1:57070/docs

Curl queries

GET:
```
curl -X 'GET' \
  'http://127.0.0.1:57070/movies/' \
  -H 'accept: application/json'
```

POST:
```
curl -X 'POST' \
  'http://127.0.0.1:57070/movies/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "title": "Les Animaux Fantastiques",
  "year": 2016,
  "duration": 115
}'
```

## rollout update
build new version of api (add route /persons)
```
docker build api -t movieapi:1.1
docker image ls
```

Declencher le rollout update en changeant l'image
```
kubectl set image deploy -l app=api  api=movieapi:1.1 

kubectl rollout status deployment/api
```

NAME                   READY   STATUS    RESTARTS   AGE
api-5d576d9bc4-5z8s8   1/1     Running   0          47m
api-5d576d9bc4-d5n6b   1/1     Running   0          47m
api-5d576d9bc4-n4jmm   1/1     Running   0          47m

NAME                   READY   STATUS    RESTARTS   AGE
api-6d9fb9f5fc-6jpg6   1/1     Running   0          17s
api-6d9fb9f5fc-hljd5   1/1     Running   0          14s
api-6d9fb9f5fc-hnb66   1/1     Running   0          19s

Retour arrière:
```
kubectl rollout undo deployment/api
```

NAME                   READY   STATUS    RESTARTS   AGE
api-5d576d9bc4-bd2cr   1/1     Running   0          24s
api-5d576d9bc4-swm5d   1/1     Running   0          27s
api-5d576d9bc4-vmjts   1/1     Running   0          26s

Restart en mode rollout
```
kubectl rollout restart deployment/api
```


Alt: kubectl edit
```
kubectl edit deployment/api
```














