from django.db import models
from django.contrib.auth.models import User


class Member(User):
    credit = models.IntegerField()
    debit = models.IntegerField()
    # Skill to be done
    skill = models.CharField(max_length=100)
    pic = models.ImageField(upload_to='photos', default=None)
    is_verified = models.BooleanField(default=False)

    def __str__(self):
        return self.user_name


class Task(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=20, default=None)
    description = models.TextField()
    owner = models.ForeignKey(Member, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Manager(Member):
    pass


class Confirm(models.Model):
    # verifier = models.ForeignKey(Manager)
    verified_member = models.ForeignKey(Member)
    date = models.DateField('confirm date')


class Remove(models.Model):
    # manager = models.ForeignKey(Manager)
    removed_member = models.ForeignKey(Member)
    date = models.DateField('remove date')


class Bank(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    logo = models.ImageField('photos', default=None)
    gate = models.URLField()


class Order(models.Model):
    id = models.AutoField(primary_key=True)
    task = models.ForeignKey(Task)
    employee = models.ForeignKey(Member)
    deadline = models.DateField('deadline date')
    state = models.IntegerField()


class DebitDecrease(models.Model):
    bank = models.ForeignKey(Bank)
    member = models.ForeignKey(Member)
    id = models.AutoField(primary_key=True)
    amount = models.IntegerField()


class DebitIncrease(models.Model):
    bank = models.ForeignKey(Bank)
    member = models.ForeignKey(Member)
    id = models.AutoField(primary_key=True)
    amount = models.IntegerField()
