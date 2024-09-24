# jenkins

## docker compose

```
docker compose up -d
```

## initial password

```
docker exec jenkins cat /var/jenkins_home/secrets/initialAdminPassword
```

jenkins: http://tour-dev.mau-sailfin.ts.net:58080
sonaqube: http://tour-dev.mau-sailfin.ts.net:9000


![first login](image.png)
![initial setup](image-1.png)
![install plugins](image-2.png)
![add admin user](image-3.png)
![instance configuration](image-4.png)
![jenkins ready](image-5.png)
![dashboard](image-6.png)


## integrate with sonarqube

![plugins](image-7.png)
![install sonarqube plugin](image-8.png)

![restart jenkins](image-9.png)

## jenkins helloworld

![helloworld](image-10.png)
![configure](image-11.png)
![project main](image-12.png)
