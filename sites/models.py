from django.db import models
class Category(models.Model):
    name= models.CharField(max_length=120)

    def __str__(self):
        return self.name

class Auteur(models.Model):
    name=models.CharField(max_length=120)

    def __str__(self):
        return self.name
    
class Livre(models.Model):
    title=models.CharField(max_length=50)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    auteur=models.ForeignKey(Auteur,on_delete=models.CASCADE)
    desc=models.TextField()
    image=models.ImageField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)


    def __str__(self) :
        return self.title


class Article(models.Model):
    title=models.CharField(max_length=50)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    desc=models.TextField()
    image=models.ImageField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    
    def __str__(self) :
        return self.title



