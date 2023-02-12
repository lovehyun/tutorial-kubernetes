# 참고 : https://kubernetes.io/ko/docs/concepts/configuration/configmap/

# configmap 설정 후, 변수로 가져오는 예시와
deployment.yaml


# configmap 설정 후, 파일로 생성하는 예시
deployment2.yaml


# 템플릿
apiVersion: v1
kind: ConfigMap
metadata:
  name: db-config
  namespace: default
data:
  DB_URL: localhost
  DB_USER: myuser
  DB_PASS: mypass
  DEBUG_INFO: debug

kubectl describe configmap db-config
