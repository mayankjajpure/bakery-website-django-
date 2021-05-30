from django.db import models

class catogary(models.Model):
    title=models.CharField(max_length=50)
    description=models.TextField()

    def __str__(self):
        return self.title
    

class images(models.Model):
    title=models.CharField(max_length=50)
    description=models.TextField()

    image=models.ImageField(upload_to="media")
    date=models.DateField()
    cat=models.ForeignKey(catogary,on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    


class order(models.Model):
    name=models.TextField()
    cat=models.TextField()
    itemcode=models.TextField()
    city=models.TextField()
    state=models.TextField()
    zipcode=models.TextField()


    def __str__(self):
        return self.name

    