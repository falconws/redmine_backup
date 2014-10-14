#!/usr/bin/env python
# coding=utf-8

from fabric.api import task, run, get

@task
def get_data():
    """
    get redmine data
    """
    dump_file = "redmine.sql"
    attach_file = "/var/lib/redmine/default/files"
    pg_dump = "pg_dump -f %s -U redmine redmine" % dump_file
    run(pg_dump)
    get(dump_file)
    get(attach_file)
