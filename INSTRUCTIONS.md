# Инструкция по завершению домашнего задания

## Что нужно сделать самостоятельно

### 1. Установите Ansible (если нет)
```bash
sudo apt update
sudo apt install -y ansible
```

### 2. Выполните плейбуки и сделайте скриншоты

**Задание 1:**
```bash
cd /home/aleksey/sys-pattern-homework

ansible-playbook -i inventory.ini playbook/playbook_archive.yml > output1.txt 2>&1
ansible-playbook -i inventory.ini playbook/playbook_tuned.yml > output2.txt 2>&1
ansible-playbook -i inventory.ini playbook/playbook_motd.yml > output3.txt 2>&1

# Проверка результатов
cat /etc/motd
ls -la /tmp/kafka_extracted/
systemctl status tuned
```

**Задание 2:**
```bash
ansible-playbook -i inventory.ini playbook/playbook_motd.yml
cat /etc/motd
```

**Задание 3:**
```bash
ansible-playbook -i inventory.ini playbook/playbook_webserver.yml
curl http://127.0.0.1
curl -I http://127.0.0.1
```

### 3. Сохраните скриншоты

```bash
# Переместите скриншоты в папку img
cp screenshot_motd.png img/motd_result.png
cp screenshot_webserver.png img/webserver_result.png
```

### 4. Обновите README.md

Замените строки с плейсхолдерами на реальные скриншоты:
```markdown
![Выполнение MOTD плейбука](img/motd_result.png)
![Веб-страница Apache](img/webserver_result.png)
```

### 5. Закоммитьте и отправьте на GitHub
```bash
git add -A
git commit -m "Добавлены реальные скриншоты выполнения"
git push origin main
```

## Чек-лист проверки

- [ ] Установлен Ansible
- [ ] Выполнены все плейбуки без ошибок
- [ ] Сделаны скриншоты вывода
- [ ] Сделаны скриншоты результатов (MOTD, веб-страница)
- [ ] Скриншоты добавлены в папку img/
- [ ] README.md обновлен с реальными скриншотами
- [ ] Все изменения отправлены на GitHub
