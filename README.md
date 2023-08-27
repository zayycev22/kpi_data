# Обработка входных данных для решения кейса "Сбор аналитических данных блога".
### :hammer_and_wrench: Languages and Tools :

<div align="center">
  <img src="https://raw.githubusercontent.com/devicons/devicon/1119b9f84c0290e0f0b38982099a2bd027a48bf1/icons/python/python-original.svg" height="40" width="40">
  <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/pandas/pandas-original.svg" height="40" width="40">
  <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/opencv/opencv-original.svg" height="40" width="40">
  <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/numpy/numpy-original.svg" height="40" width="40">
  <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/pytorch/pytorch-original.svg" height="40" width="40">
  <img src="https://brandeps.com/logo-download/C/CatBoost-logo-vector-01.svg" height="40" width="40">
</div>

## :hammer: Инструменты

Для предварительной обработки изображений была использована библиотека OpenCV.

Для последующей обработки предобработанных изображений была использована баблиотека EasyORC, в случае, если же предобработка не удалась весь текст с изображения передается регрессионной модели, реализованной с помощью библиотеки catboost.

Стоит отметить что выбор данной библиотеки основан на импортозамещении, ведь это отечественная библиотека, разработанная компанией Яндекс в 2022, которая идеально подходит для решения поставленной задачи.

Для реализации [веб-интерфеса](https://github.com/zayycev22/shishka_vision/tree/master) были использованы FastAPI, для создания быстродействующего бэкенда и react, для реализации красивого, интутивно понятного и отзывчивого фронтенда.

## :moyai: Описание алгоритма

В начале мы предобрабатываем входные данные (изображения) и если эта операция прошла успешно, то мы выявляем целевой параметр с предобработанного изображения. Если же предобработать изображение не удалось, то весь текст с изображения мы обрабатываем с помощью преобученной модели Catboost.

На выходе мы получаем значение целевого параметра, который отображаем в web интерфейсе, созданном для демострации возможностей нашего ИТ решения.
