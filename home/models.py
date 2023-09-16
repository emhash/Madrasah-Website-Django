from django.db import models

class BasicInfo(models.Model):
    madrasa_name = models.CharField( max_length=250)
    email = models.EmailField(max_length=254)
    phone = models.IntegerField()
    address = models.CharField(max_length=250)
    eiin = models.IntegerField()
    fax = models.IntegerField()
    madrasa_code = models.IntegerField()


class ImportantLink1(models.Model):
    name_of_website = models.CharField( max_length=150)
    link_of_site = models.CharField( max_length=5000)
    
    def __str__(self):
        return self.name_of_website


class ImportantLink2(models.Model):
    name_of_website = models.CharField( max_length=150)
    link_of_site = models.CharField( max_length=5000)

    def __str__(self):
        return self.name_of_website

class AddClass(models.Model):
    class_name = models.CharField(max_length=100)

    def __str__(self):
        return self.class_name
    

class ExamResult(models.Model):
    select_class = models.ForeignKey(AddClass, on_delete=models.CASCADE, null=True, blank=True)
    title_of_notice = models.CharField( max_length=350)
    add_file = models.FileField(upload_to="ExamResult/", max_length=300, null=True, blank=True)


    def __str__(self):
        return self.title_of_notice


class Syllabus(models.Model):
    select_class = models.ForeignKey(AddClass, on_delete=models.CASCADE, null=True, blank=True)
    title_of_notice = models.CharField( max_length=350)
    add_file = models.FileField(upload_to="Syllabus/", max_length=300, null=True, blank=True)


    def __str__(self):
        return self.title_of_notice


class ClassRoutine(models.Model):
    select_class = models.ForeignKey(AddClass, on_delete=models.CASCADE, null=True, blank=True)
    title_of_notice = models.CharField( max_length=350)
    add_file = models.FileField(upload_to="ClassRoutine/", max_length=300, null=True, blank=True)


    def __str__(self):
        return self.title_of_notice


class Notice(models.Model):
    title_of_notice = models.CharField( max_length=350)
    add_file = models.FileField(upload_to="Notice/", max_length=300, null=True, blank=True)
    uploaded_at = models.DateField(auto_now=True)
    total_view = models.IntegerField(null=True, blank=True, default=0)


    def __str__(self):
        return self.title_of_notice

class Gallary(models.Model):
    title = models.CharField( max_length=250, null=True, blank=True)
    description = models.TextField()
    add_photo = models.ImageField(upload_to="Gallary/" )

    def __str__(self):
        return self.title
    

class Subject(models.Model):
    select_class = models.ForeignKey(AddClass, on_delete=models.CASCADE)
    subject_name = models.CharField( max_length=90)
    def __str__(self):
        return self.subject_name

class Teacher(models.Model):
    name = models.CharField( max_length=350)
    teacher_id = models.IntegerField(null=True, blank=True)
    mobile = models.IntegerField(null=True, blank=True)
    photo = models.ImageField( upload_to="Teacher/")
    present_address = models.CharField( max_length=350, null=True, blank=True)
    permanent_address = models.CharField( max_length=350, null=True, blank=True)
    rank = models.CharField( max_length=150)
    year_of_experience = models.IntegerField(null=True, blank=True)
    subject_teach = models.ForeignKey(Subject, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

# Add only two person - such as - VC and Pro VC, or Head master and Administration
class Lagacy(models.Model):
    rank_of_top_person = models.CharField( max_length=150)
    name_of_top_person = models.CharField(max_length=350 )
    person_speach = models.TextField(null=True, blank=True)
    photo = models.ImageField(upload_to="Lagacy/")
    email = models.EmailField( max_length=254, null=True, blank=True)
    mobile = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.name_of_top_person
    

class Employee(models.Model):
    name = models.CharField( max_length=250)
    e_id = models.IntegerField(null=True, blank=True)
    mobile = models.IntegerField(null=True, blank=True)
    photo = models.ImageField( upload_to="Teacher/")
    present_address = models.CharField( max_length=350, null=True, blank=True)
    permanent_address = models.CharField( max_length=350, null=True, blank=True)
    rank = models.CharField( max_length=150)
    

    def __str__(self):
        return self.name

class Slider(models.Model):
    photo_title = models.CharField(max_length=150)
    add_photo = models.ImageField( upload_to="slider/")
    details_of_photo = models.TextField()


    def __str__(self):
        return self.photo_title

