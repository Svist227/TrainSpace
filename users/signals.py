from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from Chuvash_Workout.models import MyUsers

# User = get_user_model()
# @receiver(post_save, sender=User)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         instance.add = MyUsers.objects.create(user=instance)
#     instance.add.save()
# # @receiver(post_save, sender=User)
# # def save_billing_profile(sender, instance, **kwargs):
# #   instance.add.save()