from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Customer
from django.contrib.auth.models import User
from django.contrib.auth.models import Group


# @receiver(post_save, sender=User)
def customer_profile(sender, instance, created, **kwargs):
    if created:
        group = Group.objects.get(name="customer")
        instance.groups.add(group)
        Customer.objects.create(
            user=instance,

        )
        print("Customer Profile created! ")


post_save.connect(customer_profile, sender=User)

# @receiver(post_save, sender=User)
# def updated_profile(sender, instance, created, **kwargs):
#     if created == False:
#         instance.customer.save()
#         print("Profile updated !")
# # post_save.connect(updated_profile, sender=User)
