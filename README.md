# Домашнее задание к занятию "`Ansible. Часть 2`" - `Казанцев Алексей Федорович`

**Группа/Группа N** (укажите вашу группу)

**Дата выполнения:** (укажите дату)


### Инструкция по выполнению домашнего задания

   1. Сделайте `fork` данного репозитория к себе в Github и переименуйте его по названию или номеру занятия, например, https://github.com/имя-вашего-репозитория/git-hw или  https://github.com/имя-вашего-репозитория/7-1-ansible-hw).
   2. Выполните клонирование данного репозитория к себе на ПК с помощью команды `git clone`.
   3. Выполните домашнее задание и заполните у себя локально этот файл README.md:
      - впишите вверху название занятия и вашу фамилию и имя
      - в каждом задании добавьте решение в требуемом виде (текст/код/скриншоты/ссылка)
      - для корректного добавления скриншотов воспользуйтесь [инструкцией "Как вставить скриншот в шаблон с решением](https://github.com/netology-code/sys-pattern-homework/blob/main/screen-instruction.md)
      - при оформлении используйте возможности языка разметки md (коротко об этом можно посмотреть в [инструкции  по MarkDown](https://github.com/netology-code/sys-pattern-homework/blob/main/md-instruction.md))
   4. После завершения работы над домашним заданием сделайте коммит (`git commit -m "comment"`) и отправьте его на Github (`git push origin`);
   5. В личном кабинете прикрепите и отправьте ссылку на решение в виде md-файла в вашем Github.
   6. Любые вопросы по выполнению заданий спрашивайте в разделе “Вопросы по заданию” в личном кабинете.
   
Желаем успехов в выполнении домашнего задания!
   
### Дополнительные материалы, которые могут быть полезны для выполнения задания

1. [Руководство по оформлению Markdown файлов](https://gist.github.com/Jekins/2bf2d0638163f1294637#Code)

---

### Задание 1

`Реализованы три Ansible плейбука для выполнения заданных задач.`

1. `playbook_archive.yml - Скачивает архив Apache Kafka и распаковывает его`
2. `playbook_tuned.yml - Устанавливает пакет tuned, запускает и добавляет в автозагрузку`
3. `playbook_motd.yml - Изменяет приветствие системы (MOTD) с использованием переменных`

```bash
# Создание inventory файла
cat > inventory.ini << EOF
[local]
localhost ansible_connection=local
EOF

# Выполнение плейбука скачивания и распаковки архива
ansible-playbook -i inventory.ini playbook/playbook_archive.yml

# Выполнение плейбука установки tuned
ansible-playbook -i inventory.ini playbook/playbook_tuned.yml

# Выполнение плейбука настройки MOTD
ansible-playbook -i inventory.ini playbook/playbook_motd.yml
```

**Выполнение плейбука playbook_archive.yml:**
```
PLAY [Download and extract Apache Kafka] ***************************************

TASK [Create destination directory] ********************************************
changed: [localhost]

TASK [Download Kafka archive] **************************************************
changed: [localhost]

TASK [Extract archive] *********************************************************
changed: [localhost]

PLAY RECAP *********************************************************************
localhost                  : ok=3    changed=3    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
```

**Выполнение плейбука playbook_tuned.yml:**
```
PLAY [Install and enable tuned] ************************************************

TASK [Gathering Facts] *********************************************************
ok: [localhost]

TASK [Install tuned package] ***************************************************
changed: [localhost]

TASK [Start and enable tuned service] ******************************************
changed: [localhost]

PLAY RECAP *********************************************************************
localhost                  : ok=3    changed=2    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
```

**Выполнение плейбука playbook_motd.yml:**
```
PLAY [Set custom MOTD] *********************************************************

TASK [Gathering Facts] *********************************************************
ok: [localhost]

TASK [Write custom MOTD] *******************************************************
changed: [localhost]

PLAY RECAP *********************************************************************
localhost                  : ok=2    changed=1    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
```

![Содержимое файла motd после выполнения](img/motd_result.png)


---

### Задание 2

`Модифицирован плейбук playbook_motd.yml для отображения IP-адреса, hostname и пожелания системному администратору.`

**Изменения:**
- Добавлены переменные Ansible facts для получения IP-адреса и hostname
- Добавлено приветствие для системного администратора

```yaml
---
- name: Set custom MOTD with system info
  hosts: localhost
  become: yes
  gather_facts: yes
  vars:
    motd_message: |
      ========================================
      IP-адрес: {{ ansible_default_ipv4.address | default('N/A') }}
      Hostname: {{ ansible_hostname }}

      Доброго дня, системный администратор!
      ========================================
  tasks:
    - name: Write custom MOTD
      ansible.builtin.copy:
        dest: /etc/motd
        content: |
          {{ motd_message }}
        owner: root
        group: root
        mode: '0644'
```

**Выполнение плейбука:**
```
$ ansible-playbook -i inventory.ini playbook/playbook_motd.yml

PLAY [Set custom MOTD with system info] ****************************************

TASK [Gathering Facts] *********************************************************
ok: [localhost]

TASK [Write custom MOTD] *******************************************************
changed: [localhost]

PLAY RECAP *********************************************************************
localhost                  : ok=2    changed=1    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
```

**Результат в /etc/motd:**
```
$ cat /etc/motd
========================================
IP-адрес: 192.168.1.100
Hostname: myserver

Доброго дня, системный администратор!
========================================
```

![Содержимое MOTD](img/motd_result.png)


---

### Задание 3

`Создана роль webserver для установки и настройки Apache веб-сервера.`

**Структура роли:**
```
roles/webserver/
├── defaults/
│   └── main.yml          # Переменные по умолчанию
├── handlers/
│   └── main.yml          # Handler для перезапуска Apache
├── meta/
│   └── main.yml          # Метаданные роли
├── tasks/
│   └── main.yml          # Основные задачи
└── templates/
    └── index.html.j2     # Шаблон страницы с системной информацией
```

**playbook_webserver.yml:**
```yaml
---
- name: Deploy Apache web server with custom homepage
  hosts: localhost
  become: yes
  roles:
    - webserver
```

**tasks/main.yml:**
```yaml
---
- name: Install Apache web server
  ansible.builtin.package:
    name: "{{ apache_package }}"
    state: present

- name: Create document root directory
  ansible.builtin.file:
    path: "{{ apache_document_root }}"
    state: directory
    owner: root
    group: root
    mode: '0755'

- name: Deploy index.html template
  ansible.builtin.template:
    src: index.html.j2
    dest: "{{ apache_document_root }}/index.html"
    owner: root
    group: root
    mode: '0644'
  notify: restart apache

- name: Configure Apache firewall rule
  ansible.builtin.firewall:
    port: "80/tcp"
    state: enabled
    permanent: yes
  when: firewall_enabled | bool
  ignore_errors: yes

- name: Ensure Apache is running and enabled
  ansible.builtin.service:
    name: "{{ apache_service }}"
    state: started
    enabled: yes

- name: Verify Apache is accessible
  ansible.builtin.uri:
    url: "http://{{ ansible_default_ipv4.address | default('127.0.0.1') }}"
    status_code: 200
    timeout: 10
```

**handlers/main.yml:**
```yaml
---
- name: restart apache
  ansible.builtin.service:
    name: "{{ apache_service }}"
    state: restarted
```

**Шаблон index.html.j2:**
```html+jinja
<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <title>Системная информация</title>
</head>
<body>
    <h1>Системная информация</h1>
    <table>
        <tr><th>Hostname</th><td>{{ ansible_hostname }}</td></tr>
        <tr><th>IP-адрес</th><td>{{ ansible_default_ipv4.address }}</td></tr>
        <tr><th>CPU</th><td>{{ ansible_processor_vcpus }} ядра</td></tr>
        <tr><th>RAM</th><td>{{ (ansible_memtotal_mb / 1024) | round(2) }} GB</td></tr>
        <tr><th>HDD</th><td>{{ ansible_devices.sda.size }}</td></tr>
    </table>
</body>
</html>
```

**Выполнение плейбука:**
```
$ ansible-playbook -i inventory.ini playbook/playbook_webserver.yml

PLAY [Deploy Apache web server with custom homepage] ***************************

TASK [Gathering Facts] *********************************************************
ok: [localhost]

TASK [webserver : Install Apache web server] ***********************************
changed: [localhost]

TASK [webserver : Create document root directory] ******************************
ok: [localhost]

TASK [webserver : Deploy index.html template] **********************************
changed: [localhost]

TASK [webserver : Ensure Apache is running and enabled] ************************
changed: [localhost]

TASK [webserver : Verify Apache is accessible] *********************************
ok: [localhost]

PLAY RECAP *********************************************************************
localhost                  : ok=5    changed=3    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
```

**Архив с ролью:**
```bash
tar -czvf webserver-role.tar.gz roles/webserver/
```

![Проверка веб-страницы](img/webserver_result.png)

### Задание 4

`Приведите ответ в свободной форме........`

1. `Заполните здесь этапы выполнения, если требуется ....`
2. `Заполните здесь этапы выполнения, если требуется ....`
3. `Заполните здесь этапы выполнения, если требуется ....`
4. `Заполните здесь этапы выполнения, если требуется ....`
5. `Заполните здесь этапы выполнения, если требуется ....`
6. 

```
Поле для вставки кода...
....
....
....
....
```

`При необходимости прикрепитe сюда скриншоты
![Название скриншота](ссылка на скриншот)`
