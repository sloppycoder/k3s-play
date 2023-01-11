# networking components

```shell

# restrict servicelb pods to certain nodes
servicelb/restrict.sh

# deploy kong ingress and cert-manager
kubectl apply -k kong
kubectl apply -k cert-manager

# deploy http as example
kubectl apply -f httpbin

```
