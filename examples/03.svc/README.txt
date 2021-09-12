# 참고 : https://kubernetes.io/ko/docs/concepts/services-networking/service/

# NodePort 는 Pod가 있는 WorkerNode 의 IP 주소로 접속함
# 노드 포트의 번호는 30000 ~ 32767 사이로만 사용 가능하며, 하나의 포트로 하나의 서비스만 가능.

# ClusterIP 사용해서 내부 pods 간에 통신
kubectl apply -f 1.mysql_svc.yaml


# NodePort 사용해서 tomcat 접속
kubectl apply -f 2.tomcat_svc.yaml


# ExternalName 사용해서 클러스터 내부에서 외부에 접속
kubectl apply -f 3.ext_svc.yaml


kubectl run -it busybox --rm --image=busybox sh
> ping my-googledns-svc
> ping my-googledns-svc.default.svc.cluster.local


ExternalName 필드에 예전 kubedns 에서는 IP 주소도 설정 가능하였으나,
coredns 에서는 해당 필드를 모두 string 으로 인지하여, 더이상 IP 주소 사용할 수 없음.

위 예에서는 외부에 존재하는 DNS를(google dns) 사용해서 잘 와닿지 않을 수 있는데, 
외부 공식 DNS가 없는 Cloud 내부의 사설 IP 의 URL 등을 생각하면 됨.

예) Cloud 내에 구축한 내 RDS 주소라던지...

