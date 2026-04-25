class SrijanProfile(BaseClass):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    srijan_id = models.BigIntegerField(unique=True, null=True, blank=True)
    srijan_key = models.CharField(max_length=64, default=uuid.uuid4, editable=False)
#    srijan_key = models.CharField(max_length=64, unique=True)

    first_name = models.CharField(max_length=255)
    middle_name = models.CharField(max_length=255, blank=True)
    last_name = models.CharField(max_length=255)

    dob = models.DateField(null=True, blank=True)
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=255, unique=True)

    mobile = models.CharField(max_length=15)
    gender = models.CharField(max_length=10)
    address = models.TextField(max_length=512)

    locale = models.CharField(max_length=10)
    url = models.URLField(blank=True)

    account_type = models.CharField(max_length=50)

    last_login = models.DateTimeField(auto_now=True)

    profile_pic = models.ImageField(upload_to="profiles/", blank=True, null=True)

    class Meta:
       db_table = "main_srijanprofile"

    def save(self, *args, **kwargs):
        if not self.srijan_id:
            # एक यूनिक 10 अंकों की ID जेनरेट करना (आप अपने हिसाब से बदल सकते हैं)
            self.srijan_id = random.randint(1000000000, 9999999999)
            
            # यह सुनिश्चित करने के लिए कि ID वाकई यूनिक है
            while SrijanProfile.objects.filter(srijan_id=self.srijan_id).exists():
                self.srijan_id = random.randint(1000000000, 9999999999)
        
        super(SrijanProfile, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.first_name} {self.last_name}  "
