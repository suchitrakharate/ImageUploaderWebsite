from django.contrib import admin

# Register your models here.
from testapp.models import Image
from testapp.models import Contact

# Register your models here.
# @admin.register(Image)
class ImageAdmin(admin.ModelAdmin):

    list_display=['id','photo','caption']
admin.site.register(Image,ImageAdmin)


# for contact page
admin.site.register(Contact)