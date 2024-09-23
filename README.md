# sonar qube

## sonar scanner

```
docker run --rm -e SONAR_HOST_URL="http://host.docker.internal:9000"  -v ".:/usr/src" sonarsource/sonar-scanner-cli -D"sonar.projectKey=hello2" -D"sonar.sources=." -D"sonar.host.url=http://host.docker.internal:9000" -D"sonar.token=CHANGEIT"
```
