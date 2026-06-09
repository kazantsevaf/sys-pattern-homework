# Инструкция по созданию скриншотов для ДЗ

## Задание 1

1. Выполните плейбуки:
```bash
ansible-playbook -i inventory.ini playbook/playbook_archive.yml
ansible-playbook -i inventory.ini playbook/playbook_tuned.yml
ansible-playbook -i inventory.ini playbook/playbook_motd.yml
```

2. Сделайте скриншот вывода каждого плейбука

3. Проверьте результат:
```bash
ls -la /tmp/kafka_extracted/
cat /etc/motd
systemctl status tuned
```

## Задание 2

1. Выполните модифицированный плейбук:
```bash
ansible-playbook -i inventory.ini playbook/playbook_motd.yml
```

2. Проверьте результат:
```bash
cat /etc/motd
```

3. Сделайте скриншот вывода и содержимого файла

## Задание 3

1. Выполните плейбук с ролью:
```bash
ansible-playbook -i inventory.ini playbook/playbook_webserver.yml
```

2. Проверьте веб-страницу:
```bash
curl -I http://127.0.0.1  # Проверка статуса 200
curl http://127.0.0.1     # Проверка содержимого
```

3. Сделайте скриншоты вывода плейбука и веб-страницы

## Как вставить скриншот в README

1. Сохраните скриншот в папку `img/`
2. Добавьте в README:
```markdown
![Описание скриншота](img/имя_файла.png)
```
