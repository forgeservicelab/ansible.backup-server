Backup Server
=============

Ansible playbook to set up a replication/backup server against FORGE ServiceLab drupal environment.

Prerequisites
-------------

- The target machine(s) have to be already instantiated, this playbook does not launch computing instances

### The inventory file
The inventory file defines three mandatory groups, `mysql-master`, `nfs-master` and `slaves`; each of this groups must include all related servers in the environment (this applies especially if MySQL and NFS are HA clusters). See the `inventory.tpl` file.

Playbook Variables
------------------

- `nfs_host` - The service IP or FQDN that represents the NFS HA cluster.
- `master_host` - The service IP or FQDN that represents the MySQL HA cluster.
- `master_user` - A user with administrative rights and local access to the MySQL servers.
- `master_password` - The password for the user above.
- `replication_user` - The name of the mysql user for replication.
- `replication_password` - The password for the replication user.
- `databases` - A **List** of the databases to replicate and backup.
