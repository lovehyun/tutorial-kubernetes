# Helm Charts
## Helm 이란?
- 쿠버네티스 패키지 메니저
- 공식 사이트 : https://helm.sh/ (한국어 : https://helm.sh/ko/)
- 패키지 리포 : https://artifacthub.io/

## Helm Charts 란?
- yaml 파일의 묶음 패키지

## 주요 버전 차이점
- Ver 2.0 vs Ver 3.0 은 매우 차이가 큼
  - Ver 2.0 에서, Client / Server(Tiller - K8s 내부에 설치)
  - 각종 설치와 업데이트 등 기록들을 Tiller 서버에서 보관하여 Release Management 를 수행함
  - 다만, Tiller 서버의 복잡성/보안성 등이 있어 K8s 클러스터에서 무거운 요소가 되어 3.0 에서 제거
  - 3.0 에서는 배포만 하는 간단한 바이너리로 동작 함

## 설치
- helm 설치
  ```bash
  > curl -fsSL -o get_helm.sh https://raw.githubusercontent.com/helm/helm/master/scripts/get-helm-3
  > chmod 700 get_helm.sh
  > ./get_helm.sh
  ```
- 헬름 차트 파일 구조
  - 예제 myapp
    ```bash
    myapp/
        Chart.yaml
        values.yaml
        charts/
        templates/
        ...
    ```

## 사용법
- 공식 가이드 : https://helm.sh/ko/docs/intro/using_helm/

- 헬름 리포(퍼블릭) 업데이트 : ` helm repo update `

- 퍼블릭 리포에서 패키지 검색 : ` helm search <keyword> `
  - 예제) 검색 / 상세보기
    - ` helm search mysql `
    - ` helm inspect stable/mariadb `

- 헬름 챠트 설치 : ` helm install <chartname> `
  - 예제) 
    - ` helm install stable/mariadb `
    - ` helm install stable/mariadb --name my-mariadb `
    - ` helm status my-mariadb `

- 헬름 차트 설치 상세
  - 기존값에 추가해서 overide 하기
    - ` helm inspect values <chartname> `
    - ` helm install <chartname> -f my-values.yaml `
    ```bash
    values.yaml     +  my-values.yaml  =  result
    image: myapp                          image: myapp
    version: 1.0.0     version: 2.0.0     version: 2.0.0
    ```
