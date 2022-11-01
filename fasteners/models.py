from django.db import models


# --- Model Screws
class Screws(models.Model):
    name = models.CharField(max_length=96)
    standard = models.CharField(max_length=32)

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = "Screw"
        verbose_name_plural = "Screws"

# --- Model DIN933
class DIN933(models.Model):
    '''
    Hexagon head cap screws, also called hex bolts or hex head cap screws, are threaded fasteners with a six-sided head. 
    They are installed with a wrench or a socket. Compared to other fasteners, hex head cap screws provide a larger surface-bearing area for better clamping. 
    Hex bolts are well-suited for OEM applications, construction projects, infrastructure, and other uses that require tight tolerances.

    '''
    thread_length = models.IntegerField()
    material = models.DecimalField(max_digits=2, decimal_places=1, default="8.8")
    finish = models.CharField(max_length=24, default="Plain Steel")

    def __str__(self):
        return str(self.thread_length)

    class Meta:
        verbose_name = "Full Thread DIN 933"
        verbose_name_plural = "DIN 933 Full Thread"
        ordering = ['thread_length']

class Size933(models.Model):
    '''
    Hexagon head cap Size
    '''
    din933 = models.ForeignKey(DIN933, on_delete=models.CASCADE)
    size = models.CharField(max_length=6, default="M")
    code = models.CharField(max_length=12, unique=True)

    def __str__(self):
        return self.size

    class Meta:
        verbose_name = "DIN 933 Size"
        verbose_name_plural = "DIN 933 Size"


# --- Model DIN931
class DIN931(models.Model):
    ''''''
    thread_length = models.IntegerField()
    material = models.DecimalField(max_digits=2, decimal_places=1, default="8.8")
    finish = models.CharField(max_length=24, default="Plain Steel")

    def __str__(self):
        return str(self.thread_length)

    class Meta:
        verbose_name = "Partly Thread DIN 931"
        verbose_name_plural = "DIN 931 Partly Thread"
        ordering = ['thread_length']


class Size931(models.Model):
    '''
    Hexagon head cap Size
    '''
    din931 = models.ForeignKey(DIN931, on_delete=models.CASCADE)
    size = models.CharField(max_length=6, default="M")
    code = models.CharField(max_length=12, unique=True)

    def __str__(self):
        return self.size

    class Meta:
        verbose_name = "DIN 931 Size"
        verbose_name_plural = "DIN 931 Size"


# --- Model DIN6921
class DIN6921(models.Model):
    '''Hexagon Head Screws, With Flange'''
    thread_length = models.IntegerField()
    material = models.DecimalField(max_digits=2, decimal_places=1, default="8.8")
    finish = models.CharField(max_length=24, default="Plain Steel")

    def __str__(self):
        return str(self.thread_length)

    class Meta:
        verbose_name = "Hexagon Head Screws, With Flange DIN 6921"
        verbose_name_plural = "DIN 6921 Partly Thread"
        ordering = ['thread_length']


class Size6921(models.Model):
    '''
    Hexagon Head Screws, With Flange Size
    '''
    din6921 = models.ForeignKey(DIN6921, on_delete=models.CASCADE)
    size = models.CharField(max_length=6, default="M")
    code = models.CharField(max_length=12, unique=True)

    def __str__(self):
        return self.size

    class Meta:
        verbose_name = "DIN 6921 Size"
        verbose_name_plural = "DIN 6921 Size"

# --- Model DIN912
class DIN912(models.Model):
    '''Hexagon Head Screws, With Flange'''
    thread_length = models.IntegerField()
    material = models.DecimalField(max_digits=2, decimal_places=1, default="8.8")
    finish = models.CharField(max_length=24, default="Plain Steel")

    def __str__(self):
        return str(self.thread_length)

    class Meta:
        verbose_name = "Hexagon Socked Head Cap Screws DIN 912"
        verbose_name_plural = "DIN  912"
        ordering = ['thread_length']


class Size912(models.Model):
    '''
    Hexagon Head Screws, With Flange Size
    '''
    din912 = models.ForeignKey(DIN912, on_delete=models.CASCADE)
    size = models.CharField(max_length=6, default="M")
    code = models.CharField(max_length=12, unique=True)

    def __str__(self):
        return self.size

    class Meta:
        verbose_name = "DIN 912 Size"
        verbose_name_plural = "DIN 912 Size"

# --- Model DIN7981C
class DIN7981(models.Model):
    screw_length = models.CharField(max_length=7, unique=True)
    st35 = models.CharField(max_length=7, default='-')
    st42 = models.CharField(max_length=7, default='-')
    st48 = models.CharField(max_length=7, default='-')
    st55 = models.CharField(max_length=7, default='-')
    st63 = models.CharField(max_length=7, default='-')

    def __str__(self):
        return str(self.screw_length)
    
    class Meta:
        verbose_name = "DIN 7981C"
        verbose_name_plural = "DIN 7981C"
        ordering = ['screw_length']

# --- Model ISO14583
class ISO14583(models.Model):
    screw_length = models.CharField(max_length=7, unique=True)
    st2_9 = models.CharField('ST2.9', max_length=7, default='-')
    st3_5 = models.CharField('ST3.5', max_length=7, default='-')
    st4_2 = models.CharField('ST4.2', max_length=7, default='-')
    st4_8 = models.CharField('ST4.8', max_length=7, default='-')
    st5_5 = models.CharField('ST5.5', max_length=7, default='-')
    st6_3 = models.CharField('ST6.3', max_length=7, default='-')

    def __str__(self):
        return str(self.screw_length)
    
    class Meta:
        verbose_name = "ISO 14583"
        verbose_name_plural = "ISO 14583"

# --- Model DIN7500D
class  DIN7500D(models.Model):
    screw_length = models.CharField(max_length=7, unique=True)
    m8 = models.CharField('M8', max_length=7, default='-')
    m10 = models.CharField('M10', max_length=7, default='-')
    m12 = models.CharField('M12', max_length=7, default='-')

    def __str__(self):
        return str(self.screw_length)
    
    class Meta:
        verbose_name = " DIN7500D"
        verbose_name_plural = " DIN7500D"
        ordering = ['screw_length']
        