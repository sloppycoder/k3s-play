# New Relic integration

Newrelic has guided installation steps that generates a command line for installation, e.g.

```shell

helm repo add newrelic https://helm-charts.newrelic.com && helm repo update && \
kubectl create namespace newrelic ; helm upgrade --install newrelic-bundle newrelic/nri-bundle \
 --set global.licenseKey=<license_key> \
 --set global.cluster=<cluster name in NR> \
 --namespace=newrelic \
 --set newrelic-infrastructure.privileged=true \
 --set global.lowDataMode=true \
 --set ksm.enabled=true \
 --set kubeEvents.enabled=true \
 --set newrelic-prometheus-agent.enabled=true \
 --set logging.enabled=true 


```

The above command is translated into the configs here. Pixie currently does not support ARM64 architecture yet so it is not enabled.
