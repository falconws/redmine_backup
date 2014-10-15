#!/usr/bin/env python
# coding=utf-8

from fabric.api import task, run, get, local

@task
def get_data():
    """
    get redmine data
    """
    dump_file = "redmine.sql"
    attach_file = "/var/lib/redmine/default/files"
    pg_dump = "pg_dump -f %s -U redmine redmine" % dump_file
    rdiff_dir = "/home/mint/rdiff_backup_dir"
    run(pg_dump)
    get(dump_file)
    get(attach_file)
    local("rdiff-backup /home/mint/backup %s" % rdiff_dir)
    local("rdiff-backup --remove-older-than 2W %s" % rdiff_dir)
