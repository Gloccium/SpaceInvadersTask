# Игра "Space Invaders"

Версия 1

Авторы: Сергеев Егор, Пермяков Артем

# Описание

Реализация аркадной игры "Space Invaders" с некоторыми нововведениями,
используется по прямому назначению

# Требования

Python версии 3.8 и выше

Установленная библиотека Pygame

# Состав

Графическая версия: main.py

Модули: essentials/

UI: interface/

# Графическая версия

Пример запуска: ./main.py

# Управление

Для передвижения используйте клавиши (←, →) или (A, D)

Для стрельбы лазером по прямой используйте SPACE

Для стрельбы лазером по диагонали влево используйте Q, вправо — E

P - поставить игру на паузу

# Подробности реализации

Модули, отвечающие за побочную логику игрока, пришельцев, препятствий и
лазера, а также за их визуал — расположены в пакете essentials.

Также в нем расположен модуль для смены игровых состояний, модуль для
экранов: начального, финального, экранов паузы и таблицы лидеров

В качестве пасхалки реализован модуль для предания игре эффекта помех,
как у старого телевизора

В основе всей игры лежит класс Game, реализующий основную логику
всех вышеперечисленных игровых сущностей
