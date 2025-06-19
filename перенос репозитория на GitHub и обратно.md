##### **перенос репозитория на GitHub**
###### **с созданием репозитория на GitHub**
- Открой GitHub
- Нажми "New repository", ввести имя (seychas, без кириллицы), Нажми "Create repository" 
- $ cd "/d/Obsidian/seychas/Python_for_Data_Science" - в Git Bash переходим в папку которую будем клонировать
- $ git init - если папка не инициирована
- $ git add .
- $ git commit -m "1 day"
- $ git remote add origin https://github.com/Serg591962/Python_for_Data_Science.git
- $ git branch -M main
- $ git push -u origin main => перенос файлов на гитхаб
###### **без создания репозитория на GitHub**
- Открой GitHub
- $ cd "/d/Obsidian/seychas/Python_for_Data_Science" - в Git Bash переходим в папку которую будем клонировать
- $ git remote -v - проверить, связан ли локальный репозиторий с удалённым. Если нет git git remote add origin https://github.com/Serg591962/Python_for_Data_Science.git
- $ git add .
- $ git commit -m "2 day"
- $ git push -u origin main => перенос файлов на гитхаб
###### **обновление репозитория на GitHub**
- Открой GitHub
- $ cd "/d/Obsidian/seychas/Python_for_Data_Science" - в Git Bash переходим в папку которую будем клонировать
- $ git remote -v - проверить, связан ли локальный репозиторий с удалённым. Если нет git remote add origin  https://github.com/Serg591962/Python_for_Data_Science.git
- $ git add .
- $ git commit -m "2 day"
- $ git push origin main => обновить файлы на гитхаб
###### **клонировать репозиторий на компьютер**
- Перейди на страницу твоего репозитория на GitHub
- Открыть Git Bash на новом компьютере в том месте, где будет сохранен проект:  cd "/d/Obsidian/seychas" - 
- Введи команду для клонирования репозитория: git clone https://github.com/Serg591962/Python_for_Data_Science.git
###### **обновление репозитория на компьютере**
- Перейти в репозиторий: cd d:Obsidian/seychas/Python_for_Data_Science
- Проверить, связан ли локальный репозиторий с удалённым: git remote -v
- Ввести команду обновления уже клонированного репозитория git pull origin main







пароль Cthutq36226

cd "/d/Obsidian/seychas/zaryadka"
git clone https://github.com/Serg591962/zaryadka.git