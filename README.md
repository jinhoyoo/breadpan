Bread pan
========

기본적인 웹서비스를 간단하게 만드는 프로젝트 틀. 이 프로젝트를 Clone해서 이름을 바꿔서 진행하기를 권장한다. 

<img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQf-dHcXXifrSmL6RBJG5hdggKjvlcko0Or4IZW2j-myy2kTUbD&s" width="500px" title="Bread pan" alt="BreadPan"/>


Tech Stack 
--------
- Front-end
   * React
   * Typescript
   * SAAS

- Back-end 
  * Python 3.x
  * Flask

- Automation 
  * make

Folder structure
-------
* Clean architecture[[en](https://blog.cleancoder.com/uncle-bob/2012/08/13/the-clean-architecture.html)/[kr](https://blog.coderifleman.com/2017/12/18/the-clean-architecture/)]의 기본 개넘에 따라, 최대한 정책에 집중하고 세부사항은 다양하게 될 수 있도록 한다.

```
├── backend  : Back-end 프로젝트
│   ├── Makefile
│   ├── README.md
│   ├── breadpan  : 기본 Framework
│   ├── todo      : breadpan을 기반으로 만든 간단한 todo 예제
│   ├── tests     : Test code
│   └── apps      : todo 예제를 가지고 다양한 형태로 만든 예제. (현재는 Flask기반 WebApp)
│  
├── frontend
│   ├── Makefile
│   ├── README.md

```

