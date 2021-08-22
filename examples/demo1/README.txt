# Wordpress on K8s
#                 -> WordPress
# User -> Service -> WordPress -> MySQL
#                 -> WordPress

# 사용자 계정 만들기
echo -n "my-password" > ./password.txt

kubectl create secret generic mysql-pass --from-file=./password.txt

kubectl get secret

kubectl describe secret mysql-pass


# 볼륨 만들기 (DB용)
kubectl apply -f local-volume.yaml

kubectl get pv


# MySQL 생성
kubectl apply -f mysql.yaml

kubectl get pods

# MySQL 생성 후 계정 생성 (필요 시) - wordpress 버전에 따라 구버전 필요, 신버전 불필요
kubectl exec -it mysql-xxxxx -- bash

mysql -u root -p

show databases;

create database wp CHARACTER SET utf8;
grant all privileges on wp.* to wp@'%' identified by 'my-password';
flush privileges;
exit

exit


# WordPress 생성
kubectl apply -f wordpress.yaml


# 접속 시도
minikube service wordpress --url


# 모니터링 대시보드
(생략)


# 스케일링
kubectl scale deployment wordpress --replicas 3


# 오토 스케일링
kubectl apply -f wordpress-autoscaling.yaml

kubectl get hpa

while true; do curl localhost:30100; done

kubectl get hpa

kubectl get pods


# 모두 삭제 및 클린업
kubectl delete -f wordpress.yaml
kubectl delete -f mysql.yaml
kubectl delete -f local-volume.yaml
kubectl delete secret mysql-pass

