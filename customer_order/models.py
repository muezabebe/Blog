from django.db import models

class Order(models.Model):

    creation_date = models.DateTimeField(auto_now_add=True)
    customer_email = models.EmailField(max_length=255)
    customer_phone = models.IntegerField()
    product_category=models.CharField(max_length=50, null=True)
    product_name = models.CharField(max_length=100)
    product_quantity=models.IntegerField()




    def __str__(self):

        return f'(email: {self.customer_email}) (phone:{self.customer_phone}) (category: {self.product_category})(name:{self.product_name})(quantity:{self.product_quantity})'














