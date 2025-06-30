from django.db import models

class Projects(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    created_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='created_by')
    created_at = models.DateTimeField(auto_now_add=True)  # Automatically set on creation
    updated_at = models.DateTimeField(auto_now=True) 

    class Meta:
        managed = False
        db_table = 'projects'


class Roles(models.Model):
    name = models.CharField(unique=True, max_length=8)

    class Meta:
        managed = False
        db_table = 'roles'


class Tasks(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField(blank=True, null=True)
    due_date = models.DateField(blank=True, null=True)
    priority = models.CharField(max_length=6, blank=True, null=True)
    status = models.CharField(max_length=11, blank=True, null=True)
    project = models.ForeignKey(Projects, models.DO_NOTHING)
    created_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='created_by')
    closed_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='closed_by', related_name='tasks_closed_by_set', blank=True, null=True)
    created_at = models.DateTimeField(auto_now=True)
    closed_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tasks'


class Users(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.CharField(unique=True, max_length=255)
    password_hash = models.CharField(max_length=255)
    role = models.ForeignKey(Roles, models.DO_NOTHING)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users'
