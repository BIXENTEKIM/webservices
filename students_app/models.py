from django.db import models

class Receipting(models.Model):
    TransactionType =models.CharField(max_length=20,null=False,blank=False)
    TransId =models.CharField(max_length=20,null=False,blank=False,unique=True)
    TransTime =models.CharField(max_length=50,null=False,blank=False)
    TransAmount =models.DecimalField(max_digits=10, decimal_places=2)
    BusinessShortCode =models.CharField(max_length=20,null=False,blank=False)
    BillRefNo =models.CharField(max_length=20,null=False,blank=False,unique=False)
    InvoiceNo =models.CharField(max_length=20,null=True,blank=True)
    OrgAccountBalance = models.CharField(max_length=50, null=True, blank=True)
    ThirdPartyTransID = models.CharField(max_length=20, null=True, blank=True)
    MSISDN = models.CharField(max_length=500, null=False, blank=False)
    FirstName = models.CharField(max_length=50, null=False, blank=False)
    MiddleName = models.CharField(max_length=50, null=True, blank=True)
    LastName = models.CharField(max_length=50, null=True, blank=True)

