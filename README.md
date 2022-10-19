ansible_linux_python3
=========

Проверяет наличие интерпретатора Python3 и устанавливает его при необходимости.
При использовании явного указания интерпритатора в ansible.cfg на сервере без установленного интерпретатора Python3 возниикает следующая ошибка при сборе фактов

```sh
TASK [Gathering Facts] *********************************************************
fatal: [centos7]: FAILED! => {"ansible_facts": {}, "changed": false, "failed_modules": {"ansible.legacy.setup": {"failed": true, "module_stderr": "Shared connection to 127.0.0.1 closed.\r\n", "module_stdout": "/bin/sh: /usr/bin/python3: Нет такого файла или каталога\r\n", "msg": "MODULE FAILURE\nSee stdout/stderr for the exact error", "rc": 127}}, "msg": "The following modules failed to execute: ansible.legacy.setup\n"}

PLAY RECAP *********************************************************************
centos7                    : ok=0    changed=0    unreachable=0    failed=1    skipped=0    rescued=0    ignored=0  
```

gather_facts: false в купе с ролью позволяет купировать эту проблему если необходимо явно указывать интерпретатор

```yaml
- hosts: all
  become: true
  gather_facts: false

  roles:
    - { role: ansible_linux_python3 }
```

Role Variables
--------------

В виду того что попытка собрать факты при отсутствии интерпретатора Python3 приводит к ошибке playbook должен содержать gather_facts: false
В роли по уполчанию предусмотрен сбор фактов после установки python3
linux_python3_setup_fact: true

Example Playbook
----------------

```yaml
- hosts: all
  gather_facts: false
  become: true
  vars:
    linux_python3_setup_fact: false
  roles:
    - { role: ansible_linux_python3 }
```

License
-------

Apache 2.0

Author Information
------------------

- [habr](https://habr.com/ru/users/mmblsp/)
- mmblspace@yandex.ru
