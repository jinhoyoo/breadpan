서비스를 구현 하는 방법
===========

Breadpan이 지향하는 기본 구조는 Clean architecture에서 주장하는 기본 개념들을 최대한 이용한다. 

```plantuml
@startuml component
actor client
node app
database db

db -> app
app -> client
@enduml
```



![PlantUML model](http://plantuml.com:80/plantuml/png/3SNB4K8n2030LhI0XBlTy0YQpF394D2nUztBtfUHrE0AkStCVHu0WP_-MZdhgiD1RicMdLpXMJCK3TC3o2iEDwHSxvNVjWNDE43nv3zt731SSLbJ7onzbyeF)