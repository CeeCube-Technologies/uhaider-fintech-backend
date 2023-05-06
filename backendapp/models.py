from django.db import models


class Status(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField()

    def __str__(self):
        return self.name


class Application(models.Model):
    # STATUS_CHOICES = [
    #     ('SD', 'Scraping Data'),
    #     ('NME', 'Needs Manual Entry'),
    #     ('RFR', 'Ready for Review'),
    #     ('ES', 'Error Scraping'),
    #     ('ET', 'Error Submitting'),
    #     ('SB', 'Submitted'),
    #     ('AP', 'Approved'),
    #     ('DN', 'Denied'),
    # ]
#d
    application_id = models.AutoField(primary_key=True)
    date_submitted = models.DateTimeField(auto_now_add=True)
    # status = models.CharField(choices=STATUS_CHOICES, max_length=3)
    status = models.ForeignKey(
        Status, on_delete=models.PROTECT, related_name='applications')
    name_of_business = models.CharField(max_length=255)
    status_date = models.DateField()
    legal_business_name = models.CharField(max_length=255)
    owners = models.TextField()
    users_cash_advance = models.BooleanField()
    have_cash_advance = models.BooleanField()
     
    dba = models.CharField(max_length=255, blank=True, null=True)
    address = models.CharField(max_length=255)
    suite = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    zip = models.CharField(max_length=10)
    phone = models.CharField(max_length=20)
    legal_entry = models.CharField(max_length=20)
    state_inc = models.CharField(max_length=20)
    federal_tax_id = models.CharField(max_length=20)
    date_business_started = models.DateTimeField(auto_now_add=True)
    mobile = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField()
    owner_first_name = models.CharField(max_length=255)
    owner_last_name = models.CharField(max_length=255)
    owner_home_address = models.CharField(max_length=255)
    owner_city = models.CharField(max_length=255)
    owner_state = models.CharField(max_length=255)
    owner_zip = models.CharField(max_length=10)
    owner_ssn = models.CharField(max_length=20)
    owner_percentage_of_ownership = models.CharField(max_length=20)
    owner_dob = models.DateField()
    owner_phone = models.CharField(max_length=20)
    federal_tax_id = models.CharField(max_length=20)
    state_of_inc = models.CharField(max_length=255)
    legal_entity = models.CharField(max_length=255)
    date_business_started = models.DateField()
    gross_monthly_sales = models.DecimalField(max_digits=10, decimal_places=2)
    type_of_product_sold = models.CharField(max_length=255)
    has_open_cash_advances = models.BooleanField(default=False)
    has_used_cash_advance_plan_before = models.BooleanField(default=False)
    using_money_for = models.CharField(max_length=255)
    bank_name = models.TextField()
    begin_bal_date = models.DateTimeField(auto_now_add=True)
    begin_bal_amount = models.TextField()
    description_of_business = models.TextField()
    length_of_ownership = models.CharField(max_length=255)
    years_at_location = models.CharField(max_length=255)
    credit_score = models.PositiveIntegerField()
    ending_bal_amount = models.TextField()
    ending_bal_date = models.DateTimeField(auto_now_add=True)
    total_deposit = models.TextField()
    business_name_match_flag = models.BooleanField()
    advanced_price = models.DecimalField(max_digits=10, decimal_places=2)
    commission_price = models.DecimalField(max_digits=10, decimal_places=2)
    
    pdf_Files = models.ManyToManyField(
        'ApplicationPDFs', blank=True, related_name='applications')

    def __str__(self):
        return f"{self.name_of_business} - {self.status}"


class ApplicationPDFs(models.Model):
    application = models.ForeignKey(
        Application, on_delete=models.CASCADE)
    file = models.FileField(upload_to='pdf_files/')
    pdf_type = models.CharField(max_length=255)
    business_name = models.CharField(max_length=255)
    beginning_balance_date = models.DateField()
    beginning_balance_amount = models.DecimalField(max_digits=10, decimal_places=2)
    total_deposit = models.DecimalField(max_digits=10, decimal_places=2)
    ending_balance_date = models.DateField()
    ending_balance_amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'{self.business_name} ({self.file.name})'
    
    
    
class PdfFiles(models.Model):
    application = models.ForeignKey(Application,related_name='pdf_files', on_delete= models.CASCADE)
    file = models.FileField(upload_to ='pdf_files/')
    unique_info = models.CharField(max_length=50)
    
    def __str__(self):
        return f'{self.unique_info} ({self.file.name})'
        
