<div style = "display: inline-flex; "> 

<img src="https://sun9-14.userapi.com/impg/c855016/v855016794/1bbc91/s55qKIJiqnU.jpg?size=489x400&quality=96&sign=8d793bf6542603785fc760660fd427d3&type=album" height="100"/>

<h2 style = "margin-left: 25px"> Тестовое задание на курс «Python» </h2>

</div>

<div style = "margin-top: 25px; font-family:arial; font-style: italic; ">
Проект REST-сервис реализован на FastAPI без фронтенда, по этому к API будем обращать либо через Swagger, либо через реквесты, зависимости зафиксированы менеджером зависимостей Poetry, написаны тесты с использованием Pytest, реализована возможность собирать и запускать контейнер с сервисом в Docker. 
<br><br>
Для получения информации о заработной плате работника и иных данных нужно авторизоваться в сервисе, введя почту и пароль, после чего, если все верно, получим token, действующий 30 секунд. Данный token потребуется нам, чтобы пройти HTTPBearer, функция auth_wrapper класса AuthHandler декодирует токен и возвращает нам почту работника, если токен валидный. После чего функция сервиса API "Protected" возвращает данные работника связанные с нашей почтой.
</div>

<div style = "margin-top: 25px; margin-left: 25px;">

1. Клонируем проект с репозитория  <br> 
<p style = "margin-left: 100px; text-align:center; background-color: hsla(0, 0%, 0%, .1); width:450px"> 
git clone https://github.com/TortureGG/fastapi_poetry_docker.git</p>


2. Запуск через Docker запускаем Dockerfile: <br>

<div style = "margin-left: 50px;">

Создаем Image:
<p style = "margin-left: 100px; text-align:center; background-color: hsla(0, 0%, 0%, .1); width:250px"> 
docker build -t image . </p>
Создаем Container с портом 80:
<p style = "margin-left: 100px; text-align:center; background-color: hsla(0, 0%, 0%, .1); width:250px">
docker run -p 80:80 image </p> 
Переходим к Swagger по ссылке и можем взаимодействовать с сервисом

<p style = "margin-left: 100px; text-align:center; background-color: hsla(0, 0%, 0%, .1); width:250px"><a href="http://localhost:80/docs">http://localhost:80/docs</a>
<a href="http://127.0.0.1:80/docs">http://127.0.0.1:80/docs</a></p> 
</div>

3. Запуск  можем через Poetry (необходимо предварительно установиться pip install poetry и указать путь), переходим в папку project, где находится файил с зависимостями pyproject.toml

<p style = "margin-left: 150px; text-align:center;  background-color: hsla(0, 0%, 0%, .1); width:250px"> 
cd project<br>
poetry install<br>
poetry run python main.py
<a href="http://localhost:80/docs">http://localhost:80/docs</a>
<a href="http://127.0.0.1:80/docs">http://127.0.0.1:80/docs</a></p>
</p>

4. Тесты находятся в папке project/pytest/tests.py но предварительно нужно 
запустить REST-сервис, запускать их будетм командой: <br>
<p style = "margin-left: 150px; text-align:center; background-color: hsla(0, 0%, 0%, .1); width:250px">
poetry run pytest pytest/tests.py  </p> 
</div>   

    Задание:
    Реализуйте REST-сервис просмотра текущей зарплаты и даты следующего
    повышения. Из-за того, что такие данные очень важны и критичны, каждый
    сотрудник может видеть только свою сумму. Для обеспечения безопасности, вам
    потребуется реализовать метод где по логину и паролю сотрудника будет выдан
    секретный токен, который действует в течение определенного времени. Запрос
    данных о зарплате должен выдаваться только при предъявлении валидного токена.
        ● сервис реализован на FastAPI;
        ● зависимости зафиксированы менеджером зависимостей poetry;
        ● написаны тесты с использованием pytest;
        ● реализована возможность собирать и запускать контейнер с сервисом в   Docker.
