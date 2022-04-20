# Ansible SRE toolbox <!-- omit in toc -->

Ansible toolbox project for site reliability engineers.

- [How to run](#how-to-run)
- [Variables](#variables)
- [Playbooks](#playbooks)

## How to run

You need to create an inventory before. The available groups are:
- `all`, root group

```bash
ansible-galaxy install -r requirements.yml
ansible-playbook -i ${INVENTORY_FILEPATH} playbooks/${PLAYBOOK_FILENAME}
```

## Variables

## Playbooks
