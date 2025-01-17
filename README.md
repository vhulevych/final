[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/xYlUWZVW)
# Final Exam 2024

Ця підсумкова контрольна робота складатиметься з трьох завдань за які можна отримати до 10 балів. Точні бали кожного завдання будутьт наведені в описі. 

Памʼятайте, що репозиторії закриються на запис рівно о 14:51, тому не відкладайте на останній момент заливання робіт. Найкраще працюйте у звичному режимі з невеликими періодичними коммітами.

Три завданні достатньо великі та комплексні, якщо ви не знаєте як виконати якусь частину завдання, то напишіть це та спробуйте зробити завдання без цього. Наприклад, якщо ви не знаєте як прочитати файл, то створіть функцію що повертає рядок із змістом файла та напишіть це в коментарі. Це дозволить оцінити ваші знання більш повно.

Ще пара уточнень:
- Уважно читайте завдання! Чітко слідуйте формату в якому слід виводити чи вводити значення
- Підсумковий код має опинитись в дефолтній гілці вашого репозиторію. Ви можете під час роботи використовувати інші гілки, але код що знаходиться не в `main` не буде оцінено

Бажаємо успіху :)

### Завдання 1
Почнемо із музики. Напишіть програму, що питає у користувача статистику прослуховувань музики. Формат інпуту - один рядок, кожна пісня представляє собою пару значень "виконавець-назва пісні". Пісні розділені між собою крапкою з комою. Програма повинна відповісти на питання:

- Скільки всього різних артистів слухав користувач? Формат аутпуту: "You've listened to N artists!" 
- Яку пісню (назва) користувач слухав найбільшу кількість разів? Формат аутпуту: "Most listented song: "

Програма не повинна "падати" з помилками при будь-якому вводі користувача, замість цього повинна виводити повідомлення `There was an error processing your input. Check format and try once again.`

Приклад інпуту:
```
Bing Crosby-White Christmas; Wham-Last Christmas; Mariah Carey-All I Want for Christmas Is You; Wham-Last Christmas
```

Аутпут:
```
You've listened to 3 artists!
Most listented song: Last Christmas
```

Завдання має бути виконано у файлі `task-1.py`
Максимальна оцінка: 2 бали

### Завдання 2
Різдво - час запису на весняні курси в університеті. За підсумками запису сформовано [наступну таблицю](https://docs.google.com/spreadsheets/d/12PqzCA7jmOBHDMoJt-v695x7sCp35scZoFvEEHS3P-Y/edit?usp=sharing). Кожен рядок представляє один запис одного студента на курс. Ця ж таблиця скачана у форматі .сsv та лежить у папці Data. Напишіть програму що може запускатися з наступними параметрами командного рядка:
```
- course {course_name}
```
Програма має вивести на екран всіх студентів що записані на даний курс, пронумерованими від 1, один запис на рядок. Формат - `{номер}. {Імʼя студента}`
Наприклад:
```
1. James Oliver
2. Trevor Noah
3. Stephen Colbert
```

```
- statistics
```
Програма має вивести на екран 
а) студента що записався на найбільшу кількість курсів
б) середню кількість студентів на курсі
в) найбільш відвідуваний курс

У цьому завданні ви можете (але не зобовʼязані) користуватися Pandas та NumPy
Завдання має бути виконано у файлі `task-2.py`
Максимальна оцінка: 3 бали

### Завдання 3
Останнім завданням перейдемо до святкових рецептів. Вам потрібно написати програму, що дозволяє обробити файли рецептів підготовлених у спеціальному форматі та сформувати список покупок на їх основі. Для початку, подивіться на файли рецептів у папці `Recepies`. Всі вони мають однакову структуру:
- Назва рецепту у першому рядку
- Далі порожній рядок
- Далі заголовок інгредієнтів
- Кожен інгредієнт наведено у форматі "Назва: вага". Вага завжди наведена у грамах або кілограмах (800g, 1kg, 1.5kg etc.)
- Знову порожній рядок
- Інструкції

Напишіть програму що підтримує виконання трьох можливих команд
`prepare {file_name}`
Помітити рецепт до виконання
`show`
Вивести загальний список інгредієнтів до покупки у форматі "Назва: вага". Якщо один і той же інгредієнт зустрічається в деклькох рецептах, має бути виведена сумарна вага у грамах. Якщо якийсь рецепт було додано декілька раз, то кількість інгредієнтів має збільшитись пропорційно.
`exit`
Вийти з програми

Приклад роботи програми:
```
prepare eggnog
prepare eggnog
show
Sugar: 200g
Eggs: 160g
Cream: 400g
Milk: 1000g
Nutmeg: 10g
Cinnamon: 4g
```

Завдання має бути виконано у файлі `task-3.py`
Максимальна оцінка: 5 балів
