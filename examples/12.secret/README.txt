# 참고 : https://kubernetes.io/ko/docs/concepts/configuration/secret/

# 사용자 계정/암호 기반으로 secret 생성
kubectl apply -f user-pass.yaml

kubectl get secret



# 템플릿
apiVersion: v1
kind: Secret
metadata:
  name: my-secret
type: Opaque            # Opaque : 기본값, (key,value) 형식으로 임의의 데이터 설정
                        # kubernetes.io/service-account-token : 쿠버네티스 인증 토큰 저장
                        # kubernetes.io/dockerconfigjson : 도커 저장소의 인증 정보를 저장
                        # kubernetes.io/tls : TLS 인증서를 저장
data:
  username: dXNlcg==   <-- echo -n "user" | base64
  password: cGFzcw==



# 시크릿 사용 (Deployment 등)
apiVersion: apps/v1
kind: Deployment
(중략)
spec:
  template:
    spec:
      containers:
      - name: my-app
        image: my-app:latest
        ports:
        - containerPort: 5000
        env:
        - name: SECRET_USERNAME
          valueFrom:
            secretKeyRef:
              name: my-secret
              key: username
        - name: SECRET_PASSWORD
          valueFrom:
            secretKeyRef:
              name: my-secret
              key: password



# 프라이빗 레지스트리에서 이미지 풀링
kubectl create secret docker-registry dockersecret --docker-username=USERNAME --docker-password=PASSWORD --docker-email=EMAIL --docker-server=https://my-private.repo/v1/


# 시크릿 사용 (Deployment 등)
apiVersion: apps/v1
kind: Deployment
(중략)
spec:
  template:
    spec:
      containers:
      - name: my-app
        image: my-app:latest
        ports:
        - containerPort: 5000
      imagePullSecrets:
      - name: dockersecret



# 시크릿 데이터 저장 용량
최대 1MB, etcd에 비 암호화 상태의 text로 저장 됨



# 그 외 커맨드 라인 활용...

## 도커 레지스크리 시크릿
kubectl create secret docker-registry secret-tiger-docker \
  --docker-username=tiger \
  --docker-password=pass113 \
  --docker-email=tiger@acme.com

## TLS 시크릿
kubectl create secret tls my-tls-secret \
  --cert=path/to/cert/file \
  --key=path/to/key/file
  
## SSH 키 시크릿
kubectl create secret generic ssh-key-secret --from-file=ssh-privatekey=/path/to/.ssh/id_rsa --from-file=ssh-publickey=/path/to/.ssh/id_rsa.pub

