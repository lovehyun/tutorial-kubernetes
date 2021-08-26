# 개요
## 쿠버네티스란?
- (생략) 수업 강의자료 참조
## 쿠버네티스 유형
- Kubernetes (K8s) Original
- Minikube : Single node K8s cluster inside a VM (or docker or host)
- MicroK8s : Low-ops, light-weight, minimal production K8s (single/multi nodes)


# 쿠버네티스 설치
## K8s original 
- (생략)

## Minikube
- 공식가이드
  - https://v1-18.docs.kubernetes.io/ko/docs/tasks/tools/install-minikube/
- 수동설치 (바이너리)
  - 주의 : PC환경에 따라 아키텍처 다른 것 받아야 함
  - x86-64 기준
    ```bash
    > curl -Lo minikube https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64 && chmod +x minikube
    
    > sudo mkdir -p /usr/local/bin/
    > sudo install minikube /usr/local/bin/
    ```
- 실행
  - 시작 (도커 설치 시, 기본 드라이버 = docker, 그 외 qemu, ssh 등)
    - ` minikube start --driver=<driver_name> `
  - 상태
    - ` minikube status `
  - 중지(종료)
    - ` minikube stop `
  - 삭제
    - ` minikube delete `
- 내부 설정 확인 (minikube 컨테이너)
  ```bash
  > minikube kubectl get nodes
  > docker ps
  > minikube ssh
  > docker ps
  ```

### 확장팩 설치
- Addons 를 통한 추가 기능 활성화
  - 목록 확인 : ` minikube addons list `
  - 추가 활성화 : ` minikube addons enable dashboard metrics-server `
  - 비활성화 : ` minikube addons disable metrics-server `
  - 대시보드 접속 : ` minikube dashboard --url `

## Microk8s
- 공식가이드
  - https://microk8s.io/docs


# 쿠버네티스 명령어
## kubectl 설치
### 우부투 snap 방식
- 설치 명령어
  - ` snap install kubectl `

### apt 패키지를 통한 설치 방식
- 공식 사이트
  - https://kubernetes.io/ko/docs/tasks/tools/install-kubectl-linux/
- 패키지 관리자를 통한 설치
  1. apt 패키지 색인을 업데이트하고 쿠버네티스 apt 리포지터리를 사용하는 데 필요한 패키지들을 설치한다.
    - ` sudo apt-get update `
    - ` sudo apt-get install -y apt-transport-https ca-certificates curl `
  2. 구글 클라우드 공개 사이닝 키를 다운로드한다.
    - ` sudo curl -fsSLo /usr/share/keyrings/kubernetes-archive-keyring.gpg https://packages.cloud.google.com/apt/doc/apt-key.gpg `
  3. 쿠버네티스 apt 리포지터리를 추가한다.
    - ` echo "deb [signed-by=/usr/share/keyrings/kubernetes-archive-keyring.gpg] https://apt.kubernetes.io/ kubernetes-xenial main" | sudo tee /etc/apt/sources.list.d/kubernetes.list `
  4. 새 리포지터리의 apt 패키지 색인을 업데이트하고 kubectl을 설치한다.
    - ` sudo apt-get update `
    - ` sudo apt-get install -y kubectl `

### 수동설치 (바이너리) 방식
- 설치 명령어
  - ```bash
    > curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl"
    > curl -LO "https://dl.k8s.io/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl.sha256"
    > echo "$(<kubectl.sha256) kubectl" | sha256sum --check
    > sudo install -o root -g root -m 0755 kubectl /usr/local/bin/kubectl
    ```

## kubectl 사용법 (명령어)
- https://kubernetes.io/ko/docs/reference/kubectl/cheatsheet/

### kubectl 명령어 (기초)
- 명령어(command) 유형
  - 정보 조회 : ` kubectl get `
  - 생성 : ` kubectl create `
  - 생성(pod) : ` kubectl run `
  - 생성(service) : ` kubectl expose `
  - 로그 : ` kubectl logs `
  - 삭제 : ` kubectl delete `
