from django.contrib import admin

# Register your models here.

from .models import Member, Task, Manager, Confirm, Remove, Bank, Order, DebitDecrease, DebitIncrease

admin.site.register(Member)
admin.site.register(Task)
admin.site.register(Manager)
admin.site.register(Confirm)
admin.site.register(Remove)
admin.site.register(Bank)
admin.site.register(Order)
admin.site.register(DebitDecrease)
admin.site.register(DebitIncrease)


