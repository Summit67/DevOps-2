# HW4. Counter в Kubernetes

Репозиторий: [Summit67/DevOps-2](https://github.com/Summit67/DevOps-2/tree/main/HW4).

Работа выполнена в Ubuntu на VMware. Использовал k3d из семинара 5: он запускает k3s в Docker и уже содержит Traefik. Основная нода — control-plane; вторую добавлял для проверки DaemonSet, затем удалил для экономии ресурсов.

Исходники `counter-backend` и `counter-frontend` взяты из `stands/Lecture4/repos` репозитория курса, коммит `8d0e7a960cbe2bf997e196205949aad054ada02b`. Образы собраны на ВМ и загружены напрямую в containerd; в реестр не отправлялись.

Файлы: [чарт](chart/), [манифесты](manifests/), [скрипты](scripts/), [полные логи](logs/). Все Bash-команды ниже выполнялись из `/home/devops/DevOps-2/HW4`, если в команде не указан другой каталог.

Порт 443 ВМ занят nginx из HW1, поэтому HTTPS кластера опубликован на `127.0.0.1:8443`. В curl используется `--connect-to`; имя сертификата и HTTP Host остаются `counter.localtest.me`. Для браузера открыт SSH-туннель с порта 443 Windows на порт 8443 ВМ. `localtest.me` разрешается в loopback.

## Подготовка

Мониторинг HW3 временно остановил, после проверок запустил обратно. Команды и полный вывод сборок: [frontend](logs/build-frontend.md), [backend](logs/build-backend.md).

Команда (Bash):
```
k3d version; kubectl version --client; helm version --short; uname -sr
```
Вывод (text):
```
k3d version v5.9.0
k3s version v1.35.5-k3s1 (default)
Client Version: v1.35.5
Kustomize Version: v5.7.1
v3.19.0+g3d8990f
Linux 7.0.0-38-generic
```

Команда (Bash):
```
docker stop hw3-monitoring-grafana-1 hw3-monitoring-prometheus-1 hw3-monitoring-node-exporter-1
```
Вывод (text):
```
hw3-monitoring-grafana-1
hw3-monitoring-prometheus-1
hw3-monitoring-node-exporter-1
```

Команда (Bash):
```
k3d cluster create hw4 --servers 1 --agents 0 --image rancher/k3s:v1.35.5-k3s1 --port 127.0.0.1:8443:443@loadbalancer --port 127.0.0.1:8080:80@loadbalancer --k3s-arg "--disable=metrics-server@server:0" --wait --timeout 180s
```
Вывод (text):
```
INFO[0000] portmapping '127.0.0.1:8080:80' targets the loadbalancer: defaulting to [servers:*:proxy agents:*:proxy] 
INFO[0000] portmapping '127.0.0.1:8443:443' targets the loadbalancer: defaulting to [servers:*:proxy agents:*:proxy] 
INFO[0000] Prep: Network                                
INFO[0000] Created network 'k3d-hw4'                    
INFO[0000] Created image volume k3d-hw4-images          
INFO[0000] Starting new tools node...                   
INFO[0001] Creating node 'k3d-hw4-server-0'             
INFO[0002] Pulling image 'ghcr.io/k3d-io/k3d-tools:5.9.0' 
INFO[0003] Pulling image 'rancher/k3s:v1.35.5-k3s1'     
INFO[0006] Starting node 'k3d-hw4-tools'                
INFO[0012] Creating LoadBalancer 'k3d-hw4-serverlb'     
INFO[0014] Pulling image 'ghcr.io/k3d-io/k3d-proxy:5.9.0' 
INFO[0020] Using the k3d-tools node to gather environment information 
INFO[0020] HostIP: using network gateway 172.19.0.1 address 
INFO[0020] Starting cluster 'hw4'                       
INFO[0020] Starting servers...                          
INFO[0020] Starting node 'k3d-hw4-server-0'             
INFO[0025] All agents already running.                  
INFO[0025] Starting helpers...                          
INFO[0025] Starting node 'k3d-hw4-serverlb'             
INFO[0032] Injecting records for hostAliases (incl. host.k3d.internal) and for 2 network members into CoreDNS configmap... 
INFO[0034] Cluster 'hw4' created successfully!          
INFO[0034] You can now use it like this:                
kubectl cluster-info
```

Команда (Bash):
```
docker image ls --filter 'reference=counter-*'; tail -n 8 logs/build-frontend.txt; tail -n 8 logs/build-backend.txt
```
Вывод (text):
```
WARNING: This output is designed for human readability. For machine-readable output, please use --format.
IMAGE                        ID             DISK USAGE   CONTENT SIZE   EXTRA
counter-backend:hw4-v1       488ddeb7eafd        234MB         57.8MB        
counter-backend:hw4-v2       353518c9f440        234MB         57.8MB        
counter-backend:multistage   a775736e7351        234MB         58.8MB   U    
counter-backend:nonroot      84d3d282d252        234MB         58.8MB   U    
counter-backend:single       f89308c3744b        373MB         93.7MB   U    
counter-frontend:hw4-v1      e84ae47150f2        420MB          104MB        
#15 exporting manifest sha256:5fbebc8051d46eb5cb99f1fc2167d718d63e0bc9535f88c0fdbed2cd4b80a532 done
#15 exporting config sha256:0c2bc2b7df1a658526398407dbd861a525f4b77da39b936f1046f168bc0de8cd done
#15 exporting attestation manifest sha256:07b2c5046c2759bb14a19f4690c64d8841b175045c78406a5d48ffcde4787f8b done
#15 exporting manifest list sha256:e84ae47150f2b604cfe6b02a15c0621ecc2e9026fd7bd52415869d9366ffb95a done
#15 naming to docker.io/library/counter-frontend:hw4-v1 done
#15 unpacking to docker.io/library/counter-frontend:hw4-v1
#15 unpacking to docker.io/library/counter-frontend:hw4-v1 0.4s done
#15 DONE 2.3s
#13 exporting manifest sha256:e10565ed4ef6785a02f29fc925de2983261fb22ae309f9b08b5f61dc201639f9 done
#13 exporting config sha256:6a28635c63a3e0a838b1862830d18168df4fc83387b37c8d382ce2e4c420fda5 done
#13 exporting attestation manifest sha256:37766f5ebf80a5fecb4128f7b85356a404ac0f3f57c12aa316e1a3ed7cf25559 done
#13 exporting manifest list sha256:488ddeb7eafdab0247f7defe21f3290ff007a071f949fce440a7c525d552dea1 done
#13 naming to docker.io/library/counter-backend:hw4-v1 done
#13 unpacking to docker.io/library/counter-backend:hw4-v1
#13 unpacking to docker.io/library/counter-backend:hw4-v1 0.2s done
#13 DONE 1.0s
```

Команда (Bash):
```
docker save counter-backend:hw4-v1 counter-frontend:hw4-v1 | docker exec -i k3d-hw4-server-0 ctr -n k8s.io images import --local --all-platforms -
```
Вывод (text):
```
unpacking docker.io/library/counter-backend:hw4-v1 (sha256:488ddeb7eafdab0247f7defe21f3290ff007a071f949fce440a7c525d552dea1)...done
unpacking docker.io/library/counter-frontend:hw4-v1 (sha256:e84ae47150f2b604cfe6b02a15c0621ecc2e9026fd7bd52415869d9366ffb95a)...done
```

Команда (Bash):
```
bash scripts/secrets.sh
```
Вывод (text):
```
......+..+...............+++++++++++++++++++++++++++++++++++++++*.....+++++++++++++++++++++++++++++++++++++++*.........+.......+......+.....+....+...+.....+......+.......+........+.......+..+..........+...........+....+..+....+...........+....+..+............++++++
.+......+..+.+..+++++++++++++++++++++++++++++++++++++++*...+......+..+...+.+.....................+...+.................+++++++++++++++++++++++++++++++++++++++*.+............+...+.+..+...+...............+.+...+...+..+......+.......+..+...+....+...+...+.....++++++
-----
namespace/hw4 created
secret/postgres-auth created
```

Команда (Bash):
```
helm lint ./chart
```
Вывод (text):
```
==> Linting ./chart
[INFO] Chart.yaml: icon is recommended

1 chart(s) linted, 0 chart(s) failed
```

Команда (Bash):
```
helm upgrade --install counter ./chart -n hw4 --set database.enabled=true --set tls.create=true --set-file tls.crt=.secrets/server.crt --set-file tls.key=.secrets/server.key --wait --timeout 300s
```
Вывод (text):
```
Release "counter" does not exist. Installing it now.
NAME: counter
LAST DEPLOYED: Fri Oct 23 18:54:27 2026
NAMESPACE: hw4
STATUS: deployed
REVISION: 1
TEST SUITE: None
```

## 1.1. HTTPS и счётчик

Сертификат выпущен через OpenSSL с SAN для двух адресов. `--cacert` задаёт доверенный сертификат, проверка TLS включена.

Команда (Bash):
```
curl --fail --silent --show-error --cacert .secrets/server.crt --connect-to counter.localtest.me:443:127.0.0.1:8443 -v https://counter.localtest.me/api/counter; printf "\n"; curl --fail --silent --show-error --cacert .secrets/server.crt --connect-to counter.localtest.me:443:127.0.0.1:8443 -I https://counter.localtest.me/
```
Вывод (text):
```
* Connecting to hostname: 127.0.0.1
* Connecting to port: 8443
*   Trying 127.0.0.1:8443...
* ALPN: curl offers h2,http/1.1
} [5 bytes data]
* TLSv1.3 (OUT), TLS handshake, Client hello (1):
} [1575 bytes data]
* SSL Trust Anchors:
*   CAfile: .secrets/server.crt
*   CApath: /etc/ssl/certs
{ [5 bytes data]
* TLSv1.3 (IN), TLS handshake, Server hello (2):
{ [1210 bytes data]
* TLSv1.3 (IN), TLS change cipher, Change cipher spec (1):
{ [1 bytes data]
* TLSv1.3 (IN), TLS handshake, Encrypted Extensions (8):
{ [19 bytes data]
* TLSv1.3 (IN), TLS handshake, Certificate (11):
{ [901 bytes data]
* TLSv1.3 (IN), TLS handshake, CERT verify (15):
{ [264 bytes data]
* TLSv1.3 (IN), TLS handshake, Finished (20):
{ [36 bytes data]
* TLSv1.3 (OUT), TLS change cipher, Change cipher spec (1):
} [1 bytes data]
* TLSv1.3 (OUT), TLS handshake, Finished (20):
} [36 bytes data]
* SSL connection using TLSv1.3 / TLS_AES_128_GCM_SHA256 / X25519MLKEM768 / RSASSA-PSS
* ALPN: server accepted h2
* Server certificate:
*   subject: CN=counter.localtest.me
*   start date: Oct 23 15:54:27 2026 GMT
*   expire date: Jan 21 15:54:27 2027 GMT
*   issuer: CN=counter.localtest.me
*   Certificate level 0: Public key type RSA (2048/112 Bits/secBits), signed using sha256WithRSAEncryption
*   subjectAltName: "counter.localtest.me" matches cert's "counter.localtest.me"
* SSL certificate verified via OpenSSL.
* Established connection to 127.0.0.1 (127.0.0.1 port 8443) from 127.0.0.1 port 41630 
* using HTTP/2
* [HTTP/2] [1] OPENED stream for https://counter.localtest.me/api/counter
* [HTTP/2] [1] [:method: GET]
* [HTTP/2] [1] [:scheme: https]
* [HTTP/2] [1] [:authority: counter.localtest.me]
* [HTTP/2] [1] [:path: /api/counter]
* [HTTP/2] [1] [user-agent: curl/8.18.0]
* [HTTP/2] [1] [accept: */*]
} [5 bytes data]
> GET /api/counter HTTP/2
> Host: counter.localtest.me
> User-Agent: curl/8.18.0
> Accept: */*
> 
* Request completely sent off
{ [5 bytes data]
* TLSv1.3 (IN), TLS handshake, Newsession Ticket (4):
{ [122 bytes data]
< HTTP/2 200 
< content-type: application/json; charset=utf-8
< date: Fri, 23 Oct 2026 15:57:40 GMT
< server: Python/3.11 aiohttp/3.8.5
< content-length: 12
< 
{ [5 bytes data]
* Connection #0 to host 127.0.0.1:8443 left intact
{"count": 0}
HTTP/2 200 
cache-control: s-maxage=31536000
content-type: text/html; charset=utf-8
date: Fri, 23 Oct 2026 15:57:40 GMT
etag: "12a3sshzhi63rr"
vary: rsc, next-router-state-tree, next-router-prefetch, next-router-segment-prefetch, Accept-Encoding
x-nextjs-cache: HIT
x-nextjs-prerender: 1
x-nextjs-prerender: 1
x-nextjs-stale-time: 300
x-powered-by: Next.js
content-length: 4887
```

Команда (Bash):
```
for i in 1 2 3; do curl --fail --silent --show-error --cacert .secrets/server.crt --connect-to counter.localtest.me:443:127.0.0.1:8443 -X POST https://counter.localtest.me/api/counter; printf "\n"; done
```
Вывод (text):
```
{"count": 1}
{"count": 2}
{"count": 3}
```

В браузере открыт `https://counter.localtest.me/`. После нажатия **Increment** значение изменилось с `0` на `1`. Для самоподписанного сертификата переход через предупреждение браузера подтверждён вручную.

![Counter по HTTPS после Increment](screenshots/counter-https.png)

## 1.2. Доступ к backend

Оба Service имеют тип ClusterIP. Ingress отправляет `/api` в backend, остальные пути — во frontend; NodePort и отдельного внешнего адреса у backend нет.

Команда (Bash):
```
kubectl -n hw4 get svc,ingress -o wide; kubectl -n hw4 get ingress counter -o yaml
```
Вывод (text):
```
NAME                       TYPE        CLUSTER-IP     EXTERNAL-IP   PORT(S)    AGE     SELECTOR
service/counter-backend    ClusterIP   10.43.149.38   <none>        9000/TCP   3m12s   app=counter-backend
service/counter-frontend   ClusterIP   10.43.38.132   <none>        8080/TCP   3m12s   app=counter-frontend
service/counter-postgres   ClusterIP   None           <none>        5432/TCP   3m12s   app=counter-postgres

NAME                                CLASS     HOSTS                  ADDRESS      PORTS     AGE
ingress.networking.k8s.io/counter   traefik   counter.localtest.me   172.19.0.2   80, 443   3m12s
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  annotations:
    meta.helm.sh/release-name: counter
    meta.helm.sh/release-namespace: hw4
  creationTimestamp: "2026-10-23T15:54:28Z"
  generation: 1
  labels:
    app.kubernetes.io/managed-by: Helm
  name: counter
  namespace: hw4
  resourceVersion: "737"
  uid: a25388e0-f8a0-49fc-824d-f4f7b3eb55d6
spec:
  ingressClassName: traefik
  rules:
  - host: counter.localtest.me
    http:
      paths:
      - backend:
          service:
            name: counter-backend
            port:
              name: http
        path: /api
        pathType: Prefix
      - backend:
          service:
            name: counter-frontend
            port:
              name: http
        path: /
        pathType: Prefix
  tls:
  - hosts:
    - counter.localtest.me
    secretName: counter-tls
status:
  loadBalancer:
    ingress:
    - ip: 172.19.0.2
```

## 1.3–1.5. Порт, пробы и ресурсы

Порт backend задаётся через ConfigMap и переменную `PORT`; вместо стандартного 8080 используется 9000. Смена на 9001 с тем же образом показана в разделе 4.2. У контейнеров заданы requests и limits, у приложения — startup, readiness и liveness probes.

Команда (Bash):
```
kubectl -n hw4 exec deploy/counter-backend -- printenv PORT
kubectl -n hw4 get deploy counter-backend -o jsonpath='{.spec.template.spec.containers[0]}'
printf '
'
kubectl -n hw4 get pods -o custom-columns=NAME:.metadata.name,QOS:.status.qosClass,REQUESTS:.spec.containers[*].resources.requests,LIMITS:.spec.containers[*].resources.limits
```
Вывод (text):
```
9000
{"env":[{"name":"PORT","valueFrom":{"configMapKeyRef":{"key":"BACKEND_PORT","name":"counter-config"}}}],"image":"counter-backend:hw4-v1","imagePullPolicy":"Never","livenessProbe":{"failureThreshold":6,"httpGet":{"path":"/api/counter","port":"http","scheme":"HTTP"},"periodSeconds":10,"successThreshold":1,"timeoutSeconds":1},"name":"backend","ports":[{"containerPort":9000,"name":"http","protocol":"TCP"}],"readinessProbe":{"failureThreshold":1,"httpGet":{"path":"/api/counter","port":"http","scheme":"HTTP"},"periodSeconds":3,"successThreshold":1,"timeoutSeconds":1},"resources":{"limits":{"cpu":"300m","memory":"96Mi"},"requests":{"cpu":"25m","memory":"32Mi"}},"startupProbe":{"failureThreshold":60,"httpGet":{"path":"/api/counter","port":"http","scheme":"HTTP"},"periodSeconds":2,"successThreshold":1,"timeoutSeconds":1},"terminationMessagePath":"/dev/termination-log","terminationMessagePolicy":"File"}
NAME                                QOS         REQUESTS                   LIMITS
counter-backend-546d98d9dc-2qc9r    Burstable   map[cpu:25m memory:32Mi]   map[cpu:300m memory:96Mi]
counter-check-hzfpd                 Burstable   map[cpu:10m memory:16Mi]   map[cpu:100m memory:64Mi]
counter-frontend-576cd7c5f6-5xbrb   Burstable   map[cpu:25m memory:64Mi]   map[cpu:400m memory:256Mi]
counter-postgres-0                  Burstable   map[cpu:25m memory:64Mi]   map[cpu:300m memory:192Mi]
```

## 1.4. Зависший экземпляр

Для проверки остановил процесс backend сигналом STOP из пространства имён ноды. Readiness исключила Pod из EndpointSlice, запросы продолжили обслуживать две другие реплики; затем liveness перезапустила зависший контейнер.

Команда (Bash):
```
kubectl -n hw4 scale deployment/counter-backend --replicas=3 && kubectl -n hw4 rollout status deployment/counter-backend --timeout=120s
```
Вывод (text):
```
deployment.apps/counter-backend scaled
Waiting for deployment "counter-backend" rollout to finish: 1 out of 3 new replicas have been updated...
Waiting for deployment "counter-backend" rollout to finish: 1 of 3 updated replicas are available...
Waiting for deployment "counter-backend" rollout to finish: 2 of 3 updated replicas are available...
deployment "counter-backend" successfully rolled out
```

Команда (Bash):
```
set -euo pipefail
POD=$(kubectl -n hw4 get pod -l app=counter-backend -o jsonpath='{.items[0].metadata.name}')
CID=$(kubectl -n hw4 get pod "$POD" -o jsonpath='{.status.containerStatuses[0].containerID}')
PID=$(docker exec k3d-hw4-server-0 crictl inspect "${CID#containerd://}" | python3 -c 'import sys,json; print(json.load(sys.stdin)["info"]["pid"])')
docker exec k3d-hw4-server-0 kill -STOP "$PID"
kubectl -n hw4 wait --for=condition=Ready=false pod/"$POD" --timeout=25s
kubectl -n hw4 get pods -l app=counter-backend -o wide
kubectl -n hw4 get endpointslice -l kubernetes.io/service-name=counter-backend -o jsonpath='{range .items[*].endpoints[*]}{.targetRef.name}{" ready="}{.conditions.ready}{"\n"}{end}'
python3 scripts/traffic.py 10
kubectl -n hw4 wait --for=condition=Ready pod/"$POD" --timeout=150s
kubectl -n hw4 get pods -l app=counter-backend
kubectl -n hw4 describe pod "$POD" | tail -15
```
Вывод (text):
```
pod/counter-backend-546d98d9dc-2qc9r condition met
NAME                               READY   STATUS    RESTARTS   AGE     IP           NODE               NOMINATED NODE   READINESS GATES
counter-backend-546d98d9dc-2qc9r   0/1     Running   0          4m57s   10.42.0.7    k3d-hw4-server-0   <none>           <none>
counter-backend-546d98d9dc-6whf4   1/1     Running   0          7s      10.42.0.18   k3d-hw4-server-0   <none>           <none>
counter-backend-546d98d9dc-rw9cq   1/1     Running   0          7s      10.42.0.17   k3d-hw4-server-0   <none>           <none>
counter-backend-546d98d9dc-2qc9r ready=false
counter-backend-546d98d9dc-6whf4 ready=true
counter-backend-546d98d9dc-rw9cq ready=true
HTTP responses: {'200': 48}
pod/counter-backend-546d98d9dc-2qc9r condition met
NAME                               READY   STATUS    RESTARTS     AGE
counter-backend-546d98d9dc-2qc9r   1/1     Running   1 (4s ago)   6m25s
counter-backend-546d98d9dc-6whf4   1/1     Running   0            95s
counter-backend-546d98d9dc-rw9cq   1/1     Running   0            95s
Node-Selectors:               <none>
Tolerations:                  node.kubernetes.io/not-ready:NoExecute op=Exists for 300s
                              node.kubernetes.io/unreachable:NoExecute op=Exists for 300s
Events:
  Type     Reason             Age                     From               Message
  ----     ------             ----                    ----               -------
  Normal   Scheduled          6m24s                   default-scheduler  Successfully assigned hw4/counter-backend-546d98d9dc-2qc9r to k3d-hw4-server-0
  Warning  ErrImageNeverPull  4m22s (x11 over 6m25s)  kubelet            spec.containers{backend}: Container image "counter-backend:hw4-v1" is not present with pull policy of Never
  Warning  Failed             4m22s (x11 over 6m25s)  kubelet            spec.containers{backend}: Error: ErrImageNeverPull
  Warning  Unhealthy          84s (x3 over 88s)       kubelet            spec.containers{backend}: Readiness probe failed: Get "http://10.42.0.7:9000/api/counter": context deadline exceeded (Client.Timeout exceeded while awaiting headers)
  Warning  Unhealthy          84s                     kubelet            spec.containers{backend}: Liveness probe failed: Get "http://10.42.0.7:9000/api/counter": context deadline exceeded (Client.Timeout exceeded while awaiting headers)
  Normal   Killing            34s                     kubelet            spec.containers{backend}: Container backend failed liveness probe, will be restarted
  Normal   Pulled             4s (x2 over 4m10s)      kubelet            spec.containers{backend}: Container image "counter-backend:hw4-v1" already present on machine and can be accessed by the pod
  Normal   Created            4s (x2 over 4m10s)      kubelet            spec.containers{backend}: Container created
  Normal   Started            4s (x2 over 4m10s)      kubelet            spec.containers{backend}: Container started
```

Команда (Bash):
```
kubectl -n hw4 scale deploy counter-backend --replicas=1 && kubectl -n hw4 rollout status deploy/counter-backend --timeout=120s
```
Вывод (text):
```
deployment.apps/counter-backend scaled
deployment "counter-backend" successfully rolled out
```

## 1.6. Обновление и откат

Использовал RollingUpdate с `maxUnavailable: 0` и `maxSurge: 1`. При первой проверке появились ошибки на остановке старого Pod; добавил `preStop: sleep 10` и `minReadySeconds: 5`, затем повторил проверку. Образ v2 отличается меткой сборки, код приложения тот же.

Команда (Bash):
```
cat logs/rolling-traffic.txt
```
Вывод (text):
```
HTTP responses: {'200': 149, '502': 1, '000': 1}
```

Команда (Bash):
```
helm upgrade counter ./chart -n hw4 --reuse-values --set backend.image=counter-backend:hw4-v1 --set-string changeCause='Graceful shutdown: preStop 10 seconds' --wait --timeout 180s
```
Вывод (text):
```
Release "counter" has been upgraded. Happy Helming!
NAME: counter
LAST DEPLOYED: Fri Oct 23 19:03:40 2026
NAMESPACE: hw4
STATUS: deployed
REVISION: 3
TEST SUITE: None
```

Команда (Bash):
```
printf 'FROM counter-backend:hw4-v1\nLABEL hw4.release=v2\n' | docker build -t counter-backend:hw4-v2 - && docker save counter-backend:hw4-v2 | docker exec -i k3d-hw4-server-0 ctr -n k8s.io images import --local --all-platforms -
```
Вывод (text):
```
#0 building with "default" instance using docker driver

#1 [internal] load build definition from Dockerfile
#1 transferring dockerfile: 86B done
#1 DONE 0.0s

#2 [internal] load metadata for docker.io/library/counter-backend:hw4-v1
#2 DONE 0.0s

#3 [internal] load .dockerignore
#3 transferring context: 2B done
#3 DONE 0.0s

#4 [1/1] FROM docker.io/library/counter-backend:hw4-v1@sha256:488ddeb7eafdab0247f7defe21f3290ff007a071f949fce440a7c525d552dea1
#4 resolve docker.io/library/counter-backend:hw4-v1@sha256:488ddeb7eafdab0247f7defe21f3290ff007a071f949fce440a7c525d552dea1 done
#4 DONE 0.0s

#5 exporting to image
#5 exporting layers done
#5 exporting manifest sha256:0645cfb1074fd67ec8c7b176deb703a4f828aab7cb5296f0d23d421418946977 done
#5 exporting config sha256:0811d265dccdf35af87a9fdae7c9042b309bc2a9ee2a7f7202c8879a0d33c843 done
#5 exporting attestation manifest sha256:df19b8c3abd40ce5ea1a8393e5cf9d05d31eea26e7710142722ebc31a4b8902e done
#5 exporting manifest list sha256:353518c9f44024c783cb03ff5093423f390510bd3b3748ac0579d0b940945feb
#5 exporting manifest list sha256:353518c9f44024c783cb03ff5093423f390510bd3b3748ac0579d0b940945feb done
#5 naming to docker.io/library/counter-backend:hw4-v2 done
#5 unpacking to docker.io/library/counter-backend:hw4-v2 done
#5 DONE 0.0s
unpacking docker.io/library/counter-backend:hw4-v2 (sha256:353518c9f44024c783cb03ff5093423f390510bd3b3748ac0579d0b940945feb)...done
```

Команда (Bash):
```
python3 scripts/traffic.py 35 > logs/rolling-traffic.txt &
traffic_pid=$!
helm upgrade counter ./chart -n hw4 --reuse-values --set backend.image=counter-backend:hw4-v2 --set-string changeCause='Backend image hw4-v2' --wait --timeout 180s
wait "$traffic_pid"
cat logs/rolling-traffic.txt
kubectl -n hw4 logs job/counter-check
kubectl -n hw4 rollout history deploy/counter-backend
```
Вывод (text):
```
Release "counter" has been upgraded. Happy Helming!
NAME: counter
LAST DEPLOYED: Fri Oct 23 19:03:48 2026
NAMESPACE: hw4
STATUS: deployed
REVISION: 4
TEST SUITE: None
HTTP responses: {'200': 165}
http://counter-frontend:8080/ 200
http://counter-backend:9000/api/counter 200
deployment.apps/counter-backend 
REVISION  CHANGE-CAUSE
1         Initial installation
2         Backend image hw4-v2
3         Graceful shutdown: preStop 10 seconds
4         Backend image hw4-v2
```

Команда (Bash):
```
kubectl -n hw4 patch deploy counter-backend --type=merge -p '{"metadata":{"annotations":{"kubernetes.io/change-cause":"Check missing image"}},"spec":{"template":{"spec":{"containers":[{"name":"backend","image":"counter-backend:missing","imagePullPolicy":"Never","ports":[{"name":"http","containerPort":9000}],"env":[{"name":"PORT","value":"9000"}],"resources":{"requests":{"cpu":"25m","memory":"32Mi"},"limits":{"cpu":"300m","memory":"96Mi"}},"readinessProbe":{"httpGet":{"path":"/api/counter","port":"http"}}}]}}}}'
kubectl -n hw4 rollout status deploy/counter-backend --timeout=30s
```
Вывод (text):
```
deployment.apps/counter-backend patched
Waiting for deployment "counter-backend" rollout to finish: 0 out of 1 new replicas have been updated...
Waiting for deployment "counter-backend" rollout to finish: 1 old replicas are pending termination...
error: timed out waiting for the condition
```

Команда (Bash):
```
kubectl -n hw4 get pods -l app=counter-backend; python3 scripts/traffic.py 10; kubectl -n hw4 rollout history deploy/counter-backend
```
Вывод (text):
```
NAME                               READY   STATUS              RESTARTS   AGE
counter-backend-5645b676c5-dq6zx   0/1     ErrImageNeverPull   0          29s
counter-backend-6d647ddc8f-sxxpg   1/1     Running             0          65s
HTTP responses: {'200': 48}
deployment.apps/counter-backend 
REVISION  CHANGE-CAUSE
1         Initial installation
2         Backend image hw4-v2
3         Graceful shutdown: preStop 10 seconds
4         Backend image hw4-v2
5         Check missing image
```

Команда (Bash):
```
kubectl -n hw4 rollout undo deploy/counter-backend && kubectl -n hw4 rollout status deploy/counter-backend --timeout=120s && kubectl -n hw4 rollout history deploy/counter-backend
```
Вывод (text):
```
deployment.apps/counter-backend rolled back
deployment "counter-backend" successfully rolled out
deployment.apps/counter-backend 
REVISION  CHANGE-CAUSE
1         Initial installation
2         Backend image hw4-v2
3         Graceful shutdown: preStop 10 seconds
5         Check missing image
6         Backend image hw4-v2
```

## Ответы по приложению

1. При трёх backend значения расходятся: счётчик находится в памяти каждого процесса. Для масштабирования нужен общий источник данных, например PostgreSQL с атомарным увеличением значения.
2. Переменные окружения из ConfigMap обновляются только при создании контейнера. Смонтированные файлы обновляются с задержкой, кроме `subPath`; приложению ещё нужно перечитать их. В чарте checksum ConfigMap меняет шаблон Pod и запускает обновление.
3. Класс QoS — Burstable: requests меньше limits. Небольшие requests подходят для учебной нагрузки, limits ограничивают потребление памяти и CPU.

Команда (Bash):
```
kubectl -n hw4 scale deploy counter-backend --replicas=3 && kubectl -n hw4 rollout status deploy/counter-backend --timeout=120s
```
Вывод (text):
```
deployment.apps/counter-backend scaled
Waiting for deployment "counter-backend" rollout to finish: 1 out of 3 new replicas have been updated...
Waiting for deployment "counter-backend" rollout to finish: 1 of 3 updated replicas are available...
Waiting for deployment "counter-backend" rollout to finish: 2 of 3 updated replicas are available...
deployment "counter-backend" successfully rolled out
```

Команда (Bash):
```
for i in $(seq 1 9); do curl --fail --silent --show-error --cacert .secrets/server.crt --connect-to counter.localtest.me:443:127.0.0.1:8443 -X POST https://counter.localtest.me/api/counter; printf "\n"; done
for pod in $(kubectl -n hw4 get pod -l app=counter-backend -o name); do
  echo "$pod"
  kubectl -n hw4 exec "$pod" -- python -c 'import urllib.request; print(urllib.request.urlopen("http://127.0.0.1:9000/api/counter").read().decode())'
done
```
Вывод (text):
```
{"count": 4}
{"count": 1}
{"count": 5}
{"count": 2}
{"count": 6}
{"count": 3}
{"count": 7}
{"count": 4}
{"count": 8}
pod/counter-backend-546d98d9dc-2qc9r
{"count": 8}
pod/counter-backend-546d98d9dc-6ztl8
{"count": 4}
pod/counter-backend-546d98d9dc-dcvpp
{"count": 0}
```

Команда (Bash):
```
kubectl -n hw4 scale deploy counter-backend --replicas=1 && kubectl -n hw4 rollout status deploy/counter-backend --timeout=120s
```
Вывод (text):
```
deployment.apps/counter-backend scaled
deployment "counter-backend" successfully rolled out
```

## 2.1. Сохранение PostgreSQL

БД запущена через StatefulSet с отдельным PVC. Удаление Pod или StatefulSet не удаляет этот PVC.

Команда (Bash):
```
kubectl -n hw4 logs counter-postgres-0 | tail -25
kubectl -n hw4 exec counter-postgres-0 -- psql -U counter -d counter -c 'TABLE visits;'
kubectl -n hw4 exec counter-postgres-0 -- psql -U counter -d counter -c "INSERT INTO visits VALUES (2, 'saved before pod deletion');"
```
Вывод (text):
```
/usr/local/bin/docker-entrypoint.sh: running /docker-entrypoint-initdb.d/init.sql
CREATE TABLE
INSERT 0 1


2026-10-23 15:55:05.841 UTC [47] LOG:  received fast shutdown request
waiting for server to shut down....2026-10-23 15:55:05.842 UTC [47] LOG:  aborting any active transactions
2026-10-23 15:55:05.846 UTC [47] LOG:  background worker "logical replication launcher" (PID 53) exited with exit code 1
2026-10-23 15:55:05.847 UTC [48] LOG:  shutting down
2026-10-23 15:55:05.853 UTC [48] LOG:  checkpoint starting: shutdown immediate
2026-10-23 15:55:05.950 UTC [48] LOG:  checkpoint complete: wrote 929 buffers (5.7%); 0 WAL file(s) added, 0 removed, 0 recycled; write=0.094 s, sync=0.002 s, total=0.103 s; sync files=305, longest=0.001 s, average=0.001 s; distance=4296 kB, estimate=4296 kB; lsn=0/1929490, redo lsn=0/1929490
2026-10-23 15:55:05.954 UTC [47] LOG:  database system is shut down
 done
server stopped

PostgreSQL init process complete; ready for start up.

2026-10-23 15:55:06.057 UTC [1] LOG:  starting PostgreSQL 16.15 on x86_64-pc-linux-musl, compiled by gcc (Alpine 15.2.0) 15.2.0, 64-bit
2026-10-23 15:55:06.057 UTC [1] LOG:  listening on IPv4 address "0.0.0.0", port 5432
2026-10-23 15:55:06.057 UTC [1] LOG:  listening on IPv6 address "::", port 5432
2026-10-23 15:55:06.058 UTC [1] LOG:  listening on Unix socket "/var/run/postgresql/.s.PGSQL.5432"
2026-10-23 15:55:06.061 UTC [65] LOG:  database system was shut down at 2026-10-23 15:55:05 UTC
2026-10-23 15:55:06.064 UTC [1] LOG:  database system is ready to accept connections
 id |        note         
----+---------------------
  1 | created by init.sql
(1 row)

INSERT 0 1
```

Команда (Bash):
```
kubectl -n hw4 delete pod counter-postgres-0
kubectl -n hw4 rollout status statefulset/counter-postgres --timeout=150s
kubectl -n hw4 exec counter-postgres-0 -- psql -U counter -d counter -c 'TABLE visits;'
```
Вывод (text):
```
pod "counter-postgres-0" deleted from hw4 namespace
Waiting for 1 pods to be ready...
Waiting for 1 pods to be ready...
Waiting for 1 pods to be ready...
partitioned roll out complete: 1 new pods have been updated...
 id |           note            
----+---------------------------
  1 | created by init.sql
  2 | saved before pod deletion
(2 rows)
```

Команда (Bash):
```
kubectl -n hw4 delete statefulset counter-postgres
kubectl -n hw4 wait --for=delete pod/counter-postgres-0 --timeout=90s
kubectl -n hw4 get pvc
kubectl -n hw4 apply -f manifests/postgres.yaml
kubectl -n hw4 rollout status statefulset/counter-postgres --timeout=150s
kubectl -n hw4 exec counter-postgres-0 -- psql -U counter -d counter -c 'TABLE visits;'
```
Вывод (text):
```
statefulset.apps "counter-postgres" deleted from hw4 namespace
pod/counter-postgres-0 condition met
NAME                    STATUS   VOLUME                                     CAPACITY   ACCESS MODES   STORAGECLASS   VOLUMEATTRIBUTESCLASS   AGE
counter-postgres-data   Bound    pvc-7ff61715-2ee2-4a2c-8d11-4df4a8b4e3ff   256Mi      RWO            local-path     <unset>                 4m6s
Warning: resource configmaps/counter-postgres-init is missing the kubectl.kubernetes.io/last-applied-configuration annotation which is required by kubectl apply. kubectl apply should only be used on resources created declaratively by either kubectl create --save-config or kubectl apply. The missing annotation will be patched automatically.
configmap/counter-postgres-init configured
Warning: resource persistentvolumeclaims/counter-postgres-data is missing the kubectl.kubernetes.io/last-applied-configuration annotation which is required by kubectl apply. kubectl apply should only be used on resources created declaratively by either kubectl create --save-config or kubectl apply. The missing annotation will be patched automatically.
persistentvolumeclaim/counter-postgres-data configured
Warning: resource services/counter-postgres is missing the kubectl.kubernetes.io/last-applied-configuration annotation which is required by kubectl apply. kubectl apply should only be used on resources created declaratively by either kubectl create --save-config or kubectl apply. The missing annotation will be patched automatically.
service/counter-postgres configured
statefulset.apps/counter-postgres created
Waiting for 1 pods to be ready...
partitioned roll out complete: 1 new pods have been updated...
 id |           note            
----+---------------------------
  1 | created by init.sql
  2 | saved before pod deletion
(2 rows)
```

## 2.2–2.3. DNS, начальная таблица и пароль

Headless Service даёт постоянное имя `counter-postgres-0.counter-postgres.hw4.svc.cluster.local`. `init.sql` хранится в ConfigMap и выполняется при первом запуске на пустом томе; случайный пароль создан локально и передан через Secret. В манифестах указана только ссылка на Secret.

Команда (Bash):
```
kubectl apply -f manifests/db-client.yaml && kubectl -n hw4 wait --for=condition=complete job/db-client --timeout=90s && kubectl -n hw4 logs job/db-client
```
Вывод (text):
```
job.batch/db-client created
job.batch/db-client condition met
 inet_server_addr 
------------------
 10.42.0.16
(1 row)

 id |           note            
----+---------------------------
  1 | created by init.sql
  2 | saved before pod deletion
(2 rows)
```

Команда (Bash):
```
kubectl -n hw4 get pod counter-postgres-0 -o wide
kubectl -n hw4 get svc counter-postgres
kubectl get pv -o custom-columns=NAME:.metadata.name,RECLAIM:.spec.persistentVolumeReclaimPolicy,PATH:.spec.hostPath.path
kubectl -n hw4 get secret postgres-auth
kubectl -n hw4 get statefulset counter-postgres -o jsonpath='{.spec.template.spec.containers[0].env}'
printf '
'
```
Вывод (text):
```
NAME                 READY   STATUS    RESTARTS   AGE   IP           NODE               NOMINATED NODE   READINESS GATES
counter-postgres-0   1/1     Running   0          4s    10.42.0.16   k3d-hw4-server-0   <none>           <none>
NAME               TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)    AGE
counter-postgres   ClusterIP   None         <none>        5432/TCP   4m10s
NAME                                       RECLAIM   PATH
pvc-7ff61715-2ee2-4a2c-8d11-4df4a8b4e3ff   Delete    <none>
NAME            TYPE     DATA   AGE
postgres-auth   Opaque   1      4m12s
[{"name":"POSTGRES_USER","value":"counter"},{"name":"POSTGRES_DB","value":"counter"},{"name":"POSTGRES_PASSWORD","valueFrom":{"secretKeyRef":{"key":"password","name":"postgres-auth"}}},{"name":"PGDATA","value":"/var/lib/postgresql/data/pgdata"}]
```

Команда (Bash):
```
kubectl get pv -o custom-columns=NAME:.metadata.name,RECLAIM:.spec.persistentVolumeReclaimPolicy,LOCAL:.spec.local.path,HOSTPATH:.spec.hostPath.path; docker inspect k3d-hw4-server-0 --format "{{json .Mounts}}"
```
Вывод (text):
```
NAME                                       RECLAIM   LOCAL                                                                                             HOSTPATH
pvc-7ff61715-2ee2-4a2c-8d11-4df4a8b4e3ff   Delete    /var/lib/rancher/k3s/storage/pvc-7ff61715-2ee2-4a2c-8d11-4df4a8b4e3ff_hw4_counter-postgres-data   <none>
[{"Type":"volume","Name":"k3d-hw4-images","Source":"/var/lib/docker/volumes/k3d-hw4-images/_data","Destination":"/k3d/images","Driver":"local","Mode":"z","RW":true,"Propagation":""},{"Type":"volume","Name":"a4a72749588aaed34f2db300a7735888c0f0a8eea0e2752201c3f9c830b015a6","Source":"/var/lib/docker/volumes/a4a72749588aaed34f2db300a7735888c0f0a8eea0e2752201c3f9c830b015a6/_data","Destination":"/var/lib/cni","Driver":"local","Mode":"","RW":true,"Propagation":""},{"Type":"volume","Name":"3c86c39ff394fe9f638e85e1daf0cf22afd4ccc8867fca89254ef284b8af5d08","Source":"/var/lib/docker/volumes/3c86c39ff394fe9f638e85e1daf0cf22afd4ccc8867fca89254ef284b8af5d08/_data","Destination":"/var/lib/kubelet","Driver":"local","Mode":"","RW":true,"Propagation":""},{"Type":"volume","Name":"a87e1a0c19d17989c6337b0af4cb943bcd55315dda4821311b418c5db7c6f319","Source":"/var/lib/docker/volumes/a87e1a0c19d17989c6337b0af4cb943bcd55315dda4821311b418c5db7c6f319/_data","Destination":"/var/lib/rancher/k3s","Driver":"local","Mode":"","RW":true,"Propagation":""},{"Type":"volume","Name":"cee7a7a443ae0d808fe0081e128f512738577970f34235693bbe2614f1c790ab","Source":"/var/lib/docker/volumes/cee7a7a443ae0d808fe0081e128f512738577970f34235693bbe2614f1c790ab/_data","Destination":"/var/log","Driver":"local","Mode":"","RW":true,"Propagation":""}]
```

### Ответы по БД

1. StatefulSet сохраняет имя экземпляра, headless Service даёт его DNS-имя, PVC хранит данные независимо от Pod. Здесь один экземпляр PostgreSQL; это не кластер с репликацией.
2. Данные лежат в `/var/lib/rancher/k3s/storage/pvc-7ff61715-2ee2-4a2c-8d11-4df4a8b4e3ff_hw4_counter-postgres-data` внутри ноды. Каталог `/var/lib/rancher/k3s` подключён из Docker volume на диске ВМ. При удалении namespace удалится PVC, а политика PV `Delete` удалит и данные; аннотация Helm `keep` от удаления namespace не защищает.

## 3.1. Метрики со всех нод

Node-exporter запущен как DaemonSet с tolerations, включая control-plane. На новой ноде Pod появился автоматически. В k3d ноды используют одно ядро и память ВМ, поэтому физический объём памяти в их метриках одинаковый.

Команда (Bash):
```
kubectl apply -f manifests/node-exporter.yaml -f manifests/scaler.yaml -f manifests/scale-morning.yaml -f manifests/scale-evening.yaml && kubectl -n hw4 rollout status daemonset/node-exporter --timeout=150s
```
Вывод (text):
```
daemonset.apps/node-exporter created
serviceaccount/frontend-scaler created
role.rbac.authorization.k8s.io/frontend-scaler created
rolebinding.rbac.authorization.k8s.io/frontend-scaler created
cronjob.batch/frontend-morning created
cronjob.batch/frontend-evening created
Waiting for daemon set spec update to be observed...
Waiting for daemon set "node-exporter" rollout to finish: 0 out of 1 new pods have been updated...
Waiting for daemon set "node-exporter" rollout to finish: 0 of 1 updated pods are available...
daemon set "node-exporter" successfully rolled out
```

Команда (Bash):
```
kubectl get nodes; kubectl -n hw4 get ds; kubectl -n hw4 get pods -l app=node-exporter -o wide
```
Вывод (text):
```
NAME               STATUS   ROLES           AGE   VERSION
k3d-hw4-server-0   Ready    control-plane   12m   v1.35.5+k3s1
NAME            DESIRED   CURRENT   READY   UP-TO-DATE   AVAILABLE   NODE SELECTOR   AGE
node-exporter   1         1         1       1            1           <none>          11s
NAME                  READY   STATUS    RESTARTS   AGE   IP           NODE               NOMINATED NODE   READINESS GATES
node-exporter-rpqxv   1/1     Running   0          10s   172.19.0.2   k3d-hw4-server-0   <none>           <none>
```

Команда (Bash):
```
k3d node create extra --cluster hw4 --role agent --wait --timeout 180s && kubectl cordon k3d-extra-0
```
Вывод (text):
```
INFO[0000] Adding 1 node(s) to the runtime local cluster 'hw4'... 
INFO[0000] Using the k3d-tools node to gather environment information 
INFO[0000] Starting new tools node...                   
INFO[0000] Starting node 'k3d-hw4-tools'                
INFO[0000] HostIP: using network gateway 172.19.0.1 address 
INFO[0000] Starting node 'k3d-extra-0'                  
INFO[0004] Successfully created 1 node(s)!              
node/k3d-extra-0 cordoned
```

Команда (Bash):
```
kubectl wait --for=condition=Ready nodes --all --timeout=120s && kubectl -n hw4 rollout status daemonset/node-exporter --timeout=150s && kubectl get nodes && kubectl -n hw4 get ds && kubectl -n hw4 get pods -l app=node-exporter -o wide
```
Вывод (text):
```
node/k3d-extra-0 condition met
node/k3d-hw4-server-0 condition met
Waiting for daemon set "node-exporter" rollout to finish: 1 of 2 updated pods are available...
daemon set "node-exporter" successfully rolled out
NAME               STATUS                     ROLES           AGE   VERSION
k3d-extra-0        Ready,SchedulingDisabled   <none>          19s   v1.35.5+k3s1
k3d-hw4-server-0   Ready                      control-plane   12m   v1.35.5+k3s1
NAME            DESIRED   CURRENT   READY   UP-TO-DATE   AVAILABLE   NODE SELECTOR   AGE
node-exporter   2         2         2       2            2           <none>          34s
NAME                  READY   STATUS    RESTARTS   AGE   IP           NODE               NOMINATED NODE   READINESS GATES
node-exporter-j25s6   1/1     Running   0          19s   172.19.0.4   k3d-extra-0        <none>           <none>
node-exporter-rpqxv   1/1     Running   0          33s   172.19.0.2   k3d-hw4-server-0   <none>           <none>
```

Команда (Bash):
```
for ip in $(kubectl -n hw4 get pods -l app=node-exporter -o jsonpath='{.items[*].status.podIP}'); do
  kubectl -n hw4 exec deploy/counter-backend -- python -c "import urllib.request; data=urllib.request.urlopen('http://$ip:9100/metrics').read().decode(); print('$ip'); print('\n'.join(x for x in data.splitlines() if x.startswith(('node_uname_info{', 'node_memory_MemTotal_bytes '))))"
done
```
Вывод (text):
```
172.19.0.4
node_memory_MemTotal_bytes 3.51328256e+09
node_uname_info{domainname="(none)",machine="x86_64",nodename="k3d-extra-0",release="7.0.0-38-generic",sysname="Linux",version="#38-Ubuntu SMP PREEMPT_DYNAMIC Fri Sep  4 09:10:14 UTC 2026"} 1
172.19.0.2
node_memory_MemTotal_bytes 3.51328256e+09
node_uname_info{domainname="(none)",machine="x86_64",nodename="k3d-hw4-server-0",release="7.0.0-38-generic",sysname="Linux",version="#38-Ubuntu SMP PREEMPT_DYNAMIC Fri Sep  4 09:10:14 UTC 2026"} 1
```

Команда (Bash):
```
k3d node delete k3d-extra-0 && kubectl delete node k3d-extra-0 && kubectl -n hw4 get daemonset node-exporter
```
Вывод (text):
```
INFO[0000] Successfully deleted 1 node(s)!              
node "k3d-extra-0" deleted
NAME            DESIRED   CURRENT   READY   UP-TO-DATE   AVAILABLE   NODE SELECTOR   AGE
node-exporter   2         2         2       2            2           <none>          35s
```

## 3.2. Масштабирование по расписанию

CronJob используют часовой пояс Europe/Moscow: в 09:00 выставляют 3 реплики, в 18:00 — 1. ServiceAccount разрешён только PATCH подресурса scale у `counter-frontend` в namespace `hw4`; доступ к другим Deployment, Secret и удалению Pod запрещён.

Команда (Bash):
```
kubectl -n hw4 get cronjobs -o custom-columns=NAME:.metadata.name,SCHEDULE:.spec.schedule,TIMEZONE:.spec.timeZone,SERVICEACCOUNT:.spec.jobTemplate.spec.template.spec.serviceAccountName
```
Вывод (text):
```
NAME               SCHEDULE     TIMEZONE        SERVICEACCOUNT
frontend-evening   0 18 * * *   Europe/Moscow   frontend-scaler
frontend-morning   0 9 * * *    Europe/Moscow   frontend-scaler
```

Команда (Bash):
```
kubectl -n hw4 auth can-i patch deployment/counter-frontend --subresource=scale --as=system:serviceaccount:hw4:frontend-scaler
```
Вывод (text):
```
yes
```

Команда (Bash):
```
kubectl -n hw4 auth can-i patch deployment/counter-backend --subresource=scale --as=system:serviceaccount:hw4:frontend-scaler
```
Вывод (text):
```
no
```

Команда (Bash):
```
kubectl -n hw4 auth can-i get secrets --as=system:serviceaccount:hw4:frontend-scaler
```
Вывод (text):
```
no
```

Команда (Bash):
```
kubectl -n hw4 auth can-i delete pods --as=system:serviceaccount:hw4:frontend-scaler
```
Вывод (text):
```
no
```

Команда (Bash):
```
kubectl -n hw4 auth can-i patch deployment/counter-frontend --as=system:serviceaccount:hw4:frontend-scaler
```
Вывод (text):
```
no
```

Команда (Bash):
```
kubectl -n hw4 create job manual-morning --from=cronjob/frontend-morning
kubectl -n hw4 wait --for=condition=complete job/manual-morning --timeout=120s
kubectl -n hw4 logs job/manual-morning
kubectl -n hw4 rollout status deploy/counter-frontend --timeout=120s
kubectl -n hw4 get deploy counter-frontend
```
Вывод (text):
```
job.batch/manual-morning created
job.batch/manual-morning condition met
counter-frontend replicas = 3
Waiting for deployment "counter-frontend" rollout to finish: 1 of 3 updated replicas are available...
deployment "counter-frontend" successfully rolled out
NAME               READY   UP-TO-DATE   AVAILABLE   AGE
counter-frontend   3/3     3            3           12m
```

Команда (Bash):
```
kubectl -n hw4 create job manual-evening --from=cronjob/frontend-evening
kubectl -n hw4 wait --for=condition=complete job/manual-evening --timeout=120s
kubectl -n hw4 logs job/manual-evening
kubectl -n hw4 rollout status deploy/counter-frontend --timeout=120s
kubectl -n hw4 get deploy counter-frontend
```
Вывод (text):
```
job.batch/manual-evening created
job.batch/manual-evening condition met
counter-frontend replicas = 1
deployment "counter-frontend" successfully rolled out
NAME               READY   UP-TO-DATE   AVAILABLE   AGE
counter-frontend   1/1     1            1           12m
```

## 4.1. Две установки Helm

Имена ресурсов содержат имя релиза. Namespace передаётся Helm, адрес, образы, порты, реплики и ресурсы задаются в values. TLS-ключ передаётся из локального файла через `--set-file`, в репозитории его нет.

Команда (Bash):
```
helm upgrade --install second ./chart -n hw4-second --create-namespace --set host=second.counter.localtest.me --set tls.create=true --set-file tls.crt=.secrets/server.crt --set-file tls.key=.secrets/server.key --wait --timeout 240s
```
Вывод (text):
```
Release "second" does not exist. Installing it now.
NAME: second
LAST DEPLOYED: Fri Oct 23 19:05:04 2026
NAMESPACE: hw4-second
STATUS: deployed
REVISION: 1
TEST SUITE: None
```

Команда (Bash):
```
helm list -A
kubectl get ingress -A
curl --fail --silent --show-error --cacert .secrets/server.crt --connect-to counter.localtest.me:443:127.0.0.1:8443 https://counter.localtest.me/api/counter
printf '
'
curl --fail --silent --show-error --cacert .secrets/server.crt --connect-to second.counter.localtest.me:443:127.0.0.1:8443 https://second.counter.localtest.me/api/counter
printf '
'
kubectl -n hw4-second logs job/second-check
```
Вывод (text):
```
NAME       	NAMESPACE  	REVISION	UPDATED                                	STATUS  	CHART                        	APP VERSION
counter    	hw4        	4       	2026-10-23 19:03:48.344267901 +0300 MSK	deployed	counter-0.1.0                	hw4-v1     
second     	hw4-second 	1       	2026-10-23 19:05:04.611450307 +0300 MSK	deployed	counter-0.1.0                	hw4-v1     
traefik    	kube-system	1       	2026-10-23 15:54:45.424359283 +0000 UTC	deployed	traefik-39.0.701+up39.0.7    	v3.6.12    
traefik-crd	kube-system	1       	2026-10-23 15:54:43.489021008 +0000 UTC	deployed	traefik-crd-39.0.701+up39.0.7	v3.6.12    
NAMESPACE    NAME      CLASS     HOSTS                         ADDRESS      PORTS     AGE
hw4-second   second    traefik   second.counter.localtest.me   172.19.0.2   80, 443   8s
hw4          counter   traefik   counter.localtest.me          172.19.0.2   80, 443   10m
{"count": 0}
{"count": 0}
http://second-frontend:8080/ 200
http://second-backend:9000/api/counter 200
```

## 4.2. Конфигурация, проверка и откат

Checksum ConfigMap в шаблоне Pod вызывает перезапуск при изменении параметров. Job с hook `post-install,post-upgrade,post-rollback` автоматически проверяет frontend и backend. Перед чтением PORT дождался удаления старого Pod, чтобы команда не попала в завершающийся контейнер.

Команда (Bash):
```
set -euo pipefail
OLD_POD=$(kubectl -n hw4 get pod -l app=counter-backend -o jsonpath='{.items[0].metadata.name}')
kubectl -n hw4 get pod "$OLD_POD" -o custom-columns=NAME:.metadata.name,UID:.metadata.uid,IMAGE:.spec.containers[0].image
helm upgrade counter ./chart -n hw4 --reuse-values --set backend.port=9001 --set-string changeCause='Backend port 9000 to 9001' --wait --timeout 180s
kubectl -n hw4 rollout status deploy/counter-backend --timeout=120s
kubectl -n hw4 wait --for=delete pod/"$OLD_POD" --timeout=90s
kubectl -n hw4 get pods -l app=counter-backend -o custom-columns=NAME:.metadata.name,UID:.metadata.uid,IMAGE:.spec.containers[0].image
kubectl -n hw4 exec deploy/counter-backend -- printenv PORT
kubectl -n hw4 logs job/counter-check
helm history counter -n hw4
```
Вывод (text):
```
NAME                               UID                                    IMAGE
counter-backend-6d647ddc8f-sxxpg   bae2e28c-6067-4a7c-a65a-ded58ca80eab   counter-backend:hw4-v2
Release "counter" has been upgraded. Happy Helming!
NAME: counter
LAST DEPLOYED: Fri Oct 23 19:07:23 2026
NAMESPACE: hw4
STATUS: deployed
REVISION: 7
TEST SUITE: None
deployment "counter-backend" successfully rolled out
pod/counter-backend-6d647ddc8f-sxxpg condition met
NAME                             UID                                    IMAGE
counter-backend-bcd785f6-7tstp   af218a8c-6a03-4cee-81f2-fe9e5c8499c7   counter-backend:hw4-v2
9001
http://counter-frontend:8080/ 200
http://counter-backend:9001/api/counter 200
REVISION	UPDATED                 	STATUS    	CHART        	APP VERSION	DESCRIPTION     
1       	Fri Oct 23 18:54:27 2026	superseded	counter-0.1.0	hw4-v1     	Install complete
2       	Fri Oct 23 19:01:51 2026	superseded	counter-0.1.0	hw4-v1     	Upgrade complete
3       	Fri Oct 23 19:03:40 2026	superseded	counter-0.1.0	hw4-v1     	Upgrade complete
4       	Fri Oct 23 19:03:48 2026	superseded	counter-0.1.0	hw4-v1     	Upgrade complete
5       	Fri Oct 23 19:05:12 2026	superseded	counter-0.1.0	hw4-v1     	Upgrade complete
6       	Fri Oct 23 19:05:21 2026	superseded	counter-0.1.0	hw4-v1     	Rollback to 4   
7       	Fri Oct 23 19:07:23 2026	deployed  	counter-0.1.0	hw4-v1     	Upgrade complete
```

Команда (Bash):
```
set -euo pipefail
OLD_POD=$(kubectl -n hw4 get pod -l app=counter-backend -o jsonpath='{.items[0].metadata.name}')
helm rollback counter -n hw4 --wait --timeout 180s
kubectl -n hw4 rollout status deploy/counter-backend --timeout=120s
kubectl -n hw4 wait --for=delete pod/"$OLD_POD" --timeout=90s
kubectl -n hw4 exec deploy/counter-backend -- printenv PORT
kubectl -n hw4 logs job/counter-check
helm history counter -n hw4
```
Вывод (text):
```
Rollback was a success! Happy Helming!
deployment "counter-backend" successfully rolled out
pod/counter-backend-bcd785f6-7tstp condition met
9000
http://counter-frontend:8080/ 200
http://counter-backend:9000/api/counter 200
REVISION	UPDATED                 	STATUS    	CHART        	APP VERSION	DESCRIPTION     
1       	Fri Oct 23 18:54:27 2026	superseded	counter-0.1.0	hw4-v1     	Install complete
2       	Fri Oct 23 19:01:51 2026	superseded	counter-0.1.0	hw4-v1     	Upgrade complete
3       	Fri Oct 23 19:03:40 2026	superseded	counter-0.1.0	hw4-v1     	Upgrade complete
4       	Fri Oct 23 19:03:48 2026	superseded	counter-0.1.0	hw4-v1     	Upgrade complete
5       	Fri Oct 23 19:05:12 2026	superseded	counter-0.1.0	hw4-v1     	Upgrade complete
6       	Fri Oct 23 19:05:21 2026	superseded	counter-0.1.0	hw4-v1     	Rollback to 4   
7       	Fri Oct 23 19:07:23 2026	superseded	counter-0.1.0	hw4-v1     	Upgrade complete
8       	Fri Oct 23 19:07:41 2026	deployed  	counter-0.1.0	hw4-v1     	Rollback to 6
```

## Дополнительно. PostgreSQL в чарте

`database.enabled=true` включает БД; у второго релиза параметр оставлен false. Аннотация `helm.sh/resource-policy: keep` сохраняет PVC при удалении релиза. При повторной установке с тем же именем и namespace используется прежний PVC и тот же Secret. После удаления и новой установки история Helm начинается с ревизии 1.

Команда (Bash):
```
kubectl -n hw4 exec counter-postgres-0 -- psql -U counter -d counter -c 'TABLE visits;'
```
Вывод (text):
```
id |           note            
----+---------------------------
  1 | created by init.sql
  2 | saved before pod deletion
(2 rows)
```

Команда (Bash):
```
helm uninstall counter -n hw4 && kubectl -n hw4 wait --for=delete pod/counter-postgres-0 --timeout=90s && kubectl -n hw4 get pvc && kubectl -n hw4 get secret postgres-auth
```
Вывод (text):
```
These resources were kept due to the resource policy:
[PersistentVolumeClaim] counter-postgres-data

release "counter" uninstalled
pod/counter-postgres-0 condition met
NAME                    STATUS   VOLUME                                     CAPACITY   ACCESS MODES   STORAGECLASS   VOLUMEATTRIBUTESCLASS   AGE
counter-postgres-data   Bound    pvc-7ff61715-2ee2-4a2c-8d11-4df4a8b4e3ff   256Mi      RWO            local-path     <unset>                 13m
NAME            TYPE     DATA   AGE
postgres-auth   Opaque   1      13m
```

Команда (Bash):
```
helm upgrade --install counter ./chart -n hw4 --set database.enabled=true --set tls.create=true --set-file tls.crt=.secrets/server.crt --set-file tls.key=.secrets/server.key --wait --timeout 300s
```
Вывод (text):
```
Release "counter" does not exist. Installing it now.
NAME: counter
LAST DEPLOYED: Fri Oct 23 19:08:00 2026
NAMESPACE: hw4
STATUS: deployed
REVISION: 1
TEST SUITE: None
```

Команда (Bash):
```
kubectl -n hw4 exec counter-postgres-0 -- psql -U counter -d counter -c 'TABLE visits;'
```
Вывод (text):
```
id |           note            
----+---------------------------
  1 | created by init.sql
  2 | saved before pod deletion
(2 rows)
```

## Итоговая проверка

Манифесты повторно сформированы из окончательного чарта. Мониторинг HW3 снова запущен.

Команда (Bash):
```
helm lint ./chart
helm template counter ./chart -n hw4 --set database.enabled=true > manifests/counter.yaml
helm template counter ./chart -n hw4 --set database.enabled=true --show-only templates/database.yaml > manifests/postgres.yaml
kubectl apply --dry-run=server -f manifests/node-exporter.yaml -f manifests/scaler.yaml -f manifests/scale-morning.yaml -f manifests/scale-evening.yaml
```
Вывод (text):
```
==> Linting ./chart
[INFO] Chart.yaml: icon is recommended

1 chart(s) linted, 0 chart(s) failed
daemonset.apps/node-exporter unchanged (server dry run)
serviceaccount/frontend-scaler unchanged (server dry run)
role.rbac.authorization.k8s.io/frontend-scaler unchanged (server dry run)
rolebinding.rbac.authorization.k8s.io/frontend-scaler unchanged (server dry run)
cronjob.batch/frontend-morning unchanged (server dry run)
cronjob.batch/frontend-evening unchanged (server dry run)
```

Команда (Bash):
```
kubectl -n hw4 get deployment,statefulset,daemonset,pods
kubectl -n hw4-second get deployment,pods
kubectl -n hw4 get pods -o custom-columns=NAME:.metadata.name,QOS:.status.qosClass,REQUESTS:.spec.containers[*].resources.requests,LIMITS:.spec.containers[*].resources.limits
curl --fail --silent --show-error --cacert .secrets/server.crt --connect-to counter.localtest.me:443:127.0.0.1:8443 https://counter.localtest.me/api/counter
printf '
'
kubectl -n hw4 exec counter-postgres-0 -- psql -U counter -d counter -c 'TABLE visits;'
```
Вывод (text):
```
NAME                               READY   UP-TO-DATE   AVAILABLE   AGE
deployment.apps/counter-backend    1/1     1            1           4m49s
deployment.apps/counter-frontend   1/1     1            1           4m49s

NAME                                READY   AGE
statefulset.apps/counter-postgres   1/1     4m49s

NAME                           DESIRED   CURRENT   READY   UP-TO-DATE   AVAILABLE   NODE SELECTOR   AGE
daemonset.apps/node-exporter   1         1         1       1            1           <none>          6m31s

NAME                                    READY   STATUS      RESTARTS   AGE
pod/counter-backend-5b78fdc468-zrdjn    1/1     Running     0          4m48s
pod/counter-check-g2n85                 0/1     Completed   0          4m44s
pod/counter-frontend-5c8f94b875-fbt24   1/1     Running     0          4m48s
pod/counter-postgres-0                  1/1     Running     0          4m48s
pod/db-client-ngrpd                     0/1     Completed   0          11m
pod/manual-evening-rbzps                0/1     Completed   0          5m45s
pod/manual-morning-xw4c5                0/1     Completed   0          5m54s
pod/node-exporter-rpqxv                 1/1     Running     0          6m30s
NAME                              READY   UP-TO-DATE   AVAILABLE   AGE
deployment.apps/second-backend    1/1     1            1           7m45s
deployment.apps/second-frontend   1/1     1            1           7m45s

NAME                                   READY   STATUS      RESTARTS   AGE
pod/second-backend-995cd7cc8-b6r97     1/1     Running     0          7m44s
pod/second-check-hwnzp                 0/1     Completed   0          7m41s
pod/second-frontend-6546cd796c-jrgz5   1/1     Running     0          7m44s
NAME                                QOS         REQUESTS                   LIMITS
counter-backend-5b78fdc468-zrdjn    Burstable   map[cpu:25m memory:32Mi]   map[cpu:300m memory:96Mi]
counter-check-g2n85                 Burstable   map[cpu:10m memory:16Mi]   map[cpu:100m memory:64Mi]
counter-frontend-5c8f94b875-fbt24   Burstable   map[cpu:25m memory:64Mi]   map[cpu:400m memory:256Mi]
counter-postgres-0                  Burstable   map[cpu:25m memory:64Mi]   map[cpu:300m memory:192Mi]
db-client-ngrpd                     Burstable   map[cpu:10m memory:16Mi]   map[cpu:100m memory:64Mi]
manual-evening-rbzps                Burstable   map[cpu:10m memory:16Mi]   map[cpu:100m memory:64Mi]
manual-morning-xw4c5                Burstable   map[cpu:10m memory:16Mi]   map[cpu:100m memory:64Mi]
node-exporter-rpqxv                 Burstable   map[cpu:10m memory:16Mi]   map[cpu:100m memory:64Mi]
{"count": 1}
 id |           note            
----+---------------------------
  1 | created by init.sql
  2 | saved before pod deletion
(2 rows)
```

Команда (Bash):
```
docker ps --format '{{.Names}}: {{.Status}}'
curl --fail --silent --show-error http://127.0.0.1:3000/api/health
curl --fail --silent --show-error http://127.0.0.1:9090/-/ready
free -h
df -h /
```
Вывод (text):
```
k3d-hw4-serverlb: Up 4 hours
k3d-hw4-server-0: Up 4 hours
hw3-monitoring-grafana-1: Up 4 hours
hw3-monitoring-prometheus-1: Up 4 hours
hw3-monitoring-node-exporter-1: Up 4 hours
nginx-letsencrypt: Up 4 hours
{
  "database": "ok",
  "version": "12.1.0",
  "commit": "ccd7b6ce7ea6184b8c7eb1de044174147dd9a648"
}Prometheus Server is Ready.
               total        used        free      shared  buff/cache   available
Mem:           3.3Gi       2.0Gi       101Mi        17Mi       1.5Gi       1.3Gi
Swap:          3.3Gi       833Mi       2.5Gi
Filesystem      Size  Used Avail Use% Mounted on
/dev/sda2        20G   17G  2.2G  89% /
```

## Материалы

- [Лекция 5](https://github.com/NaxNax666/DEVOPS2-2026/blob/main/lectrues/Lecture5.md), [семинар 5](https://github.com/NaxNax666/DEVOPS2-2026/blob/main/seminars/Seminar5.md).
- [StatefulSet](https://kubernetes.io/docs/concepts/workloads/controllers/statefulset/), [DaemonSet](https://kubernetes.io/docs/concepts/workloads/controllers/daemonset/).
- [CronJob и timeZone](https://kubernetes.io/docs/concepts/workloads/controllers/cron-jobs/), [RBAC](https://kubernetes.io/docs/reference/access-authn-authz/rbac/).
- [Helm hooks](https://helm.sh/docs/topics/charts_hooks/), [checksum и сохранение ресурсов](https://helm.sh/docs/howto/charts_tips_and_tricks/).