- 컨트롤러 유형
  - 파드(pod) : ` pods = po `
    - ` kubectl get pods `
    - ` kubectl get po `
  - 리플리카셋(replicaset) : ` replicatsets = rs `
    - ` kubectl get replicasets `
    - ` kubectl get rs `
  - 디플로이먼트(deployment) : ` deployment = deploy `
    - ` kubectl get deployments `
    - ` kubectl get deploy `
- 서비스 유형
  - 서비스(service) : ` service = svc `
    - ` kubectl get services `
    - ` kubectl get svc `
- 네임스페이스
  - 네임스페이스(namespace) : ` namespace = ns `
- 다수의 서비스 조회
  - ` kubectl get deploy,rc,pods `

### kubectl 명령어 (일반)
- 컨트롤러 유형
  - 스테이트풀셋(statefulset) : ` statefulset = sts `
  - 데몬셋(daemonset) : ` daemonset = ds `
  - 잡(job) : ` job `
  - 크론(cronjab) : ` cronjob `
- 서비스 유형
  - 엔드포인트(endpoint) : ` endpoint = ep `
  - 인그레스(ingress) : ` ingress `
- 볼륨 유형
  - 볼륨(persistentvolume) : ` persistentvolume = pv `
  - 볼륨요청(persistentvolumeclaim) : `pesistentvolumeclaim = pvc `
  - 스토리지(storageclass) : ` storageclass `
- 설정
  - 설정(configmap) : ` configmap = cm `
  - 시크릿(secret) : ` secret `

### kubectl 디버깅
- 이벤트 상태 로그 : ` kubectl get events `

### 쿠버네티스 환경 기본 확인
- 클러스터 확인
  - ` kubectl cluster-info `
- 설정 확인 (멀티 클러스터 사용 시)
  - ` kubectl config view `
  - https://kubernetes.io/ko/docs/concepts/configuration/organize-cluster-access-kubeconfig/

## 쿠버네티스 활용/운영
- https://kubernetes.io/docs/tutorials/hello-minikube/

### 헬로월드
- 기본 서버 배포
  - ` kubectl create deployment hello-minikube --image=k8s.gcr.io/echoserver:1.10 `
  - ` kubectl expose deployment hello-minikube --type=NodePort --port=8080 `
    
- 기본 배포 컨테이너 확인
  - ` kubectl get all `

- 서비스 확인
  - ` kubectl get svc `

- 서비스 접속하기 (맥북에서는 특히 유용함)
  - ` minikube service hello-minikube --url `

- 호스트 포트 포워딩
  - ` kubectl port-forward hello-minikube-64b64df8c9-4rpfp 8080:8080 `

### 헬로 노드JS #1
- 컨테이너 pod 형태로 배포 및 서비스 확인
  ```bash
  > kubectl run nodejs --image=lovehyun/node-web --port=8080 
  pod/nodejs created
  
  > kubectl get pods
  NAME           READY   STATUS    RESTARTS   AGE
  nodejs         1/1     Running   0          24s
  
  > kubectl logs nodejs
  Server starting... at nodejs
  
  > kubectl exec nodejs -- curl 127.0.0.1:8080 --silent
  Welcome to nodejs
  
  > kubectl expose pod/nodejs --type=NodePort --name nodejs-http
  service/nodejs exposed
  
  > kubectl get svc
  nodejs-http   NodePort    10.103.4.59   <none>        8080:32681/TCP   4s

  > minikube service nodejs-http --url
  http://192.168.49.2:32681

  > curl 192.168.49.2:32681
  Welcome to nodejs
  ```

