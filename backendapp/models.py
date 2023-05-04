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
    credit_score = models.PositiveIntegerField()
    business_name_match_flag = models.BooleanField()
    advanced_price = models.DecimalField(max_digits=10, decimal_places=2)
    commission_price = models.DecimalField(max_digits=10, decimal_places=2)
    pdf_files = models.ManyToManyField(
        'ApplicationPDFs', blank=True, related_name='applications')

    def __str__(self):
        return f"{self.name_of_business} - {self.status}"


class ApplicationPDFs(models.Model):
    application = models.ForeignKey(
        Application, on_delete=models.CASCADE)
    file = models.FileField(upload_to='pdf_files/')
    unique_info = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.file.name} ({self.unique_info})'
