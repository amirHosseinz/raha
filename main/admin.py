from django.contrib import admin

# Register your models here.

from .models import Member, Task, Manager, Confirm, Remove, Bank, Order, debit_decrease, debit_increase

admin.site.register(Member)
admin.site.register(Task)
admin.site.register(Manager)
admin.site.register(Confirm)
admin.site.register(Remove)
admin.site.register(Bank)
admin.site.register(Order)
admin.site.register(debit_decrease)
admin.site.register(debit_increase)


