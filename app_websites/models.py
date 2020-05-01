from django.db import models

class Machine(models.Model):
    machine = models.CharField(max_length=200, blank=True)
    model = models.ForeignKey('model', on_delete=models.CASCADE, null=True, blank=True)
    path = models.CharField(max_length=200, blank=True)
    year = models.IntegerField(default='1980', null=True, blank=True)
    desc = models.TextField(null=True, blank=True)
    small_image = models.ImageField(upload_to="images/machine", blank=True)

    def __str__(self):
        return self.machine + ' | ' + str(self.model) + ' | ' + str(self.year) + ' | ' + str(self.path)

    class Meta:
        ordering = ["year"]

class PartList(models.Model):						
    partlist = models.CharField(max_length=200, blank=True)
    machine = models.ManyToManyField(Machine)
    upload = models.FileField(upload_to='pdfs', blank=True) 

    def __str__(self):
        return  str(self.partlist)

class PartDiagram(models.Model):
    part_diagram = models.CharField(max_length=200, blank=True)
    image = models.ImageField(upload_to="images/part", blank=True)

    def __str__(self):
        return self.part_diagram

class Part(models.Model):
    part = models.CharField(max_length=200, blank=True)
    assembly = models.ForeignKey('assembly', on_delete=models.CASCADE, null=True, blank=True)
    part_diagram = models.ManyToManyField(PartDiagram, blank=True)  
    machine = models.ManyToManyField(Machine, blank=True)
    desc = models.CharField(max_length=200, blank=True)
    ref_no = models.IntegerField(blank=True)
    link = models.CharField(max_length=200, blank=True) 

    def __str__(self):
        return self.part + ' | ' + self.desc

class Assembly(models.Model):						
    assembly = models.CharField(max_length=200, blank=True)
    sort_order = models.IntegerField(default='0', blank=True) 

    def __str__(self):
        return  str(self.assembly)

class Model(models.Model):
    model = models.CharField(max_length=200)
    series = models.ForeignKey('series', on_delete=models.CASCADE, null=True, blank=True)
    path = models.CharField(max_length=200, default='series')
    short_desc = models.TextField(null=True, blank=True) 
    desc = models.TextField(null=True, blank=True)
    small_image = models.ImageField(upload_to="images/model", blank=True)
    header_image = models.ImageField(upload_to="images/model", blank=True) 
    sort_order = models.IntegerField(default='0', null=True, blank=True)

    def __str__(self):
        return str(self.series.brand) + ' | ' +  self.model
    
    class Meta:
        ordering = ["sort_order"]

class Series(models.Model):
    series = models.CharField(max_length=200)
    brand = models.ForeignKey('Brand', on_delete=models.CASCADE, null=True, blank=True)
    path = models.CharField(max_length=200, default='series')
    short_desc = models.TextField(null=True, blank=True) 
    desc = models.TextField(null=True, blank=True)
    small_image = models.ImageField(upload_to="images/series", blank=True)
    sort_order = models.IntegerField(default='0', null=True, blank=True)
    
    def __str__(self):
        return  str(self.brand) + ' | ' +  self.series
    
    class Meta:
        ordering = ["sort_order"]

class MachineType(models.Model):
    machine_type = models.CharField(max_length=200, default='')
    desc = models.CharField(max_length=200, default='', null=True, blank=True)
    sort_order = models.IntegerField(default='0', null=True, blank=True)
    
    def __str__(self):
        return self.machine_type

    class Meta:
        ordering = ['sort_order']
        
class Brand(models.Model):
    brand = models.CharField(max_length=200, default='')
    machine_type = models.ManyToManyField(MachineType)
    short_desc = models.TextField(null=True, blank=True)
    desc = models.TextField(null=True, blank=True)
    sort_order = models.IntegerField(default='0', null=True, blank=True)
    path = models.CharField(max_length=200, default='brand')
    small_image = models.ImageField(upload_to='media/images/brand', blank=True)
    
    def __str__(self):
        return self.brand

    class Meta:
        ordering = ['sort_order']



