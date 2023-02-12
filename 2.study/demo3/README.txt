# green/orange/red 컨테이너 앱 생성
kubectl apply -f myapp-green.yaml
kubectl apply -f myapp-orange.yaml
kubectl apply -f myapp-red.yaml

# 연결하기 위한 서비스 생성 (web 서버 별도로 필요 없음)
kubectl apply -f myapp-service.yaml

# 연결 확인
minikube service myapp-svc --url
> http://192.168.49.2:30100


curl http://192.168.49.2:30100

<!DOCTYPE html>
<title>Hello Flask</title>
<body style="background: green">
<div style="text-align: center;">
    <h1>Hello, World from shpark!</h1>
</div>
</body>


curl http://192.168.49.2:30100

<!DOCTYPE html>
<title>Hello Flask</title>
<body style="background: orange">
<div style="text-align: center;">
    <h1>Hello, World from shpark!</h1>
</div>
</body>


# 연결 확인 (VSCODE)
포트포워딩 추가 : 포트 (192.168.49.2:30100) 추가 후 localhost:30100 으로 확인


# 서비스 및 로그 확인
kubectl get pods
kubectl logs -f deploy/myapp-green
kubectl logs -f deploy/myapp-orange --all-containers=true --since=1m


# 서비스 업그레이드 (아래가 최신버전)
kubectl set image deploy/myapp-green app-green=lovehyun/flask-app:1.3

kubectl rollout history deploy myapp-green
kubectl rollout history deploy myapp-green --revision=2
kubectl rollout history deploy myapp-green --revision=3

kubectl rollout undo deploy myapp-green
kubectl rollout history deploy myapp-green --revision=3
kubectl rollout history deploy myapp-green --revision=4
