# 서비스 계정 생성
kubectl create -f 1.serviceaccount-admin.yaml
kubectl describe secret lovehyun-admin-token-xxxx -n kube-system

# 관리자 권한 부여
kubectl create -f 2.admin-rbac.yaml

# 사용자 설정 구성
kubeconfig.conf

kubectl get pods --all-namespaces --kubeconfig kubeconfig.conf



# Pod 읽기 전용 사용자 만들기
kubectl create -f 3.serviceaccount-user.yaml

kubectl create -f 4.user-rbac.yaml

kubectl get secret
kubectl describe secret readuser-token-qsx66

kubectl config set-credentials readuser --token=xxxxxxxxxx

kubectl config get-contexts
kubectl config set-context readuser-context --cluster=minikube --user=readuser
kubectl config get-contexts

kubectl config use-context readuser-context
