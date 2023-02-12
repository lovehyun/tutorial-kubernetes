# 참고 : https://kubernetes.io/ko/docs/concepts/storage/volumes/

# 볼륨 생성 (1Gi 스토리지 1개)
kubectl apply -f 1.pv.yaml

# 볼륨 요청 (2Gi 요청시 실패 (Pending), 100Mi 요청시에도 1Gi 할당)
kubectl apply -f 2.pvc.yaml