### 헬로 노드JS #2
- 컨테이너 deployment 형태로 배포 및 서비스 확인
  ```bash
  > kubectl create deployment nodejs --image=lovehyun/node-web --port=8080 
  deployment.apps/nodejs created

  > kubectl get deployments
  NAME           READY   UP-TO-DATE    AVAILABLE   AGE
  nodejs         1/1     1             1           7s

  > kubectl get replicasets
  NAME		           DESIRED	CURRENT		READY	  AGE
  nodejs-775cf96dc5  1		    1		      1	      59s

  > kubectl get pods
  NAME           		      READY   STATUS    RESTARTS   AGE
  nodejs-775cf96dc5-6qp5k 1/1     Running   0          2m30s

  > kubectl scale deployment/nodejs --replicas=2
  deployment.apps/nodejs scaled
  
  > kubectl get replicasets
  NAME 		            DESIRED	CURRENT		READY	  AGE
  nodejs-775cf96dc5   2	   	  2         2	      4m9s
  
  > kubectl get pods
  NAME           		      READY	  STATUS    RESTARTS    AGE
  nodejs-775cf96dc5-6qp5k 1/1	    Running	  0           4m13s
  nodejs-775cf96dc5-f6nwl	1/1	    Running	  0	          14s

  > kubectl expose deployment/nodejs --type=NodePort --name nodejs-http
  service/nodejs-http exposed

  > kubectl get svc
  NAME		TYPE	   CLUSTER-IP	 EXTERNAL-IP	PORT(S)		AGE
  nodejs-http	NodePort   10.97.135.189  <none>         8080:30518/TCP   4s

  > kubectl get nodes -o wide
  NAME        STATUS   ROLES                  AGE   VERSION   INTERNAL-IP    EXTERNAL-IP   OS-IMAGE             KERNEL-VERSION      CONTAINER-RUNTIME
  minikube    Ready    control-plane,master   5d    v1.21.2   192.168.49.2   <none>        Ubuntu 20.04.2 LTS   5.11.0-25-generic   docker://20.10.7

  > minikube service nodejs-http --url
  http://192.168.49.2:30518

  > curl 192.168.49.2:30518
  Welcome to nodejs-775cf96dc5-6qp5k
  
  > curl 192.168.49.2:30518
  Welcome to nodejs-775cf96dc5-f6nwl
  ```

## 메뉴얼 (한글)
- https://kubernetes.io/ko/docs/home/

## kubectl 설정 및 환경변수
### kubeconfig 환경 변수
- kubeconfig 란?
  - ` $HOME/.kube/config ` 파일을 통해 클러스터, 인증, 컨텍스트 정보 확인
- 클러스터 내 사용 가능한 자원의 목록
  - ` kubectl api-resources `
- 접속 가능한 컨텍스트 정보 확인
  - ` kubectl config get-contexts `
  - ```bash
    CURRENT   NAME       CLUSTER    AUTHINFO   NAMESPACE
    *         minikube   minikube   minikube   default
    ```
- 원하는 컨텍스트로 변경
  - ` kubectl config use-context minikube `
  - ` kubectl config current-context `
  - ` kubectl config set-context minikube --namespace=my-namespace `
- 현재 컨텍스트 보기
  - ` kubectl config view `
- K8s 클라우드 서비스 접속하기
  - Amazon EKS (AWS K8s 서비스) 접속하기 : https://docs.aws.amazon.com/ko_kr/eks/latest/userguide/create-kubeconfig.html
  - Google GKE (GCP K8s 서비스) 접속하기 : https://cloud.google.com/kubernetes-engine/docs/how-to/cluster-access-for-kubectl
  - Azure AKS (Azure K8s 서비스) 접속하기 : https://docs.microsoft.com/ko-kr/azure/aks/control-kubeconfig-access

- 명령어 실행 시 한시적으로 다른 컨텍스트에 명령어 요청
  - ` kubectl --kubeconfig=<config> get pods `
- bash 쉘 자동완성
  - ` echo 'source <(kubectl completion bash)' >> ~/.bashrc `
- 클러스터 노드들의 IP 주소 확인
  - ` kubectl get nodes -o wide `
  - ` kubectl get nodes -o json | jq -r '.items[].status.addresses[] | select(.type=="InternalIP") | .address' `

