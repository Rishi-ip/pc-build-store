from django.db import models

# Create your models here.



class product(models.Model):
    pid=models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.CharField(max_length=200)
    image = models.ImageField(upload_to='products/')



    class Meta:
        db_table="product"



class customer(models.Model):
    emailId=models.CharField(max_length=200,primary_key=True)
    custname=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    contact_No=models.BigIntegerField()


    class Meta:
        db_table="customer"



class cart(models.Model):
    product_obj=models.ForeignKey(product,on_delete=models.CASCADE)
    cust_obj=models.ForeignKey(customer,on_delete=models.CASCADE)
    quantity=models.IntegerField()
    totalprice=models.FloatField(default=0.0)

    class Meta:
        db_table='cart'



class orders(models.Model):
    emailId=models.CharField(max_length=100)
    ordernumber=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    city=models.CharField(max_length=100)
    state=models.CharField(max_length=100)
    pincode=models.CharField(max_length=100)
    phoneno=models.BigIntegerField()
    totalbillamount=models.FloatField(default=0.0)



