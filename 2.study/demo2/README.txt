# 시크릿 생성
kubectl apply -f mongo-secret.yaml
kubectl get secret


# mongodb 에서 시크릿 참조하도록 변경

    spec:
      containers:
      - name: mongodb
        image: mongo  # dockerhub 에서 필요한 포트/환경변수 참조
        ports:
        - containerPort: 27017
        env:
        - name: MONGO_INITDB_ROOT_USERNAME
          value:
        - name: MONGO_INITDB_ROOT_PASSWORD
          value:

 => 위에는 plaintext 넣어도 되는데 비추
    그래서 secret 참조하도록 변경


# mongodb 생성
kubectl apply -f mongo.yaml

kubectl get deploy
kubectl get pods

kubectl describe pod mongo-xxxx


# service 랑 deployment 랑 --- 통해 한 파일에 작성 가능함
# 일단 이 예제에서는 따로 분리해서 진행하였음

kubectl apply -f mongo-service.yaml

kubectl get svc

kubectl describe svc mongodb-svc
Endpoints: 172.17.0.8:27017


kubectl get all -l app=mongodb


# mongo-express 웹 프런트 설치

        # - name: ME_CONFIG_MONGODB_SERVER
        #   value: 
        - name: ME_CONFIG_MONGODB_SERVER
          valueFrom:
            configMapRef:
              name: mongodb-configmap
              key: database_url

 => 위에는 plaintext 넣어도 되는데 비추
    그래서 configmap 참조하도록 변경

kubectl apply -f mongo-express-configmap.yaml

kubectl apply -f mongo-express.yaml


# mongo-express-service 적용

kubectl apply -f mongo-express-service.yaml


# external ip 가져오기

minikube service mongo-express-svc --url

또는 원격 vscode 환경이라면...

kubectl port-forward svc/mongo-express-svc 8081:8081


# mongodb 테스트하기

SOMA <- Create Database

