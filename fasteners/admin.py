from django.contrib import admin

from .models import Screws, DIN931, DIN933, Size933, DIN931, Size931, DIN6921, Size6921, DIN912, Size912, DIN7981, ISO14583, DIN7500D

admin.site.register(Screws)


# -------------------------------------------------- DIN933-------------------------------
class Size933Inline(admin.StackedInline):
    model = Size933
    extra = 3



class DIN933Admin(admin.ModelAdmin):
    list_display = ('thread_length', 'material', 'finish')

    fieldsets = [
        ('',               {'fields': ['thread_length']}),
        ('Properties', {'fields': ['material', 'finish']}),
    ]
    inlines = [Size933Inline]

admin.site.register(DIN933, DIN933Admin)


class Size933Admin(admin.ModelAdmin):
    list_display = ('size', 'code')

admin.site.register(Size933, Size933Admin)


# -------------------------------------------------- DIN931-------------------------------
class Size931Inline(admin.StackedInline):
    model = Size931
    extra = 3

class DIN931Admin(admin.ModelAdmin):
    list_display = ('thread_length', 'material', 'finish')

    fieldsets = [
        ('',               {'fields': ['thread_length']}),
        ('Properties', {'fields': ['material', 'finish']}),
    ]
    inlines = [Size931Inline]

admin.site.register(DIN931, DIN931Admin)

class Size931Admin(admin.ModelAdmin):
    list_display = ('size', 'code')

admin.site.register(Size931, Size931Admin)

# -------------------------------------------------- DIN6921-------------------------------
class Size6921Inline(admin.StackedInline):
    model = Size6921
    extra = 3

class DIN6921Admin(admin.ModelAdmin):
    list_display = ('thread_length', 'material', 'finish')

    fieldsets = [
        ('',               {'fields': ['thread_length']}),
        ('Properties', {'fields': ['material', 'finish']}),
    ]
    inlines = [Size6921Inline]

admin.site.register(DIN6921, DIN6921Admin)

class Size6921Admin(admin.ModelAdmin):
    list_display = ('size', 'code')

admin.site.register(Size6921, Size6921Admin)

# -------------------------------------------------- DIN912-------------------------------
class Size912Inline(admin.StackedInline):
    model = Size912
    extra = 3

class DIN912Admin(admin.ModelAdmin):
    list_display = ('thread_length', 'material', 'finish')

    fieldsets = [
        ('',               {'fields': ['thread_length']}),
        ('Properties', {'fields': ['material', 'finish']}),
    ]
    inlines = [Size912Inline]

admin.site.register(DIN912, DIN912Admin)

class Size912Admin(admin.ModelAdmin):
    list_display = ('size', 'code')

admin.site.register(Size912, Size912Admin)

# -------------------------------------------------- DIN7981 -------------------------------
class DIN7981Admin(admin.ModelAdmin):
    list_display = ('screw_length', 'st35', 'st42', 'st48', 'st55', 'st63')

admin.site.register(DIN7981, DIN7981Admin)

# -------------------------------------------------- ISO14583 -------------------------------
class ISO14583Admin(admin.ModelAdmin):
    list_display = ('screw_length', 'st2_9', 'st3_5', 'st4_2', 'st4_8', 'st5_5', 'st6_3')

admin.site.register(ISO14583, ISO14583Admin)

# -------------------------------------------------- DIN7500D -------------------------------
class DIN7500DAdmin(admin.ModelAdmin):
    list_display = ('screw_length', 'm8', 'm10', 'm12')

admin.site.register(DIN7500D, DIN7500DAdmin)
