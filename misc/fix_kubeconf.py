import os
import sys

import yaml


def read_kube_config(file):
    with open(file) as f:
        return yaml.load(f, Loader=yaml.Loader)


def upsert_config(configs, entry_type, entry, prefix):

    new_name = f"{prefix}-{entry_type}" if entry_type != "context" else prefix

    updated = False
    for c in configs:
        if c["name"] == new_name:
            c[entry_type] = entry
            updated = True
            break

    if not updated:
        configs.append({"name": new_name, entry_type: entry})

    return new_name


def new_kube_config(prefix, remote_config):
    # this is a kubeconfig file from a freshly installed environment, which
    # only contains the default cluster and default users
    remote = read_kube_config(remote_config)
    remote_cluster = remote["clusters"][0]["cluster"]
    remote_user = remote["users"][0]["user"]

    current = read_kube_config(os.path.expanduser("~/.kube/config"))
    new_cluster = upsert_config(current["clusters"], "cluster", remote_cluster, prefix)
    new_user = upsert_config(current["users"], "user", remote_user, prefix)
    upsert_config(
        current["contexts"],
        "context",
        {"cluster": new_cluster, "user": new_user},
        prefix,
    )

    print(yaml.dump(current, default_flow_style=False))


if __name__ == "__main__":
    prefix = sys.argv[2] if len(sys.argv) > 2 else "pie"
    if len(sys.argv) > 1:
        new_kube_config(prefix, sys.argv[1])
    else:
        print("please specifcy remote kubeconfig file")
