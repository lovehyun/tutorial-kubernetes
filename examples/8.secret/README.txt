# 템플릿
apiVersion: v1
kind: Secret
metadata:
  name: my-secret
type: Opaque           <-- 기본값, key-value 형식으로 임의의 데이터 설정
data:
  username: dXNlcg==   <-- echo -n "uesr" | base64
  password: cGFzcw==
