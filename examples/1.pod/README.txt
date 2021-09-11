# single container pod
# create vs apply 차이점 이해하기
kubectl create -f 1.nginx_pod.yaml
kubectl apply -f 1.nginx_pod.yaml


# delete
kubectl delete -f 1.nginx_pod.yaml


# 생성한 pod 에 접속하기
kubectl apply -f 2.tomcat_pod.yaml

kubectl exec -it my-nginx-pod -- /bin/bash
kubectl exec -it my-tomcat-pod -- /bin/bash


# 환경변수 추가하기
kubectl apply -f 3.mysql_pod.yaml


# 서비스 추가하고 연동하기
kubectl apply -f 4.mysql_svc.yaml


# 파드와 서비스 생성하기 및 서비스 연결
kubectl apply -f 5.nginx_svc.yaml

kubectl get svc

curl 192.168.49.2:3XXXX


# multiple container pod
kubectl apply -f 6.nginx_tomcat.yaml

kubectl exec -it my-nginx-tomcat-pods -c my-nginx -- /bin/bash
kubectl exec -it my-nginx-tomcat-pods -c my-tomcat -- /bin/bash

> exit
> ctrl + p, ctrl + q


# delete multiple objects
kubectl delete pod,service foo bar


# delete multiple objects by label
kubectl delete pod,services -l name=myLabel


# delete all in namespace
kubectl delete pod,svc --all -n my-namespace


# Pod의 상태값(Status)
kubectl describe pods
- Pending : 생성 중
- Running : 실행 중
- Succeeded : 컨테이너 실행 성공적으로 마치고 종료
- Failed : 오류로 종료
- Unknown : 통신 불가


# -----------------------------------------------
# 템플릿 참고
apiVersion: v1
kind: Pod
metadata:
  name: my-pod
  labels:
    app: my-pod-label
spec:
  containers:
  - name: my-pod
    image: my-app:latest
    resources:
      requests:
        cpu: 0.1   <-- core 당 연산양 (0.1 = 10%)
        memory: 200M
      limits:
        cpu: 0.5
        memory: 1G
    ports:
    - containerPort: 8000
    env:
    - name: MY-ENV1
      value: "my-value1"
    - name: HOSTNAME
      valueFrom:
        fieldRef:
          fieldPath: spec.nodeName
    - name: POD_NAME
      valueFrom:
        fieldRef:
          fieldPath: metadata.name
    - name: POD_IP
      valueFrom:
        fieldRef:
          fieldPath: status.podIP


# pod 에 접속
kubectl exec -it my-pod sh
env
