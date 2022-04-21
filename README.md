# Ansible SRE toolbox <!-- omit in toc -->

Ansible toolbox project for site reliability engineers.

- [How to run](#how-to-run)
- [Variables](#variables)
  - [`apt_sources`](#apt_sources)
  - [`bind9_bound_addresses`](#bind9_bound_addresses)
  - [`bind9_dns_forwarders`](#bind9_dns_forwarders)
  - [`bind9_recursion_allowed_networks`](#bind9_recursion_allowed_networks)
  - [`bind9_zones`](#bind9_zones)
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

### `bind9_bound_addresses`

List of addresses to bind on.

By default:
```yaml
bind9_bound_addresses: [any]
```

Example:
```yaml
bind9_bound_ips: [127.0.0.1]
```

### `bind9_dns_forwarders`

List of IPs of DNS forwarders.

By default:
```yaml
bind9_dns_forwarders: []
```

Example:
```yaml
dns_forwarders: [192.168.1.1]
```

### `bind9_recursion_allowed_networks`

List of networks recursion-allowed.

By default:
```yaml
bind9_recursion_allowed_networks: []
```

Example:
```yaml
bind9_recursion_allowed_networks: [192.168.1.1/24]
```

### `bind9_zones`

List of DNS zones.

By default:
```yaml
bind9_zones: []
```

Example:
```yaml
bind9_zones:
  - domain: home                                   # Domain name (required)
    master: pve-01                                 # Hostname of master server (required)
    soa: dns.home                                  # SOA (required)
    serial: 20220420                               # Serial (required)
    hostnames: [server-01]                         # List of hostnames (required)
    ttl: 1                                         # TTL (optional, 0 by default)
    admin_email: root@dns.home                     # Administrator email (optional, root + '@' + soa by default)
    refresh: 3600                                  # Refresh (optiona, 3600 by default)
    retry: 300                                     # Retry (optional, 300 by default)
    expire: 86400                                  # Expire (optional, 86400 by default)
    ns: dns.home                                   # NS (optional, soa by default)
    master_ip: 192.168.1.20                        # IP of master server (optional, default IPv4 by default)
    ip_hostvar_name: ansible_defaupt_ipv4.address  # Name of the hostvar variable that contains server IP (optiona, ansible_defaupt_ipv4.address by default)
```

## Playbooks

### 000-bootstrap

Target: `all`

Ensure servers are boostraped by ensuring:
- apt is configured
- bind9 is installed and configured (only on servers targeted as `master` in `bind9_zones`)
