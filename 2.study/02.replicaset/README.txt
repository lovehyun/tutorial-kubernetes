# 참고 : https://kubernetes.io/ko/docs/concepts/workloads/controllers/replicaset/

# replicaset
label 을 pod에 설정하고, selector 를 통해서 분산처리 할 리소스 레이블과 연결함


# tomcat pod 수동실행 테스트 (이미지 잘 가져와서 배포되는지 테스트용)
kubectl apply -f 1.pods.yaml


# tomcat pod 삭제
kubectl delete -f 1.tomcat.yaml


# 또는 수동으로 pod 삭제
kubectl delete pods tomcat


# replicaset
kubectl apply -f 2.replica.yaml


# replicaset 조회
kubectl get rs


# 묶여서 제어권 누가 하는지 확인
kubectl describe pods pod1


# 수동으로 갯수 늘리기
kubectl scale rs/tomcat --replicas=5


# replicaset auto healing 테스트
kubectl delete pods/tomcat-xxxxx


# 수동으로 모두 삭제하기
kubectl delete rs/tomcat


# 레이블을 통해 해당 파드 조회
kubectl get pods -l tier=tomcat
kubectl get pods --selector tier=tomcat
