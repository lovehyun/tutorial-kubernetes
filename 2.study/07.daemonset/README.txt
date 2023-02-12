# 참고 : https://kubernetes.io/ko/docs/concepts/workloads/controllers/daemonset/

# FluentD-Elasticsearch 데몬셋 생성
kubectl apply -f fluentd_ds.yaml

또는 외부에서 직접 적용 시 (위 코드와 동일 내용)
kubectl apply -f https://k8s.io/examples/controllers/daemonset.yaml

* 적용되는 네임스페이스 확인 - 시스템 서비스임으로 kube-system 에 적용



# 데몬셋의 업데이트 전략 확인
kubectl get ds/fluentd-elasticsearch -o go-template='{{.spec.updateStrategy.type}}{{"\n"}}' -n kube-system
=> RollingUpate


# 데몬셋의 업데이트 진행 (v2.5.2 -> v2.6.0)
kubectl set image ds/fluentd-elasticsearch fluentd-elasticsearch=quay.io/fluentd_elasticsearch/fluentd:v2.6.0 -n kube-system



# 삭제 및 클린업
kubectl delete ds fluentd-elasticsearch -n kube-system

