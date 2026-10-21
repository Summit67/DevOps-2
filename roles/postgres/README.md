# Роль postgres

Ставит PostgreSQL из репозиториев Ubuntu, создаёт кластер, базы и пользователей, запускает postgres-exporter. Нужны Ubuntu с systemd, sudo и коллекция community.postgresql из requirements.yml. Проверено на Ubuntu 26.04 с PostgreSQL 18.

## Переменные

Значения по умолчанию находятся в defaults/main.yml, внутренние переменные с __ — в vars/main.yml.

| Переменная | По умолчанию | Для чего |
|---|---|---|
| postgres__version | "18" | Версия PostgreSQL в репозитории Ubuntu |
| postgres__data_dir | /data/postgres/data | Каталог кластера внутри /data/postgres/ |
| postgres__service_name | postgres-hw2 | Имя службы PostgreSQL |
| postgres__opts | Словарь в defaults/main.yml | Параметры postgresql.conf; меняются через lineinfile |
| postgres__hba | Список в defaults/main.yml | Правила pg_hba.conf: type, database, user, address для host, method |
| postgres__login_socket | /var/run/postgresql | Сокет для задач создания БД и пользователей |
| postgres__login_port | postgres__opts.port или 5432 | Порт подключения |
| postgres__users | [] | Пользователи: name, password, необязательный role_attr_flags |
| postgres__databases | [] | Базы: name, необязательные owner и encoding |
| postgres__exporter_version | "0.18.1" | Версия postgres-exporter |
| postgres__exporter_arch | amd64 | Архитектура архива релиза |
| postgres__exporter_listen | 127.0.0.1:9187 | Адрес HTTP-метрик |
| postgres__exporter_service_name | postgres-exporter | Имя службы экспортера |
| postgres__exporter_db_user | postgres_exporter | Пользователь БД с правами pg_monitor |
| postgres__exporter_password | Пустая строка | Обязательный пароль из Vault |
| postgres__exporter_db_host | 127.0.0.1 | Адрес PostgreSQL для экспортера |
| postgres__exporter_database | postgres | База для подключения экспортера |

В postgres__opts строковые значения задаются вместе с одинарными кавычками PostgreSQL, например listen_addresses: "'127.0.0.1'". Числа — без них. При смене сокета нужно согласовать postgres__login_socket и unix_socket_directories в postgres__opts. При смене порта достаточно задать port в postgres__opts.

## Пример плейбука

```
---
- name: Install PostgreSQL
  hosts: vm1
  become: true
  roles:
    - postgres
```

Пример host_vars/vm1.yml:

```
---
postgres__users:
  - name: app_user
    password: "{{ vault_app_password }}"
    role_attr_flags: LOGIN,NOSUPERUSER,NOCREATEDB,NOCREATEROLE
postgres__databases:
  - name: app_db
    owner: app_user
    encoding: UTF8
postgres__exporter_password: "{{ vault_exporter_password }}"
```

vault_app_password и vault_exporter_password хранятся в зашифрованном group_vars/all/encrypted.yml. Задачи с паролями используют no_log. Файл подключения экспортера на целевой ВМ доступен только root.

## Что делает роль

initdb запускается только при отсутствии PG_VERSION. Изменения конфигов вызывают хендлеры перезапуска, изменения unit-файлов — ещё и daemon_reload. Архив экспортера скачивается на контроллере с delegate_to: localhost и become: false, затем бинарник копируется на vm1. Повторный прогон не вносит изменений.

Роль рассчитана на учебную ВМ: стандартный кластер Ubuntu останавливается, данные остаются на месте. Смена postgres__data_dir создаёт другой кластер, существующие данные автоматически не переносит.
