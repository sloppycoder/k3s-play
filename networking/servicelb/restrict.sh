# restrict servicelb only to 2 nodes in the cluster

kubectl label nodes pie4 svccontroller.k3s.cattle.io/enablelb=true svccontroller.k3s.cattle.io/lbpool=pool1
kubectl label nodes pie9 svccontroller.k3s.cattle.io/enablelb=true svccontroller.k3s.cattle.io/lbpool=pool2
kubectl label nodes pie1 svccontroller.k3s.cattle.io/enablelb=true svccontroller.k3s.cattle.io/lbpool=pool2
