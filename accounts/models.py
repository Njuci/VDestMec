from django.contrib.auth.models import AbstractUser,BaseUserManager
from Vote.models import Faculte,promotion
import django.db


class ManagerEtudiant(BaseUserManager):
    def create_user(self,numMatricule,nom,post_nom,sexe,password=None,is_actif=True,is_staff=False,is_admin=False):
        if type(numMatricule)!=str:
            raise ValueError("caractères invalides")
        user_ob=self.model(numMatricule=numMatricule)
        user_ob.nom=nom
        user_ob.post_nom=post_nom
        user_ob.sexe=sexe
        user_ob.staff=is_staff
        user_ob.admin=is_admin
        user_ob.actif=is_actif        
        user_ob.set_password(password)
        user_ob.save(using=self._db)
        return user_ob
    def create_staffuser(self,numMatricule,nom,post_nom,sexe,password=None):
        user=self.create_user(numMatricule=numMatricule,nom=nom,post_nom=post_nom,password=password,sexe=sexe,is_staff=True)
        return user
    def create_superuser(self,numMatricule,nom,post_nom,sexe,password=None):
        superuser=self.create_user(numMatricule=numMatricule,nom=nom,post_nom=post_nom,sexe=sexe,password=password,is_staff=True,is_admin=True)
        return superuser
        

class Etudiant(AbstractUser):
    Sx=(
        ('m','masculin'),
        ('f','feminin'),
    )   
  
    nom=django.db.models.CharField(max_length=60)
    post_nom=django.db.models.CharField(max_length=60)
    prenom=django.db.models.CharField(max_length=60,null=True)
    sexe=django.db.models.CharField( max_length=9,choices=Sx)
    numMatricule=django.db.models.CharField(unique=True,max_length=26)
    #promotion=django.db.models.ForeignKey(promotion,on_delete=django.db.models.CASCADE)   
    actif=django.db.models.BooleanField(default=True)
    admin=django.db.models.BooleanField(default=False)
    staff=django.db.models.BooleanField(default=True)
    timestamp=django.db.models.DateTimeField(auto_now_add=True)
    USERNAME_FIELD='numMatricule'
    REQUIRED_FIELDS=['nom','post_nom','sexe']
    
    objects=ManagerEtudiant()
    @property
    def is_staff(self):
        return self.staff
    @property
    def is_active(self):
        return self.actif
    @property
    def is_admin(self):
        return self.admin
             
    class Meta:
        ordering=['nom']
class Profile(django.db.models.Model):
    Utilisateur=django.db.models.OneToOneField(Etudiant,on_delete=django.db.models.CASCADE)