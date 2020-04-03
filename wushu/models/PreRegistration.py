from django.db import models
from wushu.models.City import City
from wushu.models.Country import Country
from wushu.models.SportClubUser import SportClubUser
from wushu.models.Coach import Coach
from wushu.models.ClubRole import ClubRole



class PreRegistration(models.Model):
    MALE = 'Erkek'
    FEMALE = 'Kadın'

    AB1 = 'AB Rh+'
    AB2 = 'AB Rh-'
    A1 = 'A Rh+'
    A2 = 'A Rh-'
    B1 = 'B Rh+'
    B2 = 'B Rh-'
    O1 = 'AB Rh+'
    O2 = 'AB Rh+'

    GENDER_CHOICES = (
        (MALE, 'Erkek'),
        (FEMALE, 'Kadın'),
    )

    BLOODTYPE = (
        (AB1, 'AB Rh+'),
        (AB2, 'AB Rh-'),
        (A1, 'A Rh+'),
        (A2, 'A Rh-'),
        (B1, 'B Rh+'),
        (B2, 'B Rh-'),
        (O1, '0 Rh+'),
        (O2, '0 Rh-'),

    )
    WAITED = 'Beklemede'
    APPROVED = 'Onaylandı'
    PROPOUND = 'Onaya Gönderildi'
    DENIED = 'Reddedildi'

    STATUS_CHOICES = (
        (APPROVED, 'Onaylandı'),
        (PROPOUND, 'Onaya Gönderildi'),
        (DENIED, 'Reddedildi'),
        (WAITED, 'Beklemede'),
    )
    status = models.CharField(max_length=128, verbose_name='Onay Durumu', choices=STATUS_CHOICES, default=WAITED)

    # person form
    tc = models.CharField(max_length=120, null=True, blank=True)
    height = models.CharField(max_length=120, null=True, blank=True)
    weight = models.CharField(max_length=120, null=True, blank=True)
    birthplace = models.CharField(max_length=120, null=True, blank=True,verbose_name='Doğum Yeri')
    motherName = models.CharField(max_length=120, null=True, blank=True,verbose_name='Anne Adı')
    fatherName = models.CharField(max_length=120, null=True, blank=True,verbose_name='Baba Adı')
    profileImage = models.ImageField(upload_to='profile/', null=True, blank=True, default='profile/user.png',verbose_name='Profil Resmi')
    birthDate = models.DateField(null=True, blank=True, verbose_name='Doğum Tarihi')
    bloodType = models.CharField(max_length=128, verbose_name='Kan Grubu', choices=BLOODTYPE, default=AB1)
    gender = models.CharField(max_length=128, verbose_name='Cinsiyeti', choices=GENDER_CHOICES, default=MALE)
    # communicationform
    postalCode = models.CharField(max_length=120, null=True, blank=True)
    phoneNumber = models.CharField(max_length=120, null=True, blank=True)
    phoneNumber2 = models.CharField(max_length=120, null=True, blank=True)
    address = models.TextField(blank=True, null=True, verbose_name='Adres')
    city = models.ForeignKey(City, on_delete=models.CASCADE, verbose_name='İl')
    country = models.ForeignKey(Country, on_delete=models.CASCADE, verbose_name='Ülke')

    # sportClup
    name = models.CharField(blank=True, null=True, max_length=120)
    shortName = models.CharField(blank=True, null=True, max_length=120)
    foundingDate = models.DateField(blank=True, null=True, max_length=120,verbose_name='Kuruluş Tarihi')
    clubMail = models.CharField(blank=True, null=True, max_length=120)
    logo = models.ImageField(upload_to='club/', null=True, blank=True, verbose_name='Kulüp Logo')

    creationDate = models.DateTimeField(auto_now_add=True)
    modificationDate = models.DateTimeField(auto_now=True)
    isFormal = models.BooleanField(default=False)

    clubpostalCode = models.CharField(max_length=120, null=True, blank=True)
    clubphoneNumber = models.CharField(max_length=120, null=True, blank=True)
    clubphoneNumber2 = models.CharField(max_length=120, null=True, blank=True)
    clubaddress = models.TextField(blank=True, null=True, verbose_name='Adres')
    clubcity = models.ForeignKey(City, on_delete=models.CASCADE, verbose_name='İl')
    clubcountry = models.ForeignKey(Country, on_delete=models.CASCADE, verbose_name='Ülke')


     #userForm
    first_name = models.CharField( max_length=30, blank=True)
    last_name = models.CharField( max_length=150, blank=True)
    email = models.EmailField( max_length=254,blank=True)
    is_staff = models.BooleanField(default=False, help_text=('Designates whether the user can log into this admin site.'))
    is_active = models.BooleanField(default=False,help_text=('Designates whether this user should be treated as active. '))

    # gerekli evraklar
    dekont = models.FileField(upload_to='dekont/', null=False, blank=False, verbose_name='Dekont ')
    petition= models.FileField(upload_to='dekont/', null=True, blank=True, verbose_name='Dilekçe ')
    # Sportclup user
    role = models.ForeignKey(ClubRole, on_delete=models.CASCADE, verbose_name='Üye Rolü')


    class Meta:
        default_permissions = ()

