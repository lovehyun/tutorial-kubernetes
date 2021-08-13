# NodePort 는 Pod가 있는 WorkerNode 의 IP 주소로 접속함
# 노드 포트의 번호는 30000 ~ 32767 사이로만 사용 가능하며, 하나의 포트로 하나의 서비스만 가능.

# NodePort 사용해서 tomcat 접속
kubectl apply -f svc_tomcat1.yaml



# ClusterIP 사용해서 내부 pods 간에 통신
kubectl apply -f svc_mysql1.yaml

