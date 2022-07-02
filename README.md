# 송추 소개 사이트(송추의 지도, 날씨 정보를 확인)
# DevelUP(https://develup.goorm.io/)

- 사용 언어: Python

- 사용 프레임워크: Django

- 프론트앤드 사용 기술: HTML, CSS, JS
- 백엔드 사용 기술: Git, PyOWM, DISQUS, Naver MAP(https://console.ncloud.com/dashboard), uWSGI, Nginx

- 서버: AWS EC2
  - EC2 서버 기본 세팅
    - sudo apt-get update
    - sudo apt-get dist-upgrade
    - sudo apt-get install python3-pip
    - sudo apt install python3-virtualenv

- uWSGI
  - 정적인 웹 서버(Apache / Nginx)와 python으로 작성된 Web Framework(Flask / Django) 사이의 통신을 도와주는 역할
  - 즉, 파이썬 어플리케이션이 웹 서버와 통신하기 위한 명세라고 보면 된다.
  - `Client <-> Nginx <-> uWSGI <-> Django`
  - `uwsgi --http :8080 --home /home/ubuntu/srv/DevelUP-quest1/venv --chdir /home/ubuntu/srv/DevelUP-quest1/ -w config.wsgi`
  - `sudo chown -R ubuntu:ubuntu /var/log/uwsgi/DevelUP/`
  - `uwsgi --ini /home/ubuntu/srv/DevelUP-quest1/config/uwsgi/mysite.ini`

- Nginx
  - `sudo apt-get install nginx`
  - `sudo /etc/init.d/nginx start`
  - `sudo ln -s /etc/nginx/sites-available/mysite_nginx.conf /etc/nginx/sites-enabled/`
  - `python manage.py collectstatic`
  - `sudo /etc/init.d/nginx restart`

- DB: sqlite3

- API를 사용하면서 활용하는 방법을 익혔고, DISQUS를 등록하여 댓글 시스템을 구현하였습니다.

<h1>난제</h1> 
<h2>1. directory index of "/home/ubuntu/srv/DevelUP-quest1/" is forbidden</h2>
<h3>chmod 755 권한 주기 /home/ubuntu (실패)</h3>

<h1>해결</h1>
<h2>root의 경로를 templates까지 추가해주니까 홈페이지는 뜬다</h2>
하지만 templates까지 경로를 주면 HTML CSS JS 가 전부 엉망이 된다..
