from django.db import models

# Create your models here.
class Category(models.Model):
    class Meta:
        abstract = True

    name = models.CharField(max_length=40)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, related_name='subs', related_query_name='subs', unique=False)

    def sub_categories(self):
        return self.__class__.objects.filter(parent=self)
    
    def parent_category(self):
        return self.__class__.objects.get(id=self.parent.id)
        


class ClothesCategory(Category):
    pass

class Product(models.Model):
    name = models.CharField(max_length=40)
    category = models.OneToOneField(ClothesCategory, on_delete=models.CASCADE, unique=False)


