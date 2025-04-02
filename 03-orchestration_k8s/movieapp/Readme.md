## configmap with SQL script
kubectl create configmap db-init-sql --from-file=sql/01-tables.sql 
kubectl get cm
kubectl get cm db-init-sql -o yaml
kubectl get cm db-init-sql -o json
kubectl get cm db-init-sql -o jsonpath='{.data}'
kubectl get cm db-init-sql -o jsonpath='{.data.*}'
kubectl get cm db-init-sql -o jsonpath='{.data.01-tables\.sql}'

## pod + deployment db postgres
kubectl apply -f .\postgres.deployment.yml
kubectl get po,deploy
kubectl get pv,pvc

kubectl logs pod/db-75d445446c-v9bnp
kubectl logs -l app=db 

kubectl exec -it db-75d445446c-v9bnp -- bash
psql -U movie -d dbmovies
\l
\d
create table t();

kubectl delete pod -l app=db

kubectl exec -it db-75d445446c-ccf5g -- bash
psql -U movie -d dbmovies
\d


## add a configmap after first creation
- delete deploy
- delete pv
- apply config