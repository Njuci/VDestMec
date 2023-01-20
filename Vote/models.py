from django.db import models


class Faculte(models.Model):
    codeFac=models.CharField(max_length=10,unique=True)
    denomination_extact=models.TextField()
    #LogoFac=models.ImageField(null=True)
    #les designers vont juger cette affaire de photo    
    class Meta:
        ordering=['codeFac']
        
    def __str__(self):
        return self.codeFac


class promotion(models.Model):    
    faclte=models.ForeignKey(Faculte,null=False,on_delete=models.CASCADE)
    #on pourrai utiliser TextChoise mais FoeignKey est adapté dans notre cas ici    
    codePromotion=models.CharField(max_length=15,unique=True)
    denomination_exact_Promo=models.TextField()
    class Meta:
        ordering=['codePromotion']
        
    def __str__(self):
        return self.codePromotion
    def getFac(self):
        return self.faclte.get__str__()