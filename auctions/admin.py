from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, ListingModel, BidModel, CommentModel

# Register your models here.
admin.site.register(User, UserAdmin)
admin.site.register(ListingModel)
admin.site.register(BidModel)
admin.site.register(CommentModel)
