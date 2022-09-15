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

TAB - начать игру или перезапустить игру в случае смерти игрока

Для передвижения используйте клавиши (←, →) или (A, D)

Для стрельбы лазером используйте SPACE

# Подробности реализации

Модули, отвечающие за побочную логику игрока, пришельцев, препятствий и
лазера, а также за их визуал — расположены в пакете essentials.

Также в нем расположен модуль для смены игровых состояний, модуль для
экранов(начального и финального), и модуль-пасхалка для предания игре
эффекта помех, как у старого телевизора

В основе всей игры лежит класс Game, реализующий основную логику всех выше
перечисленных игровых сущностей
