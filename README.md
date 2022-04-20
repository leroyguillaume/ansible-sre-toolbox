# Ansible SRE toolbox <!-- omit in toc -->

Ansible toolbox project for site reliability engineers.

- [How to run](#how-to-run)
- [Variables](#variables)
  - [`apt_sources`](#apt_sources)
- [Playbooks](#playbooks)
  - [000-bootstrap](#000-bootstrap)

## How to run

You need to create an inventory before. The available groups are:
- `all`, root group

```bash
ansible-galaxy install -r requirements.yml
ansible-playbook -i ${INVENTORY_FILEPATH} playbooks/${PLAYBOOK_FILENAME}
```

## Variables

### `apt_sources`

List of APT sources.

By default:
```yaml
apt_sources: []
```

Example:
```yaml
apt_sources:
  filename: pve.list  # Filename (required)
  state: present      # State (optional, present|absent, present by default)
  repos:              # List of repositories (optional, empty list by default)
    - deb http://download.proxmox.com/debian/pve bullseye pve-no-subscription
    - deb http://security.debian.org/debian-security bullseye-security main contrib
```

## Playbooks

### 000-bootstrap

Target: `all`

Ensure servers are boostraped by ensuring:
- apt is configured
