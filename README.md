# DevOps - HW2

Ansible-роль для PostgreSQL и postgres-exporter. Выполнено на моем Ubuntu 26.04, поставил PostgreSQL 18 и Ansible core 2.20.1.

Для ориентировки:
- [Роль](roles/postgres/)
- [Плейбук](postgres.play.yml)
- [Отчёт с выводом команд](HW2_Ansible_PostgreSQL.md)
- [Переменные роли](roles/postgres/README.md)

## Запуск

Команды выполняются на Linux. У меня Ansible и vm1 - одна ВМ, подключение идёт по SSH к 127.0.0.1 под devops. Нужны SSH ключ и sudo без пароля; адрес, пользователя и ключ можно поменять в inventories/main/hosts.yaml.

```
sudo apt update
sudo apt install -y ansible acl
git clone https://github.com/Summit67/DevOps-2.git
cd DevOps-2
ansible-galaxy collection install -r requirements.yml
```

Пароли был зашифрованы в inventories/main/group_vars/all/encrypted.yml. Файл vault-pass с паролем Vault я исключил из Git'а. 
Для своего запуска:

```
umask 077
openssl rand -base64 32 > vault-pass
rm inventories/main/group_vars/all/encrypted.yml
ansible-vault create inventories/main/group_vars/all/encrypted.yml
```

В редакторе Vault два ключа со своими паролями: vault_app_password и vault_exporter_password, потом:

```
ansible-playbook postgres.play.yml --syntax-check
ansible-playbook postgres.play.yml
ansible-playbook postgres.play.yml
```

PostgreSQL работает через postgres-hw2.service, данные в /data/postgres/data. Стандартный кластер Ubuntu остановлен и отключён. Экспортер работает через postgres-exporter.service, метрики — http://127.0.0.1:9187/metrics. Создаются app_user, базы app_db и test_db, пользователь postgres_exporter с pg_monitor.

## Проверка

```
ansible vm1 -b -m command -a 'systemctl is-active postgres-hw2 postgres-exporter'
ansible vm1 -b --become-user postgres -m command -a 'psql -c "SELECT 1"'
curl -s http://127.0.0.1:9187/metrics | grep '^pg_up '
```

Первый прогон: changed=23, failed=0. Второй: changed=0, failed=0. Полный вывод обоих запусков и проверок - в отчёте.
