# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Comments(models.Model):
    id = models.AutoField(primary_key=True)
    comment = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'comments'


class Departments(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(unique=True, max_length=100)
    description = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'departments'


class Employees(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    role = models.ForeignKey('Roles', models.DO_NOTHING)
    department = models.ForeignKey(Departments, models.DO_NOTHING)
    experience_years = models.IntegerField(blank=True, null=True)
    contract_start_date = models.DateField(blank=True, null=True)
    contract_end_date = models.DateField(blank=True, null=True)
    location = models.CharField(max_length=100, blank=True, null=True)
    work_schedule = models.ForeignKey('Workschedules', models.DO_NOTHING, blank=True, null=True)
    created_at = models.DateTimeField()
    img = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'employees'


class Roles(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(unique=True, max_length=50)
    description = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'roles'


class Scores(models.Model):
    id = models.AutoField(primary_key=True)
    rating = models.CharField(max_length=9)
    score = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'scores'


class Userratings(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey('Users', models.DO_NOTHING, blank=True, null=True)
    employee = models.ForeignKey(Employees, models.DO_NOTHING, blank=True, null=True)
    rating = models.ForeignKey(Scores, models.DO_NOTHING, blank=True, null=True)
    comment = models.ForeignKey(Comments, models.DO_NOTHING, blank=True, null=True)
    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'userratings'


class Users(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(unique=True, max_length=50)
    email = models.CharField(unique=True, max_length=100)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'users'


class Workschedules(models.Model):
    id = models.AutoField(primary_key=True)
    schedule = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'workschedules'
