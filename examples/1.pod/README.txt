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

# Pod의 상태값(Status)
kubectl describe pods
- Pending : 생성 중
- Running : 실행 중
- Succeeded : 컨테이너 실행 성공적으로 마치고 종료
- Failed : 오류로 종료
- Unknown : 통신 불가

# 템플릿
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
    envs:
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
