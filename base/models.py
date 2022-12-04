from django.db import models

class Profile(models.Model):
  SEX_CHOICE = (
  (1, "Male"),
  (2, "Female")
)
  # FIRST NAME AND LAST NAME HAS BEEN FILLED BY DJANGO ABSTRACTUSER CLASS

  nin = models.BigIntegerField(unique=True)
  surname = models.CharField(max_length=100)
  first_name = models.CharField(max_length=100)
  middle_name = models.CharField(max_length=30)
  
  # MAILING ADDRESS
  lga = models.ForeignKey("LGA", on_delete=models.CASCADE, related_name="mailing_lga")
  city = models.CharField(max_length=100)
  tel = models.BigIntegerField()
  email = models.EmailField(unique=True)
  
  # PERSONAL INFORMATION
  sex = models.IntegerField(choices=SEX_CHOICE)
  date_of_birth = models.DateField()
  place_of_birth = models.CharField(max_length=200)
  lga_of_origin = models.ForeignKey("LGA", on_delete=models.CASCADE, related_name="lga_of_origin")
  certificate_of_origin = models.ImageField(upload_to='certificates_of_origin')
  signature = models.ImageField(upload_to='signatures')
  
  # ACADEMIC RECORD
  secondary_school = models.CharField(max_length=250)
  graduation_year = models.IntegerField()
  current_institution = models.CharField(max_length=100)
  year_of_admission = models.IntegerField()
  id_card = models.ImageField(upload_to='id_cards')
  course_of_study = models.CharField(max_length=100)
  present_level = models.IntegerField()
  gpa = models.FloatField()
  transcript = models.ImageField(upload_to='transcripts', null=True, blank=True)
  
  # FANMILY BACKGROUND
  mother_name = models.CharField(max_length=100, null=True, blank=True)
  mother_address = models.CharField(max_length=250, null=True, blank=True)
  mother_occupation = models.CharField(max_length=50, null=True, blank=True)
  mother_tel = models.BigIntegerField(null=True, blank=True)
  
  father_name = models.CharField(max_length=100, null=True, blank=True)
  father_address = models.CharField(max_length=250, null=True, blank=True)
  father_occupation = models.CharField(max_length=50, null=True, blank=True)
  father_tel = models.BigIntegerField(null=True, blank=True)
  
  guardian_name = models.CharField(max_length=100, null=True, blank=True)
  guardian_address = models.CharField(max_length=250, null=True, blank=True)
  guardian_occupation = models.CharField(max_length=50, null=True, blank=True)
  guardian_tel = models.BigIntegerField(null=True, blank=True)
  
  # HOD 
  attestation_letter = models.ImageField('attestation_letters')
  
  # STUDENT ATTESTATION
  attestation = models.BooleanField(default=False)
  
  def __str__(self):
    return f'{self.first_name} - {self.surname}'
  
  class Meta:
    ordering = ['surname']
  
class LGA(models.Model):
  name = models.CharField(max_length=100)
  
  def __str__(self):
    return self.name
  
  class Meta:
    ordering = ['name']