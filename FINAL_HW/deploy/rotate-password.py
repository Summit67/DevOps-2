from pathlib import Path
import secrets
import subprocess
import sys
import yaml

vault = Path(__file__).parent / 'inventories/prom/group_vars/all/vault.yml'
key_file = sys.argv[1]
result = subprocess.run(
    ['ansible-vault', 'view', '--vault-password-file', key_file, str(vault)],
    check=True, capture_output=True, text=True,
)
values = yaml.safe_load(result.stdout)
values['vault_audit_password'] = secrets.token_hex(24)
subprocess.run(
    ['ansible-vault', 'encrypt', '--vault-password-file', key_file,
     '--output', str(vault)],
    input=yaml.safe_dump(values), text=True, check=True,
)
print('Updated encrypted vault_audit_password')
