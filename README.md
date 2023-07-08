# work02008
Если вы будете запускать на линукс то будет достаточно прописать make start
А если вы на windows, то вот инструкции:
-python3/python/py(в зависимотсти от версии) -m .venv
-активировать если это требуется
-pip install -r requirments.txt
-docker-compose up
-flask db upgrade
-flask run

Постле этого на главном окне будет две гиперссылки посмотреть содержимое таблицы или создать для ее строку новую
![image](https://github.com/CHAMOMI1E/work02008/assets/118203026/e6616763-4144-40d6-abda-ae1d15246ddb)

Если вы нажмёте Create JSON, то будет дана строка для ввода и 2 кнопки("Добавить"-для добавления нового input и "create"-для отправки формы)

![image](https://github.com/CHAMOMI1E/work02008/assets/118203026/6512709a-e490-4c5f-a63d-673f42c76aaa)

Вы можете добавить много таких полей, но желательно их все заполнять(ошибки не будет, но json будет на половину не заполнен)
![image](https://github.com/CHAMOMI1E/work02008/assets/118203026/0df0321a-982d-434a-9bfe-3e20645cfff1)

Результат будет выводится на экране в формате json
![image](https://github.com/CHAMOMI1E/work02008/assets/118203026/ba905df6-f99a-45ad-ace0-033ff09537d5)

В этой программк бд создает docker, так что не надо создавать бд ввручную.
