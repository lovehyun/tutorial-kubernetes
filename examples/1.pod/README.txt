# single container pod
kubectl exec -it my-pod-tomcat -- /bin/bash

# multiple container pod
kubectl exec -it my-pod-tomcat -c my-cont-tomcat -- /bin/bash

# exit
# ctrl + p, ctrl + q

# delete
kubectl delete -f pod_tomcat1.yaml

# delete multiple object
kubectl delete pod,service foo bar

# delete multiple object by label
kubectl delete pod,services -l name=myLabel

# delete all in namespace
kubectl delete pod,svc --all -n my-namespace

