#!/bin/bash

set -e

function check_arg {
  if [ -z ${1} ]; then
    >&2 echo "Usage: ${script_name} <vmid> <name> <image url>"
    exit 2
  fi
}

dir=/var/lib/vz/images
storage=local-lvm

script_name=${0}
vm_id=${1}
name="${2}"
url=${3}

if [ ${USER} != "root" ]; then
  >&2 echo "You need root privileges to execute this script"
  exit 1
fi

check_arg ${vm_id}
check_arg "${name}"
check_arg ${url}

filename="${name}.img"
filepath="${dir}/${filename}"

if [ -f "${filepath}" ]; then
  echo "Skipping download of image because ${filepath} exists"
else
  echo "Downloading ${url} to ${filepath}..."
  curl -fL ${url} > ${filepath}
  echo "${filepath} downloaded"
fi

qm create ${vm_id} --name "${name}" --memory 2048 --net0 virtio,bridge=vmbr0
qm importdisk ${vm_id} "${filepath}" ${storage}
qm set ${vm_id} --scsihw virtio-scsi-pci --scsi0 ${storage}:vm-${vm_id}-disk-0
qm set ${vm_id} --ide2 ${storage}:cloudinit
qm set ${vm_id} --boot c --bootdisk scsi0
qm set ${vm_id} --serial0 socket --vga serial0
qm template ${vm_id}
echo "Template '${name}' (${vm_id}) created"
