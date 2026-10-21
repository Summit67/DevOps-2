# HW2 — Ansible и PostgreSQL

[Репозиторий](https://github.com/Summit67/DevOps-2) · [Роль](https://github.com/Summit67/DevOps-2/tree/main/roles/postgres) · [Плейбук](https://github.com/Summit67/DevOps-2/blob/main/postgres.play.yml)

## Коллекция

Команда (Bash):
```
ansible-galaxy collection install -r requirements.yml
```
Вывод (text):
```
Starting galaxy collection install process
Nothing to do. All requested collections are already installed. If you want to reinstall them, consider using `--force`.
```

## Синтаксис

Команда (Bash):
```
ansible-playbook postgres.play.yml --syntax-check
```
Вывод (text):
```

playbook: postgres.play.yml
```

## Первый прогон

Команда (Bash):
```
cd /home/devops/DevOps-2
ANSIBLE_NOCOLOR=1 ansible-playbook postgres.play.yml 2>&1 | tee logs/01-first-run.txt
```
Вывод (text):
```

PLAY [Install PostgreSQL on vm1] ***********************************************

TASK [Gathering Facts] *********************************************************
ok: [vm1]

TASK [postgres : Check role parameters] ****************************************
ok: [vm1]

TASK [postgres : Install packages from Ubuntu repositories] ********************
changed: [vm1]

TASK [postgres : Disable the default Ubuntu cluster] ***************************
ok: [vm1]

TASK [postgres : Check the Ubuntu cluster startup file] ************************
ok: [vm1]

TASK [postgres : Prevent the default cluster from starting automatically] ******
changed: [vm1]

TASK [postgres : Create /data] *************************************************
changed: [vm1]

TASK [postgres : Create PostgreSQL data directories] ***************************
changed: [vm1] => (item=/data/postgres)
changed: [vm1] => (item=/data/postgres/data)

TASK [postgres : Initialize the database cluster] ******************************
[WARNING]: Module remote_tmp /var/lib/postgresql/.ansible/tmp did not exist and was created with a mode of 0700, this may cause issues when running as another user. To avoid this, create the remote_tmp dir with the correct permissions manually
changed: [vm1]

TASK [postgres : Set PostgreSQL options without replacing other defaults] ******
changed: [vm1] => (item=listen_addresses)
changed: [vm1] => (item=port)
changed: [vm1] => (item=unix_socket_directories)
changed: [vm1] => (item=password_encryption)
changed: [vm1] => (item=max_connections)
changed: [vm1] => (item=shared_buffers)

TASK [postgres : Configure client authentication] ******************************
changed: [vm1]

TASK [postgres : Install the PostgreSQL service] *******************************
changed: [vm1]

TASK [postgres : Apply configuration before checking PostgreSQL] ***************

RUNNING HANDLER [postgres : Reload systemd] ************************************
ok: [vm1]

RUNNING HANDLER [postgres : Restart PostgreSQL] ********************************
changed: [vm1]

TASK [postgres : Enable and start PostgreSQL] **********************************
changed: [vm1]

TASK [postgres : Check PostgreSQL readiness] ***********************************
ok: [vm1]

TASK [postgres : Run SELECT 1] *************************************************
ok: [vm1]

TASK [postgres : Show SELECT 1 result] *****************************************
ok: [vm1] => {
    "__select_result.query_result": [
        {
            "result": 1
        }
    ]
}

TASK [postgres : Create database users] ****************************************
changed: [vm1] => (item=(censored due to no_log))

TASK [postgres : Create user databases] ****************************************
changed: [vm1] => (item={'name': 'app_db', 'owner': 'app_user', 'encoding': 'UTF8'})
changed: [vm1] => (item={'name': 'test_db', 'owner': 'app_user', 'encoding': 'UTF8'})

TASK [postgres : Create the exporter database user] ****************************
changed: [vm1]

TASK [postgres : Give pg_monitor to the exporter] ******************************
changed: [vm1]

TASK [postgres : Create the download directory] ********************************
changed: [vm1 -> localhost]

TASK [postgres : Download the exporter archive] ********************************
changed: [vm1 -> localhost]

TASK [postgres : Unpack the exporter] ******************************************
changed: [vm1 -> localhost]

TASK [postgres : Create a system user for the exporter] ************************
changed: [vm1]

TASK [postgres : Copy the exporter binary to vm1] ******************************
changed: [vm1]

TASK [postgres : Configure exporter connection] ********************************
changed: [vm1]

TASK [postgres : Install the exporter service] *********************************
changed: [vm1]

TASK [postgres : Apply the exporter service configuration] *********************

RUNNING HANDLER [postgres : Reload systemd] ************************************
ok: [vm1]

RUNNING HANDLER [postgres : Restart postgres-exporter] *************************
changed: [vm1]

TASK [postgres : Enable and start postgres-exporter] ***************************
changed: [vm1]

PLAY RECAP *********************************************************************
vm1                        : ok=32   changed=23   unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
```

## Повторный прогон

Команда (Bash):
```
ANSIBLE_NOCOLOR=1 ansible-playbook postgres.play.yml 2>&1 | tee logs/02-second-run.txt
```
Вывод (text):
```

PLAY [Install PostgreSQL on vm1] ***********************************************

TASK [Gathering Facts] *********************************************************
ok: [vm1]

TASK [postgres : Check role parameters] ****************************************
ok: [vm1]

TASK [postgres : Install packages from Ubuntu repositories] ********************
ok: [vm1]

TASK [postgres : Disable the default Ubuntu cluster] ***************************
ok: [vm1]

TASK [postgres : Check the Ubuntu cluster startup file] ************************
ok: [vm1]

TASK [postgres : Prevent the default cluster from starting automatically] ******
ok: [vm1]

TASK [postgres : Create /data] *************************************************
ok: [vm1]

TASK [postgres : Create PostgreSQL data directories] ***************************
ok: [vm1] => (item=/data/postgres)
ok: [vm1] => (item=/data/postgres/data)

TASK [postgres : Initialize the database cluster] ******************************
ok: [vm1]

TASK [postgres : Set PostgreSQL options without replacing other defaults] ******
ok: [vm1] => (item=listen_addresses)
ok: [vm1] => (item=port)
ok: [vm1] => (item=unix_socket_directories)
ok: [vm1] => (item=password_encryption)
ok: [vm1] => (item=max_connections)
ok: [vm1] => (item=shared_buffers)

TASK [postgres : Configure client authentication] ******************************
ok: [vm1]

TASK [postgres : Install the PostgreSQL service] *******************************
ok: [vm1]

TASK [postgres : Apply configuration before checking PostgreSQL] ***************

TASK [postgres : Enable and start PostgreSQL] **********************************
ok: [vm1]

TASK [postgres : Check PostgreSQL readiness] ***********************************
ok: [vm1]

TASK [postgres : Run SELECT 1] *************************************************
ok: [vm1]

TASK [postgres : Show SELECT 1 result] *****************************************
ok: [vm1] => {
    "__select_result.query_result": [
        {
            "result": 1
        }
    ]
}

TASK [postgres : Create database users] ****************************************
ok: [vm1] => (item=(censored due to no_log))

TASK [postgres : Create user databases] ****************************************
ok: [vm1] => (item={'name': 'app_db', 'owner': 'app_user', 'encoding': 'UTF8'})
ok: [vm1] => (item={'name': 'test_db', 'owner': 'app_user', 'encoding': 'UTF8'})

TASK [postgres : Create the exporter database user] ****************************
ok: [vm1]

TASK [postgres : Give pg_monitor to the exporter] ******************************
ok: [vm1]

TASK [postgres : Create the download directory] ********************************
ok: [vm1 -> localhost]

TASK [postgres : Download the exporter archive] ********************************
ok: [vm1 -> localhost]

TASK [postgres : Unpack the exporter] ******************************************
skipping: [vm1]

TASK [postgres : Create a system user for the exporter] ************************
ok: [vm1]

TASK [postgres : Copy the exporter binary to vm1] ******************************
ok: [vm1]

TASK [postgres : Configure exporter connection] ********************************
ok: [vm1]

TASK [postgres : Install the exporter service] *********************************
ok: [vm1]

TASK [postgres : Apply the exporter service configuration] *********************

TASK [postgres : Enable and start postgres-exporter] ***************************
ok: [vm1]

PLAY RECAP *********************************************************************
vm1                        : ok=27   changed=0    unreachable=0    failed=0    skipped=1    rescued=0    ignored=0
```

## Службы

Команда (Bash):
```
ansible vm1 -b -m command -a 'systemctl is-active postgres-hw2 postgres-exporter'
```
Вывод (text):
```
vm1 | CHANGED | rc=0 >>
active
active
```

## Автозапуск

Команда (Bash):
```
ansible vm1 -b -m command -a 'systemctl is-enabled postgres-hw2 postgres-exporter'
```
Вывод (text):
```
vm1 | CHANGED | rc=0 >>
enabled
enabled
```

## SELECT 1

Команда (Bash):
```
ansible vm1 -b --become-user postgres -m command -a 'psql -c "SELECT 1"'
```
Вывод (text):
```
vm1 | CHANGED | rc=0 >>
 ?column? 
----------
        1
(1 row)
```

## Базы данных

Команда (Bash):
```
ansible vm1 -b --become-user postgres -m command -a 'psql -c "\l"'
```
Вывод (text):
```
vm1 | CHANGED | rc=0 >>
                                                     List of databases
   Name    |  Owner   | Encoding | Locale Provider |   Collate   |    Ctype    | Locale | ICU Rules |   Access privileges   
-----------+----------+----------+-----------------+-------------+-------------+--------+-----------+-----------------------
 app_db    | app_user | UTF8     | libc            | en_US.UTF-8 | en_US.UTF-8 |        |           | 
 postgres  | postgres | UTF8     | libc            | en_US.UTF-8 | en_US.UTF-8 |        |           | 
 template0 | postgres | UTF8     | libc            | en_US.UTF-8 | en_US.UTF-8 |        |           | =c/postgres          +
           |          |          |                 |             |             |        |           | postgres=CTc/postgres
 template1 | postgres | UTF8     | libc            | en_US.UTF-8 | en_US.UTF-8 |        |           | =c/postgres          +
           |          |          |                 |             |             |        |           | postgres=CTc/postgres
 test_db   | app_user | UTF8     | libc            | en_US.UTF-8 | en_US.UTF-8 |        |           | 
(5 rows)
```

## Пользователи

Команда (Bash):
```
ansible vm1 -b --become-user postgres -m command -a 'psql -c "\du"'
```
Вывод (text):
```
vm1 | CHANGED | rc=0 >>
                                 List of roles
     Role name     |                         Attributes                         
-------------------+------------------------------------------------------------
 app_user          | 
 postgres          | Superuser, Create role, Create DB, Replication, Bypass RLS
 postgres_exporter |
```

## Метрики

Команда (Bash):
```
ansible vm1 -m uri -a 'url=http://127.0.0.1:9187/metrics return_content=true' | grep -o 'pg_up 1'
```
Вывод (text):
```
pg_up 1
```

## Каталог данных

Команда (Bash):
```
ansible vm1 -b --become-user postgres -m command -a 'psql -c "SHOW data_directory"'
```
Вывод (text):
```
vm1 | CHANGED | rc=0 >>
   data_directory    
---------------------
 /data/postgres/data
(1 row)
```

## Права каталогов

Команда (Bash):
```
ansible vm1 -b -m command -a 'stat -c %a:%U:%G:%n /data /data/postgres /data/postgres/data'
```
Вывод (text):
```
vm1 | CHANGED | rc=0 >>
755:root:root:/data
700:postgres:postgres:/data/postgres
700:postgres:postgres:/data/postgres/data
```

## Права экспортера

Команда (Bash):
```
sudo -u postgres psql -c "SELECT pg_has_role('postgres_exporter', 'pg_monitor', 'member') AS pg_monitor;"
```
Вывод (text):
```
 pg_monitor 
------------
 t
(1 row)
```

