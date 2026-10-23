Команда (Bash):
```
docker build -t counter-backend:hw4-v1 ./counter-backend
```
Вывод (text):
```
#0 building with "default" instance using docker driver

#1 [internal] load build definition from Dockerfile
#1 transferring dockerfile: 930B done
#1 DONE 0.0s

#2 [internal] load metadata for docker.io/library/python:3.11-slim-bookworm
#2 DONE 2.9s

#3 [internal] load .dockerignore
#3 transferring context: 121B done
#3 DONE 0.0s

#4 [internal] load build context
#4 DONE 0.0s

#5 [base 1/1] FROM docker.io/library/python:3.11-slim-bookworm@sha256:f06d01d4ba3f8ad5af45a3ec87df19c1d317d8e8961edc0fabda61811af6f7cf
#5 resolve docker.io/library/python:3.11-slim-bookworm@sha256:f06d01d4ba3f8ad5af45a3ec87df19c1d317d8e8961edc0fabda61811af6f7cf
#5 resolve docker.io/library/python:3.11-slim-bookworm@sha256:f06d01d4ba3f8ad5af45a3ec87df19c1d317d8e8961edc0fabda61811af6f7cf 1.0s done
#5 DONE 1.0s

#4 [internal] load build context
#4 transferring context: 92.02kB done
#4 DONE 0.0s

#5 [base 1/1] FROM docker.io/library/python:3.11-slim-bookworm@sha256:f06d01d4ba3f8ad5af45a3ec87df19c1d317d8e8961edc0fabda61811af6f7cf
#5 sha256:efd623ba8e536eb877739a1b5d5a43f48fdea8143a8de7ab5331a100f6df1b80 0B / 250B 0.2s
#5 sha256:fe9b55673e95e44e6b867088bbaa2ade7d1e259c40c6fe8a6b2190b6a8366497 0B / 16.03MB 0.2s
#5 sha256:5938c3a3cfef8c7171a52090e5a46e274e21e3860a258dfa9a9f64e5909f25db 0B / 3.34MB 0.2s
#5 sha256:efd623ba8e536eb877739a1b5d5a43f48fdea8143a8de7ab5331a100f6df1b80 250B / 250B 0.6s done
#5 sha256:5938c3a3cfef8c7171a52090e5a46e274e21e3860a258dfa9a9f64e5909f25db 3.34MB / 3.34MB 1.3s done
#5 extracting sha256:5938c3a3cfef8c7171a52090e5a46e274e21e3860a258dfa9a9f64e5909f25db
#5 sha256:fe9b55673e95e44e6b867088bbaa2ade7d1e259c40c6fe8a6b2190b6a8366497 2.10MB / 16.03MB 1.5s
#5 extracting sha256:5938c3a3cfef8c7171a52090e5a46e274e21e3860a258dfa9a9f64e5909f25db 0.1s done
#5 sha256:fe9b55673e95e44e6b867088bbaa2ade7d1e259c40c6fe8a6b2190b6a8366497 5.24MB / 16.03MB 1.7s
#5 sha256:fe9b55673e95e44e6b867088bbaa2ade7d1e259c40c6fe8a6b2190b6a8366497 8.39MB / 16.03MB 1.8s
#5 sha256:fe9b55673e95e44e6b867088bbaa2ade7d1e259c40c6fe8a6b2190b6a8366497 12.58MB / 16.03MB 2.0s
#5 sha256:fe9b55673e95e44e6b867088bbaa2ade7d1e259c40c6fe8a6b2190b6a8366497 16.03MB / 16.03MB 2.1s
#5 sha256:fe9b55673e95e44e6b867088bbaa2ade7d1e259c40c6fe8a6b2190b6a8366497 16.03MB / 16.03MB 2.1s done
#5 extracting sha256:fe9b55673e95e44e6b867088bbaa2ade7d1e259c40c6fe8a6b2190b6a8366497
#5 extracting sha256:fe9b55673e95e44e6b867088bbaa2ade7d1e259c40c6fe8a6b2190b6a8366497 0.4s done
#5 DONE 3.5s

#5 [base 1/1] FROM docker.io/library/python:3.11-slim-bookworm@sha256:f06d01d4ba3f8ad5af45a3ec87df19c1d317d8e8961edc0fabda61811af6f7cf
#5 extracting sha256:efd623ba8e536eb877739a1b5d5a43f48fdea8143a8de7ab5331a100f6df1b80 done
#5 DONE 3.5s

#6 [build 1/5] RUN pip install --no-cache-dir 'poetry==1.8.*'
#6 2.005 Collecting poetry==1.8.*
#6 2.396   Downloading poetry-1.8.5-py3-none-any.whl.metadata (6.9 kB)
#6 2.491 Collecting build<2.0.0,>=1.0.3 (from poetry==1.8.*)
#6 2.557   Downloading build-1.6.1-py3-none-any.whl.metadata (5.6 kB)
#6 2.654 Collecting cachecontrol<0.15.0,>=0.14.0 (from cachecontrol[filecache]<0.15.0,>=0.14.0->poetry==1.8.*)
#6 2.725   Downloading cachecontrol-0.14.4-py3-none-any.whl.metadata (3.1 kB)
#6 2.852 Collecting cleo<3.0.0,>=2.1.0 (from poetry==1.8.*)
#6 2.942   Downloading cleo-2.1.0-py3-none-any.whl.metadata (12 kB)
#6 3.061 Collecting crashtest<0.5.0,>=0.4.1 (from poetry==1.8.*)
#6 3.151   Downloading crashtest-0.4.1-py3-none-any.whl.metadata (1.1 kB)
#6 3.525 Collecting dulwich<0.22.0,>=0.21.2 (from poetry==1.8.*)
#6 3.601   Downloading dulwich-0.21.7-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (4.3 kB)
#6 3.704 Collecting fastjsonschema<3.0.0,>=2.18.0 (from poetry==1.8.*)
#6 3.786   Downloading fastjsonschema-2.22.2-py3-none-any.whl.metadata (2.1 kB)
#6 3.867 Collecting installer<0.8.0,>=0.7.0 (from poetry==1.8.*)
#6 3.937   Downloading installer-0.7.0-py3-none-any.whl.metadata (936 bytes)
#6 4.063 Collecting keyring<25.0.0,>=24.0.0 (from poetry==1.8.*)
#6 4.134   Downloading keyring-24.3.1-py3-none-any.whl.metadata (20 kB)
#6 4.164 Requirement already satisfied: packaging>=23.1 in /usr/local/lib/python3.11/site-packages (from poetry==1.8.*) (26.3)
#6 4.240 Collecting pexpect<5.0.0,>=4.7.0 (from poetry==1.8.*)
#6 4.317   Downloading pexpect-4.9.0-py2.py3-none-any.whl.metadata (2.5 kB)
#6 4.405 Collecting pkginfo<2.0,>=1.12 (from poetry==1.8.*)
#6 4.473   Downloading pkginfo-1.13.3-py3-none-any.whl.metadata (14 kB)
#6 4.588 Collecting platformdirs<5,>=3.0.0 (from poetry==1.8.*)
#6 4.662   Downloading platformdirs-4.13.5-py3-none-any.whl.metadata (5.5 kB)
#6 4.768 Collecting poetry-core==1.9.1 (from poetry==1.8.*)
#6 4.843   Downloading poetry_core-1.9.1-py3-none-any.whl.metadata (3.5 kB)
#6 4.950 Collecting poetry-plugin-export<2.0.0,>=1.6.0 (from poetry==1.8.*)
#6 5.030   Downloading poetry_plugin_export-1.10.1-py3-none-any.whl.metadata (3.7 kB)
#6 5.117 Collecting pyproject-hooks<2.0.0,>=1.0.0 (from poetry==1.8.*)
#6 5.195   Downloading pyproject_hooks-1.3.3-py3-none-any.whl.metadata (1.3 kB)
#6 5.612 Collecting requests<3.0,>=2.26 (from poetry==1.8.*)
#6 5.691   Downloading requests-2.34.2-py3-none-any.whl.metadata (4.8 kB)
#6 5.793 Collecting requests-toolbelt<2.0.0,>=1.0.0 (from poetry==1.8.*)
#6 6.182   Downloading requests_toolbelt-1.0.0-py2.py3-none-any.whl.metadata (14 kB)
#6 6.290 Collecting shellingham<2.0,>=1.5 (from poetry==1.8.*)
#6 6.361   Downloading shellingham-1.5.4-py2.py3-none-any.whl.metadata (3.5 kB)
#6 6.494 Collecting tomlkit<1.0.0,>=0.11.4 (from poetry==1.8.*)
#6 6.572   Downloading tomlkit-0.15.2-py3-none-any.whl.metadata (3.4 kB)
#6 6.676 Collecting trove-classifiers>=2022.5.19 (from poetry==1.8.*)
#6 6.752   Downloading trove_classifiers-2026.9.21.13-py3-none-any.whl.metadata (2.4 kB)
#6 6.927 Collecting virtualenv<21.0.0,>=20.26.6 (from poetry==1.8.*)
#6 7.005   Downloading virtualenv-20.39.1-py3-none-any.whl.metadata (3.5 kB)
#6 7.201 Collecting msgpack<2.0.0,>=0.5.2 (from cachecontrol<0.15.0,>=0.14.0->cachecontrol[filecache]<0.15.0,>=0.14.0->poetry==1.8.*)
#6 7.318   Downloading msgpack-1.2.3-cp311-cp311-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl.metadata (8.3 kB)
#6 7.444 Collecting filelock>=3.8.0 (from cachecontrol[filecache]<0.15.0,>=0.14.0->poetry==1.8.*)
#6 7.514   Downloading filelock-4.2.4-py3-none-any.whl.metadata (2.0 kB)
#6 8.212 Collecting rapidfuzz<4.0.0,>=3.0.0 (from cleo<3.0.0,>=2.1.0->poetry==1.8.*)
#6 8.291   Downloading rapidfuzz-3.14.6-cp311-cp311-manylinux_2_27_x86_64.manylinux_2_28_x86_64.whl.metadata (12 kB)
#6 8.458 Collecting urllib3>=1.25 (from dulwich<0.22.0,>=0.21.2->poetry==1.8.*)
#6 8.535   Downloading urllib3-2.8.0-py3-none-any.whl.metadata (7.4 kB)
#6 8.655 Collecting jaraco.classes (from keyring<25.0.0,>=24.0.0->poetry==1.8.*)
#6 8.730   Downloading jaraco.classes-3.4.0-py3-none-any.whl.metadata (2.6 kB)
#6 8.860 Collecting importlib-metadata>=4.11.4 (from keyring<25.0.0,>=24.0.0->poetry==1.8.*)
#6 8.944   Downloading importlib_metadata-9.1.0-py3-none-any.whl.metadata (4.5 kB)
#6 9.032 Collecting SecretStorage>=3.2 (from keyring<25.0.0,>=24.0.0->poetry==1.8.*)
#6 9.105   Downloading secretstorage-3.5.0-py3-none-any.whl.metadata (4.0 kB)
#6 9.211 Collecting jeepney>=0.4.2 (from keyring<25.0.0,>=24.0.0->poetry==1.8.*)
#6 9.281   Downloading jeepney-0.9.0-py3-none-any.whl.metadata (1.2 kB)
#6 9.366 Collecting ptyprocess>=0.5 (from pexpect<5.0.0,>=4.7.0->poetry==1.8.*)
#6 9.438   Downloading ptyprocess-0.7.0-py2.py3-none-any.whl.metadata (1.3 kB)
#6 9.457 INFO: pip is looking at multiple versions of poetry-plugin-export to determine which version is compatible with other requirements. This could take a while.
#6 9.461 Collecting poetry-plugin-export<2.0.0,>=1.6.0 (from poetry==1.8.*)
#6 9.536   Downloading poetry_plugin_export-1.10.0-py3-none-any.whl.metadata (3.6 kB)
#6 9.613   Downloading poetry_plugin_export-1.9.0-py3-none-any.whl.metadata (3.1 kB)
#6 9.708   Downloading poetry_plugin_export-1.8.0-py3-none-any.whl.metadata (2.8 kB)
#6 9.958 Collecting charset_normalizer<4,>=2 (from requests<3.0,>=2.26->poetry==1.8.*)
#6 10.04   Downloading charset_normalizer-3.5.2-cp311-cp311-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl.metadata (46 kB)
#6 10.07      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 46.4/46.4 kB 1.4 MB/s eta 0:00:00
#6 10.17 Collecting idna<4,>=2.5 (from requests<3.0,>=2.26->poetry==1.8.*)
#6 10.25   Downloading idna-3.20-py3-none-any.whl.metadata (7.2 kB)
#6 10.35 Collecting certifi>=2023.5.7 (from requests<3.0,>=2.26->poetry==1.8.*)
#6 10.43   Downloading certifi-2026.10.23-py3-none-any.whl.metadata (2.5 kB)
#6 10.56 Collecting distlib<1,>=0.3.7 (from virtualenv<21.0.0,>=20.26.6->poetry==1.8.*)
#6 10.64   Downloading distlib-0.4.4-py2.py3-none-any.whl.metadata (5.3 kB)
#6 10.65 Collecting filelock>=3.8.0 (from cachecontrol[filecache]<0.15.0,>=0.14.0->poetry==1.8.*)
#6 10.72   Downloading filelock-3.32.7-py3-none-any.whl.metadata (2.0 kB)
#6 10.86 Collecting zipp>=3.20 (from importlib-metadata>=4.11.4->keyring<25.0.0,>=24.0.0->poetry==1.8.*)
#6 10.93   Downloading zipp-4.1.2-py3-none-any.whl.metadata (3.6 kB)
#6 11.35 Collecting cryptography>=2.0 (from SecretStorage>=3.2->keyring<25.0.0,>=24.0.0->poetry==1.8.*)
#6 11.42   Downloading cryptography-50.0.2-cp311-abi3-manylinux_2_34_x86_64.whl.metadata (4.4 kB)
#6 11.54 Collecting more-itertools (from jaraco.classes->keyring<25.0.0,>=24.0.0->poetry==1.8.*)
#6 11.61   Downloading more_itertools-11.2.1-py3-none-any.whl.metadata (42 kB)
#6 11.63      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 42.7/42.7 kB 2.8 MB/s eta 0:00:00
#6 11.83 Collecting cffi>=2.0.0 (from cryptography>=2.0->SecretStorage>=3.2->keyring<25.0.0,>=24.0.0->poetry==1.8.*)
#6 11.91   Downloading cffi-2.1.1-cp311-cp311-manylinux2014_x86_64.manylinux_2_17_x86_64.whl.metadata (2.5 kB)
#6 12.02 Collecting pycparser (from cffi>=2.0.0->cryptography>=2.0->SecretStorage>=3.2->keyring<25.0.0,>=24.0.0->poetry==1.8.*)
#6 12.09   Downloading pycparser-3.12-py3-none-any.whl.metadata (9.7 kB)
#6 12.18 Downloading poetry-1.8.5-py3-none-any.whl (249 kB)
#6 12.33    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 250.0/250.0 kB 1.7 MB/s eta 0:00:00
#6 12.41 Downloading poetry_core-1.9.1-py3-none-any.whl (309 kB)
#6 12.52    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 309.5/309.5 kB 2.8 MB/s eta 0:00:00
#6 12.60 Downloading build-1.6.1-py3-none-any.whl (31 kB)
#6 12.68 Downloading cachecontrol-0.14.4-py3-none-any.whl (22 kB)
#6 12.77 Downloading cleo-2.1.0-py3-none-any.whl (78 kB)
#6 12.79    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 78.7/78.7 kB 4.2 MB/s eta 0:00:00
#6 12.87 Downloading crashtest-0.4.1-py3-none-any.whl (7.6 kB)
#6 12.94 Downloading dulwich-0.21.7-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (516 kB)
#6 13.13    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 516.4/516.4 kB 2.8 MB/s eta 0:00:00
#6 13.20 Downloading fastjsonschema-2.22.2-py3-none-any.whl (27 kB)
#6 13.29 Downloading installer-0.7.0-py3-none-any.whl (453 kB)
#6 13.42    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 453.8/453.8 kB 3.6 MB/s eta 0:00:00
#6 13.49 Downloading keyring-24.3.1-py3-none-any.whl (38 kB)
#6 13.58 Downloading pexpect-4.9.0-py2.py3-none-any.whl (63 kB)
#6 13.59    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 63.8/63.8 kB 5.6 MB/s eta 0:00:00
#6 13.66 Downloading pkginfo-1.13.3-py3-none-any.whl (35 kB)
#6 13.73 Downloading platformdirs-4.13.5-py3-none-any.whl (32 kB)
#6 13.80 Downloading poetry_plugin_export-1.8.0-py3-none-any.whl (10 kB)
#6 13.88 Downloading pyproject_hooks-1.3.3-py3-none-any.whl (10 kB)
#6 13.97 Downloading requests-2.34.2-py3-none-any.whl (73 kB)
#6 13.99    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 73.1/73.1 kB 3.9 MB/s eta 0:00:00
#6 14.06 Downloading requests_toolbelt-1.0.0-py2.py3-none-any.whl (54 kB)
#6 14.08    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 54.5/54.5 kB 4.3 MB/s eta 0:00:00
#6 14.15 Downloading shellingham-1.5.4-py2.py3-none-any.whl (9.8 kB)
#6 14.22 Downloading tomlkit-0.15.2-py3-none-any.whl (52 kB)
#6 14.23    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 52.2/52.2 kB 4.4 MB/s eta 0:00:00
#6 14.30 Downloading trove_classifiers-2026.9.21.13-py3-none-any.whl (14 kB)
#6 14.37 Downloading virtualenv-20.39.1-py3-none-any.whl (5.8 MB)
#6 15.51    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 5.8/5.8 MB 5.1 MB/s eta 0:00:00
#6 15.59 Downloading certifi-2026.10.23-py3-none-any.whl (135 kB)
#6 15.60    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 135.1/135.1 kB 11.0 MB/s eta 0:00:00
#6 15.67 Downloading charset_normalizer-3.5.2-cp311-cp311-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl (269 kB)
#6 15.70    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 270.0/270.0 kB 10.0 MB/s eta 0:00:00
#6 15.78 Downloading distlib-0.4.4-py2.py3-none-any.whl (472 kB)
#6 15.82    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 472.1/472.1 kB 10.4 MB/s eta 0:00:00
#6 15.90 Downloading filelock-3.32.7-py3-none-any.whl (100 kB)
#6 15.91    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100.2/100.2 kB 10.4 MB/s eta 0:00:00
#6 15.98 Downloading idna-3.20-py3-none-any.whl (69 kB)
#6 15.99    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 69.6/69.6 kB 7.3 MB/s eta 0:00:00
#6 16.06 Downloading importlib_metadata-9.1.0-py3-none-any.whl (28 kB)
#6 16.14 Downloading jeepney-0.9.0-py3-none-any.whl (49 kB)
#6 16.15    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 49.0/49.0 kB 11.4 MB/s eta 0:00:00
#6 16.23 Downloading msgpack-1.2.3-cp311-cp311-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl (477 kB)
#6 16.30    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 477.8/477.8 kB 7.8 MB/s eta 0:00:00
#6 16.37 Downloading ptyprocess-0.7.0-py2.py3-none-any.whl (13 kB)
#6 16.45 Downloading rapidfuzz-3.14.6-cp311-cp311-manylinux_2_27_x86_64.manylinux_2_28_x86_64.whl (3.2 MB)
#6 16.79    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 3.2/3.2 MB 9.4 MB/s eta 0:00:00
#6 16.86 Downloading secretstorage-3.5.0-py3-none-any.whl (15 kB)
#6 16.93 Downloading urllib3-2.8.0-py3-none-any.whl (135 kB)
#6 16.94    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 135.7/135.7 kB 18.3 MB/s eta 0:00:00
#6 17.01 Downloading jaraco.classes-3.4.0-py3-none-any.whl (6.8 kB)
#6 17.08 Downloading cryptography-50.0.2-cp311-abi3-manylinux_2_34_x86_64.whl (4.8 MB)
#6 17.50    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 4.8/4.8 MB 11.3 MB/s eta 0:00:00
#6 17.57 Downloading zipp-4.1.2-py3-none-any.whl (10 kB)
#6 17.63 Downloading more_itertools-11.2.1-py3-none-any.whl (74 kB)
#6 17.64    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 74.4/74.4 kB 33.2 MB/s eta 0:00:00
#6 17.71 Downloading cffi-2.1.1-cp311-cp311-manylinux2014_x86_64.manylinux_2_17_x86_64.whl (217 kB)
#6 17.73    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 217.8/217.8 kB 12.5 MB/s eta 0:00:00
#6 17.80 Downloading pycparser-3.12-py3-none-any.whl (62 kB)
#6 17.81    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 62.6/62.6 kB 9.7 MB/s eta 0:00:00
#6 17.96 Installing collected packages: trove-classifiers, ptyprocess, distlib, zipp, urllib3, tomlkit, shellingham, rapidfuzz, pyproject-hooks, pycparser, poetry-core, platformdirs, pkginfo, pexpect, msgpack, more-itertools, jeepney, installer, idna, filelock, fastjsonschema, crashtest, charset_normalizer, certifi, virtualenv, requests, jaraco.classes, importlib-metadata, dulwich, cleo, cffi, build, requests-toolbelt, cryptography, cachecontrol, SecretStorage, keyring, poetry-plugin-export, poetry
#6 19.61 Successfully installed SecretStorage-3.5.0 build-1.6.1 cachecontrol-0.14.4 certifi-2026.10.23 cffi-2.1.1 charset_normalizer-3.5.2 cleo-2.1.0 crashtest-0.4.1 cryptography-50.0.2 distlib-0.4.4 dulwich-0.21.7 fastjsonschema-2.22.2 filelock-3.32.7 idna-3.20 importlib-metadata-9.1.0 installer-0.7.0 jaraco.classes-3.4.0 jeepney-0.9.0 keyring-24.3.1 more-itertools-11.2.1 msgpack-1.2.3 pexpect-4.9.0 pkginfo-1.13.3 platformdirs-4.13.5 poetry-1.8.5 poetry-core-1.9.1 poetry-plugin-export-1.8.0 ptyprocess-0.7.0 pycparser-3.12 pyproject-hooks-1.3.3 rapidfuzz-3.14.6 requests-2.34.2 requests-toolbelt-1.0.0 shellingham-1.5.4 tomlkit-0.15.2 trove-classifiers-2026.9.21.13 urllib3-2.8.0 virtualenv-20.39.1 zipp-4.1.2
#6 19.61 WARNING: Running pip as the 'root' user can result in broken permissions and conflicting behaviour with the system package manager. It is recommended to use a virtual environment instead: https://pip.pypa.io/warnings/venv
#6 DONE 20.1s

#7 [build 2/5] WORKDIR /build
#7 DONE 0.1s

#8 [build 3/5] COPY pyproject.toml poetry.lock README.md ./
#8 DONE 0.0s

#9 [build 4/5] COPY src/ src/
#9 DONE 0.0s

#10 [build 5/5] RUN   mkdir -p dist   && poetry export --without-hashes --format constraints.txt --output dist/constraints.txt   && pip wheel --no-cache-dir --isolated --requirement dist/constraints.txt --wheel-dir dist/vendor   && poetry build --format wheel
#10 0.672 Warning: poetry-plugin-export will not be installed by default in a future version of Poetry.
#10 0.672 In order to avoid a breaking change and make your automation forward-compatible, please install poetry-plugin-export explicitly. See https://python-poetry.org/docs/plugins/#using-plugins for details on how to install a plugin.
#10 0.672 To disable this warning run 'poetry config warnings.export false'.
#10 1.069 Ignoring colorama: markers 'python_version >= "3.11" and python_version < "4.0" and sys_platform == "win32"' don't match your environment
#10 2.273 Collecting aiohttp==3.8.5 (from -r dist/constraints.txt (line 1))
#10 2.671   Downloading aiohttp-3.8.5-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (7.7 kB)
#10 2.748 Collecting aiosignal==1.3.1 (from -r dist/constraints.txt (line 2))
#10 2.821   Downloading aiosignal-1.3.1-py3-none-any.whl.metadata (4.0 kB)
#10 2.917 Collecting async-timeout==4.0.3 (from -r dist/constraints.txt (line 3))
#10 2.998   Downloading async_timeout-4.0.3-py3-none-any.whl.metadata (4.2 kB)
#10 3.096 Collecting attrs==23.1.0 (from -r dist/constraints.txt (line 4))
#10 3.176   Downloading attrs-23.1.0-py3-none-any.whl.metadata (11 kB)
#10 3.371 Collecting charset-normalizer==3.2.0 (from -r dist/constraints.txt (line 5))
#10 3.446   Downloading charset_normalizer-3.2.0-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (31 kB)
#10 3.614 Collecting frozenlist==1.4.0 (from -r dist/constraints.txt (line 7))
#10 3.687   Downloading frozenlist-1.4.0-cp311-cp311-manylinux_2_5_x86_64.manylinux1_x86_64.manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (5.2 kB)
#10 3.766 Collecting idna==3.4 (from -r dist/constraints.txt (line 8))
#10 3.838   Downloading idna-3.4-py3-none-any.whl.metadata (9.8 kB)
#10 3.926 Collecting iniconfig==2.0.0 (from -r dist/constraints.txt (line 9))
#10 3.999   Downloading iniconfig-2.0.0-py3-none-any.whl.metadata (2.6 kB)
#10 4.332 Collecting multidict==6.0.4 (from -r dist/constraints.txt (line 10))
#10 4.403   Downloading multidict-6.0.4-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (4.1 kB)
#10 4.504 Collecting packaging==23.2 (from -r dist/constraints.txt (line 11))
#10 4.575   Downloading packaging-23.2-py3-none-any.whl.metadata (3.2 kB)
#10 4.664 Collecting pluggy==1.3.0 (from -r dist/constraints.txt (line 12))
#10 4.736   Downloading pluggy-1.3.0-py3-none-any.whl.metadata (4.3 kB)
#10 4.822 Collecting pytest-aiohttp==1.0.5 (from -r dist/constraints.txt (line 13))
#10 4.892   Downloading pytest_aiohttp-1.0.5-py3-none-any.whl.metadata (2.6 kB)
#10 4.990 Collecting pytest-asyncio==0.21.1 (from -r dist/constraints.txt (line 14))
#10 5.076   Downloading pytest_asyncio-0.21.1-py3-none-any.whl.metadata (4.0 kB)
#10 5.198 Collecting pytest==7.4.3 (from -r dist/constraints.txt (line 15))
#10 5.269   Downloading pytest-7.4.3-py3-none-any.whl.metadata (7.9 kB)
#10 5.609 Collecting yarl==1.9.2 (from -r dist/constraints.txt (line 16))
#10 5.685   Downloading yarl-1.9.2-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (23 kB)
#10 5.861 Downloading aiohttp-3.8.5-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (1.1 MB)
#10 6.184    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 1.1/1.1 MB 3.3 MB/s eta 0:00:00
#10 6.265 Downloading aiosignal-1.3.1-py3-none-any.whl (7.6 kB)
#10 6.342 Downloading async_timeout-4.0.3-py3-none-any.whl (5.7 kB)
#10 6.423 Downloading attrs-23.1.0-py3-none-any.whl (61 kB)
#10 6.428    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 61.2/61.2 kB 15.5 MB/s eta 0:00:00
#10 6.506 Downloading charset_normalizer-3.2.0-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (199 kB)
#10 6.514    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 199.6/199.6 kB 28.2 MB/s eta 0:00:00
#10 6.590 Downloading frozenlist-1.4.0-cp311-cp311-manylinux_2_5_x86_64.manylinux1_x86_64.manylinux_2_17_x86_64.manylinux2014_x86_64.whl (250 kB)
#10 6.601    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 250.5/250.5 kB 25.9 MB/s eta 0:00:00
#10 6.673 Downloading idna-3.4-py3-none-any.whl (61 kB)
#10 6.675    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 61.5/61.5 kB 304.0 MB/s eta 0:00:00
#10 6.746 Downloading iniconfig-2.0.0-py3-none-any.whl (5.9 kB)
#10 6.827 Downloading multidict-6.0.4-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (117 kB)
#10 6.836    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 117.4/117.4 kB 15.8 MB/s eta 0:00:00
#10 6.911 Downloading packaging-23.2-py3-none-any.whl (53 kB)
#10 6.919    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 53.0/53.0 kB 6.4 MB/s eta 0:00:00
#10 6.992 Downloading pluggy-1.3.0-py3-none-any.whl (18 kB)
#10 7.063 Downloading pytest_aiohttp-1.0.5-py3-none-any.whl (8.5 kB)
#10 7.139 Downloading pytest_asyncio-0.21.1-py3-none-any.whl (13 kB)
#10 7.224 Downloading pytest-7.4.3-py3-none-any.whl (325 kB)
#10 7.244    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 325.1/325.1 kB 16.5 MB/s eta 0:00:00
#10 7.348 Downloading yarl-1.9.2-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (282 kB)
#10 7.368    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 282.8/282.8 kB 15.1 MB/s eta 0:00:00
#10 7.379 Saved ./dist/vendor/aiohttp-3.8.5-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl
#10 7.379 Saved ./dist/vendor/aiosignal-1.3.1-py3-none-any.whl
#10 7.379 Saved ./dist/vendor/async_timeout-4.0.3-py3-none-any.whl
#10 7.379 Saved ./dist/vendor/attrs-23.1.0-py3-none-any.whl
#10 7.380 Saved ./dist/vendor/charset_normalizer-3.2.0-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl
#10 7.380 Saved ./dist/vendor/frozenlist-1.4.0-cp311-cp311-manylinux_2_5_x86_64.manylinux1_x86_64.manylinux_2_17_x86_64.manylinux2014_x86_64.whl
#10 7.380 Saved ./dist/vendor/idna-3.4-py3-none-any.whl
#10 7.381 Saved ./dist/vendor/iniconfig-2.0.0-py3-none-any.whl
#10 7.381 Saved ./dist/vendor/multidict-6.0.4-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl
#10 7.381 Saved ./dist/vendor/packaging-23.2-py3-none-any.whl
#10 7.381 Saved ./dist/vendor/pluggy-1.3.0-py3-none-any.whl
#10 7.382 Saved ./dist/vendor/pytest_aiohttp-1.0.5-py3-none-any.whl
#10 7.382 Saved ./dist/vendor/pytest_asyncio-0.21.1-py3-none-any.whl
#10 7.382 Saved ./dist/vendor/pytest-7.4.3-py3-none-any.whl
#10 7.383 Saved ./dist/vendor/yarl-1.9.2-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl
#10 7.987 
#10 7.987 [notice] A new release of pip is available: 24.0 -> 26.2.2
#10 7.987 [notice] To update, run: pip install --upgrade pip
#10 8.637 Creating virtualenv counter-backend-XDF0t07c-py3.11 in /root/.cache/pypoetry/virtualenvs
#10 8.970 Building counter-backend (0.1.0)
#10 8.973   - Building wheel
#10 8.979   - Built counter_backend-0.1.0-py3-none-any.whl
#10 DONE 9.1s

#11 [final 1/2] COPY --from=build /build/dist/ /tmp/dist/
#11 DONE 0.0s

#12 [final 2/2] RUN pip install --no-cache-dir --no-index --find-links /tmp/dist/vendor /tmp/dist/*.whl  && rm -rf /tmp/dist
#12 1.354 Looking in links: /tmp/dist/vendor
#12 1.363 Processing /tmp/dist/counter_backend-0.1.0-py3-none-any.whl
#12 1.373 Processing /tmp/dist/vendor/aiohttp-3.8.5-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (from counter-backend==0.1.0)
#12 1.380 Processing /tmp/dist/vendor/pytest_aiohttp-1.0.5-py3-none-any.whl (from counter-backend==0.1.0)
#12 1.385 Processing /tmp/dist/vendor/pytest_asyncio-0.21.1-py3-none-any.whl (from counter-backend==0.1.0)
#12 1.397 Processing /tmp/dist/vendor/attrs-23.1.0-py3-none-any.whl (from aiohttp<4.0.0,>=3.8.5->counter-backend==0.1.0)
#12 1.401 Processing /tmp/dist/vendor/charset_normalizer-3.2.0-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (from aiohttp<4.0.0,>=3.8.5->counter-backend==0.1.0)
#12 1.407 Processing /tmp/dist/vendor/multidict-6.0.4-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (from aiohttp<4.0.0,>=3.8.5->counter-backend==0.1.0)
#12 1.412 Processing /tmp/dist/vendor/async_timeout-4.0.3-py3-none-any.whl (from aiohttp<4.0.0,>=3.8.5->counter-backend==0.1.0)
#12 1.417 Processing /tmp/dist/vendor/yarl-1.9.2-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (from aiohttp<4.0.0,>=3.8.5->counter-backend==0.1.0)
#12 1.422 Processing /tmp/dist/vendor/frozenlist-1.4.0-cp311-cp311-manylinux_2_5_x86_64.manylinux1_x86_64.manylinux_2_17_x86_64.manylinux2014_x86_64.whl (from aiohttp<4.0.0,>=3.8.5->counter-backend==0.1.0)
#12 1.427 Processing /tmp/dist/vendor/aiosignal-1.3.1-py3-none-any.whl (from aiohttp<4.0.0,>=3.8.5->counter-backend==0.1.0)
#12 1.434 Processing /tmp/dist/vendor/pytest-7.4.3-py3-none-any.whl (from pytest-aiohttp<2.0.0,>=1.0.5->counter-backend==0.1.0)
#12 1.464 Processing /tmp/dist/vendor/iniconfig-2.0.0-py3-none-any.whl (from pytest>=6.1.0->pytest-aiohttp<2.0.0,>=1.0.5->counter-backend==0.1.0)
#12 1.465 Requirement already satisfied: packaging in /usr/local/lib/python3.11/site-packages (from pytest>=6.1.0->pytest-aiohttp<2.0.0,>=1.0.5->counter-backend==0.1.0) (26.3)
#12 1.469 Processing /tmp/dist/vendor/pluggy-1.3.0-py3-none-any.whl (from pytest>=6.1.0->pytest-aiohttp<2.0.0,>=1.0.5->counter-backend==0.1.0)
#12 1.476 Processing /tmp/dist/vendor/idna-3.4-py3-none-any.whl (from yarl<2.0,>=1.0->aiohttp<4.0.0,>=3.8.5->counter-backend==0.1.0)
#12 1.554 Installing collected packages: pluggy, multidict, iniconfig, idna, frozenlist, charset-normalizer, attrs, async-timeout, yarl, pytest, aiosignal, pytest-asyncio, aiohttp, pytest-aiohttp, counter-backend
#12 1.972 Successfully installed aiohttp-3.8.5 aiosignal-1.3.1 async-timeout-4.0.3 attrs-23.1.0 charset-normalizer-3.2.0 counter-backend-0.1.0 frozenlist-1.4.0 idna-3.4 iniconfig-2.0.0 multidict-6.0.4 pluggy-1.3.0 pytest-7.4.3 pytest-aiohttp-1.0.5 pytest-asyncio-0.21.1 yarl-1.9.2
#12 1.973 WARNING: Running pip as the 'root' user can result in broken permissions and conflicting behaviour with the system package manager. It is recommended to use a virtual environment instead: https://pip.pypa.io/warnings/venv
#12 DONE 2.1s

#13 exporting to image
#13 exporting layers
#13 exporting layers 0.7s done
#13 exporting manifest sha256:e10565ed4ef6785a02f29fc925de2983261fb22ae309f9b08b5f61dc201639f9 done
#13 exporting config sha256:6a28635c63a3e0a838b1862830d18168df4fc83387b37c8d382ce2e4c420fda5 done
#13 exporting attestation manifest sha256:37766f5ebf80a5fecb4128f7b85356a404ac0f3f57c12aa316e1a3ed7cf25559 done
#13 exporting manifest list sha256:488ddeb7eafdab0247f7defe21f3290ff007a071f949fce440a7c525d552dea1 done
#13 naming to docker.io/library/counter-backend:hw4-v1 done
#13 unpacking to docker.io/library/counter-backend:hw4-v1
#13 unpacking to docker.io/library/counter-backend:hw4-v1 0.2s done
#13 DONE 1.0s
```
