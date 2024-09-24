# sonar qube

## sonar scanner

windows

```
docker run --rm -e SONAR_HOST_URL="http://host.docker.internal:9000"  -v ".:/usr/src" sonarsource/sonar-scanner-cli -D"sonar.projectKey=hello2" -D"sonar.sources=." -D"sonar.host.url=http://host.docker.internal:9000" -D"sonar.token=CHANGEIT"
```

linux

```
docker run --rm \
  -e SONAR_HOST_URL="http://host.docker.internal:9000"  \
  -v ".:/usr/src" sonarsource/sonar-scanner-cli \
  -Dsonar.projectKey=java \
  -Dsonar.sources=. \
  -D"sonar.java.binaries=target/classes" \
  -Dsonar.host.url=http://tour-dev.mau-sailfin.ts.net:9000 \
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
