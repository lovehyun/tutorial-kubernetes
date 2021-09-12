# 참고 : https://kubernetes.io/ko/docs/concepts/workloads/controllers/job/
#       https://kubernetes.io/ko/docs/concepts/workloads/controllers/cron-jobs/

# 동시 잡 수행
kubectl apply -f job.yaml

kubectl get jobs

kubectl describe job my-job



# 반복 잡 수행
kubectl apply -f cronjob.yaml

kubectl get cronjobs

kubectl describe cronjob my-cronjob

kubectl get pods

kubectl logs my-cronjob-xxxxx

