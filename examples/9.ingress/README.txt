# 참고 : https://kubernetes.io/ko/docs/concepts/services-networking/ingress/

# Minikube 에서 ingress 활성화 (기본은 disable 되어 있음)
minikube addons enable ingress


# kubernetes-dashboard 를 기반으로 ingress 예제 만들기
kubectl apply -f ingress-eg1.yaml

호스트 내에 해당 도메인이 없음으로, 추가 설정
kubectl get ingress -n kubernetes-dashboard

sudo vim /etc/hosts

192.168.xx.x my-dashboard.com

