# Professional Excuser
Very handy when you want to use an excuse to avoid any compromise

## Docker 
### Build
```
docker build -t professional-excuser . 
```

### Run
```
docker run -p 80:80 professional-excuser
```

## Kubernetes

### Install the chart
```
cd infra & helm install professional-excuser professional-excuser
```
### Port Forward
```
kubectl port-forward svc/professional-excuser 8080:80
```