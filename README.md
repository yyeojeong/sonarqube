# sonar qube

## sonarqube와 jenkins 연동 실습

1. 실습 예제 fork 하기

![fork](image-7.png)
![create a new fork](image-8.png)

2. sonarqube에 자신의 프로젝트 만들기

https://sonarqube.momoiot.co.kr/projects

![create project](image-9.png)
![select local project](image-10.png)
![create local project](image-11.png)
![setup project](image-12.png)
![select Locally](image-13.png)
![generate token](image-14.png)
![generated token](image-15.png)

3. Jenkins에 파이프라인 만들기

https://jenkins.momoiot.co.kr/me/my-views/view/all/

![New Item](image-16.png)
![Multibranch pipeline](image-17.png)
![branch source](image-18.png)
![scan pipeline](image-19.png)

4. Jenkinsfile의 sonarq 프로젝트 키 변경

![change key](image-20.png)


5. Jenkins 파이프라인 수동 실행

![select branch](image-21.png)
![build now](image-22.png)
![console output](image-23.png)
![result](image-24.png)

## sonar scanner

windows

```
docker run --rm -e SONAR_HOST_URL="http://host.docker.internal:9000"  -v ".:/usr/src" sonarsource/sonar-scanner-cli -D"sonar.projectKey=hello2" -D"sonar.sources=." -D"sonar.host.url=http://host.docker.internal:9000" -D"sonar.token=CHANGEIT"
```

mac

```
docker run --rm \
  -e SONAR_HOST_URL="http://host.docker.internal:9000"  \
  -v ".:/usr/src" sonarsource/sonar-scanner-cli \
  -Dsonar.projectKey=java \
  -Dsonar.sources=. \
  -D"sonar.java.binaries=target/classes" \
  -Dsonar.host.url=http://http://host.docker.internal:9000 \
  -Dsonar.token=sqp_a1ef2470a50a6570ad47ad410ea46135416c8f22
```

## custom rules

![my way](image.png)
![created my way](image-1.png)
![activate](image-2.png)
![dialog](image-3.png)
![bulk deactivate](image-4.png)
![setting-quality](image-5.png)
![select my way](image-6.png)
