# tomcat pod 수동실행 테스트 (이미지 잘 가져와서 배포되는지 테스트용)
kubectl apply -f tomcat.yaml

# tomcat delete
kubectl delete -f tomcat.yaml

# 또는 수동으로...
kubectl delete pods tomcat



# 수동으로 갯수 늘리기
kubectl scale rs/tomcat --replicas=5

# 수동으로 모두 삭제하기
kubectl delete rs/tomcat



# replicaset
kubectl apply -f replica.yaml

# replicaset 조회
kubectl get rs

# replicaset auto healing 테스트
kubectl delete pods/tomcat-xxxxx



# 수동으로 만든 pods 들을 하나의 replica 로 묶어 제어
kubectl apply -f pods.yaml

# 이전 replicaset 을 실행하기 (그럼 selector 를 통해서 묶이게 됨) 그래서 부족한 1개만 추가 실행됨
kubectl apply -f replica.yaml

# 묶여서 제어권 누가 하는지 확인
kubectl describe pods pod1

