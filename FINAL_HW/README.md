# FINAL_HW. audit-svc

GitHub Actions собирает образ и публикует его в `ghcr.io/summit67/audit-svc`.
Ветка main запускает тесты и сборку; защищённые теги vX.Y.Z дополнительно запускают Ansible на Ubuntu через self-hosted runner с меткой deploy.

- [Отчёт](REPORT.md)
- [Описание сервиса](SERVICE.md)
- [Развёртывание](deploy/audit-svc.play.yml)
- [Мониторинг](monitoring/)

Образ запускается от UID 10001. Версия Python закреплена digest, время сборки задано SOURCE_DATE_EPOCH, создание pyc отключено. Поэтому изменение только vault.yml не меняет образ. Контейнер сравнивается по Image ID, а конфиг монтируется каталогом: atomic rename из Ansible виден приложению. Хендлер вызывает /reload без перезапуска.

PostgreSQL и приложение находятся в закрытой сети audit-backend. Nginx подключён также к audit-edge, принимает запросы на 127.0.0.1:8088 и закрывает /reload. Prometheus подключён только к audit-edge и собирает метрики приложения через Nginx.

Миграции выполняются перед обновлением приложения. Ошибка миграции останавливает плейбук. Повторное применение схемы не считается изменением.

Повторный запуск на ВМ из каталога deploy (ключ Vault передаётся окружением):
```
chmod +x vault-pass.sh
ansible-playbook audit-svc.play.yml --vault-password-file ./vault-pass.sh -e audit_image_tag=v1.0.2
```

Мониторинг:
```
cd monitoring
docker compose up -d
```

Grafana: 127.0.0.1:13001, Prometheus: 127.0.0.1:19091. Grafana разрешает только просмотр без входа и доступна через loopback.

Для FINAL_HW остановлены кластер HW4 и мониторинг HW3, их данные сохранены.
JSON Nginx взят из [nginx-prometheus-exporter](https://github.com/nginx/nginx-prometheus-exporter/blob/main/grafana/dashboard.json).
