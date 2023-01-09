# K3S Playground
A collection of configuration and experiment on a local K3S cluster.

Currently it consists of  3 Raspberry Pi 4 8GB RAM boards running Ubuntu 20.04.5 LTS, connected to a Synology NAS serving as NFS server.

![Cluster Photo](images/cluster.jpg)

Each PI board uses static IP. /etc/hosts on each board will contain mapping for each node.

| IP address | hostname |
|---|---|
| 192.168.1.201 | pie1 |
| 192.168.1.202 | pie2 |
| 192.168.1.203 | pie3 |


## install K3S on the cluster
[this repo](https://github.com/sloppycoder/k3s-ansible) contains Ansible playbook for installing the K3S 1.24 on the cluster. 

## Configurations

| folder | content |
|---|---|
| [kong-calico](kong-calico/) | install calico, kong together |
| [kong-istio-datadog](kong-istio-datadog/) | Using Istio and Kong together and use Datadog for observatility |
| [infra](infra/) | common infra components, e.g. nfs-subdir-external-provisioner, redis |
| [misc](misc/) | misc snippets, e.g. certbot scripts, python script to handle ~/.kube/config file etc |