### kubectl 설정파일 (yaml 포멧)
- YAML 의 자료형
  - 주석 : #
  - 여러파일 구분자 : ---
  - Scalars(strings/numbers)
    - ```bash
      Name: shpark
      Year: 2021
      ```
  - Sequence(arrays/lists)
    - ```bash
      MySpecs:
      - good
      - better
      - best
      ```
  - Mappings(hashes/dictionaries)
    - ```bash
      Score:
        Math: 100
        Eng: 90
      ```
  - 기본 템플릿
    - ```bash
      apiVersion: v1
      kind: Pod
      metadata:
      spec:
      ```
### kubectl 명령어 디버깅
- 로그레벨 변경을 통한 상세 로그 확인
  - ` kubectl get pods --v=7 `
    - v=3 : 변경 사항에 대한 확장 정보
    - v=4 : 디버그 수준 상세화
    - v=5 : 트레이스 수준 상세화
    - v=6 : 요청한 리소스 표시
    - v=7 : HTTP 요청 헤더를 표시
    - v=8 : HTTP 요청 내용을 표시
    - v=9 : HTTP 요청 내용을 생략 없이 모두 표시


# 강의자료 소개
## 실습
- examples 디렉토리의, 아래 개별 디렉토리 내의 README.txt 참고
### 0. role
- 사용자 계정 확인
  - ` cat ~/.kube/config `
- 서비스 계정 확인
  - ` kubectl get serviceaccount `
  - ` kubectl get serviceaccount default -o yaml `
  - ` kubectl describe secret default-token-xxxxx `

### 1. pod
- 파드 생성 (실제로는 이렇게 배포하지 않음(개념 학습용), 실제로는 deployment 를 사용함)
- ` README.txt ` 참고

### 2. replicaset
- 리플리카셋 생성 (상동)

### 3. svc
- 서비스 컨트롤러
- imperative 명렁어
  - ```bash
    kubectl expose deployment nginx-app --type=NodePort
    kubectl get service
    kubectl describe service nginx-app

    curl localhost:31000
    ```
- 서비스 포트 타입
  - ClusterIP : 기본 타입이며 클러스터 내에서만 사용 가능 (외부 접속 불가)
  - NodePort : 모든 노드의 지정된 포트 할당 (외부에서 클러스터 안으로 접속 가능)
  - LoadBalancer : 퍼블릭 클라우드 또는 로드밸런서 장비가 있는 경우 사용 가능 (External-IP 로 표시)
  - ExternalName : 클러스터 안에서 외부로 접근할 때 사용 (도메인 주소로 응답)

### 4. deployment
- 디프로이먼트 컨트롤러
- imperative 명령어
  - ```bash
    kubectl run nginx-app --image nginx --port=80
    kubectl get pods
    kubectl get deployments

    kubectl scale deploy nginx-app --replicas=3
    kubectl get pods
    kubectl get deployments

    kubectl edit deployments nginx-app

    kubectl delete pod nginx-app-xxxxxxxx
    kubectl delete deployments nginx-app

    kubectl set image deploy/nginx-app nginx-app=nginx:1.11

    kubectl rollout history deploy nginx-app
    kubectl rollout history deploy nginx-app --revision=3
    kubectl rollout undo deploy nginx-app
    kubectl rollout undo deploy nginx-app --to-revision=3 
    kubectl rollout pause deploy/nginx-app
    kubectl rollout resume deploy/nginx-app
    ```
- declarative 명령어
  - ```bash
    kubectl create -f nginx-deployment.yml
    or
    kubectl apply -f nginx-deployment.yml
    ```

### 5. svc_lb
- 서비스 컨트롤러 (로드밸런싱)

### 6. volume
- 볼륨

### 7. configmap
- 컨피그맵

### 8. secret
- 시크릿

### 9. network_policy
- 네트워크

### 10. job/cronjob
- 다중 작업 실행 또는 정해진 날자/시간에 정기적으로 수행하는 파드들의 생성

### 11. statefulset
- 상태가 있는 파드들의 관리 (볼륨을 사용해서 특정 데이터를 저장)

### 12. daemonset
- 클러스터 내 모든 노드에 파드 배포 (예, 모니터링 / 로그 수집 등)
