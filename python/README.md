# python

## install dependencies
```sh
python3 -m venv venv
. venv/bin/activate
pip install coverage

```

## sonar scanner
```sh
docker run --rm -e SONAR_HOST_URL="http://tour-dev.mau-sailfin.ts.net:9000" -v ".:/usr/src" sonarsource/sonar-scanner-cli \
-D"sonar.projectKey=helloworld" \
-D"sonar.sources=." \
-D"sonar.host.url=http://tour-dev.mau-sailfin.ts.net:9000" \
-D"sonar.token=sqp_125a4353faca3d67b65b1261279226da1b6e70e0" 
```

## coverage

```sh
coverage run -m unittest discover
coverage xml -o coverage.xml
```

```sh
docker run --rm \
-e SONAR_HOST_URL="http://tour-dev.mau-sailfin.ts.net:9000" \
-v ".:/usr/src" \
sonarsource/sonar-scanner-cli \
-D"sonar.projectKey=helloworld" \
-D"sonar.sources=." \
-D"sonar.host.url=http://tour-dev.mau-sailfin.ts.net:9000" \
-D"sonar.token=sqp_125a4353faca3d67b65b1261279226da1b6e70e0" \
-D"sonar.python.coverage.reportPaths=coverage.xml"
```
