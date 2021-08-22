# 서비스 계정 생성
kubectl create -f 1.serviceaccount-admin.yaml
kubectl describe secret lovehyun-admin-token-xxxx -n kube-system

# 관리자 권한 부여
kubectl create -f 2.admin-rbac.yaml

# 사용자 설정 구성 (별도 파일로 - 원본 파일 망가트리지 않도록 임시로 새 파일 생성)
kubeconfig.conf

kubectl get pods --all-namespaces --kubeconfig kubeconfig.conf



# Pod 읽기 전용 사용자 만들기
kubectl create -f 3.serviceaccount-user.yaml

kubectl create -f 4.user-rbac.yaml

kubectl get secret
kubectl describe secret readonly-user-token-qsx66

kubectl config set-credentials readonly-user --token=xxxxxxxxxx

kubectl config get-contexts
kubectl config set-context readonly-user-context --cluster=minikube --user=readonly-user
kubectl config get-contexts

kubectl config use-context readonly-user-context



# 삭제
kubectl config delete-context readonly-user-context
kubectl config delete-user readonly-user

kubectl delete -f 4.uesr-rbac.yaml
kubectl delete -f 3.serviceaccount-user.yaml
kubectl delete -f 2.admin-rbac.yaml
kubectl delete -f 1.serviceaccount-admin.yaml
