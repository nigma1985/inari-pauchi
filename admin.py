from django import forms
from django.contrib import admin
from django.db.models.aggregates import Sum
from django.urls import reverse
from django.utils.http import urlencode
from django.utils.html import format_html
from .models import Alternative, Initial, Subsequent, His, Her

admin.site.site_header = "Administration"

# Register your models here.
# admin.site.register(Initial)

class SubsequentInline(admin.TabularInline):
    model = Subsequent

    list_per_page = 25
    fieldsets = (
        (None, {
            'fields': ('your_char','your_integer','your_initial','your_creation', 'your_update'),
            'classes': ('extrapretty',),
        }),
    )
    readonly_fields = ('your_creation', 'your_update')
    extra = 0

@admin.register(Initial)
class InitialSite(admin.ModelAdmin):
    search_fields = ('my_char',)
    list_filter = ('my_char', 'my_truth')
    list_per_page = 25
    inlines = [
        SubsequentInline,
    ]
    fieldsets = (
        (None, {
            'fields': ('my_char',),
            'classes': ('wide', 'extrapretty',),
            'description': 'This section is mandatory'
        }),
        ('Optional', {
            'classes': ('collapse',),
            'fields': ('my_truth', ('my_integer', 'my_decimal') ),
            'description': 'You may skip these - however, it is recommended to complete the form'
        }),
    )
    def show_money(self, obj):
        from django.utils.html import format_html
        if obj.my_decimal:
            number = '{:,.2f}'.format(obj.my_decimal)
            if obj.my_decimal < 0:
                return format_html('<div style="text-align:right;color:red">{} €</div>', number)
            else: 
                return format_html('<div style="text-align:right">{} €</div>', number)
        else: 
            return format_html('<div style="text-align:right"></div>', )
    show_money.short_description = 'Money'
    
    def show_counter(self, obj):
        from django.utils.html import format_html
        if obj.my_integer:
            number = '{:,.0f}'.format(obj.my_integer)
            if obj.my_integer < 0:
                return format_html('<div style="text-align:right;color:red">{}</div>', number)
            else: 
                return format_html('<div style="text-align:right">{}</div>', number)
        else: 
            return format_html('<div style="text-align:right"></div>', )
    show_counter.short_description = 'Counter'

    def show_average(self, obj):
        from django.db.models import Avg
        from django.utils.html import format_html

        result = Subsequent.objects.filter(your_initial=obj).aggregate(Avg('your_integer'))
        if result['your_integer__avg']:
            number = '{:,.2f}'.format(result['your_integer__avg'])
            if result['your_integer__avg'] < 0:
                return format_html('<div style="text-align:right;color:red">{}</div>', number)
            else: 
                return format_html('<div style="text-align:right">{}</div>', number)
        else: 
            return format_html('<div style="text-align:right"></div>', )
    show_average.short_description = 'Average INT'

    def show_sum_alternative(self, obj):
        from django.db.models import Sum
        from django.utils.html import format_html

        result = Alternative.objects.filter(alt_initial=obj).aggregate(Sum('alt_decimal'))
        if result['alt_decimal__sum']:
            number = '{:,.2f}'.format(result['alt_decimal__sum'])
            if result['alt_decimal__sum'] < 0:
                return format_html('<div style="text-align:right;color:red">{}</div>', number)
            else: 
                return format_html('<div style="text-align:right">{}</div>', number)
        else: 
            return format_html('<div style="text-align:right"></div>', )
    show_sum_alternative.short_description = 'Sum Money'

    def show_average_her(self, obj):
        from django.db.models import Avg
        from django.utils.html import format_html
        
        result = Her.objects.filter(alt_initial=obj).aggregate(Avg('her_integer'))
        if result['her_integer__avg']:
            number = '{:,.2f}'.format(result['her_integer__avg'])
            if result['her_integer__avg'] < 0:
                return format_html('<div style="text-align:right;color:red">{}</div>', number)
            else: 
                return format_html('<div style="text-align:right">{}</div>', number)
        else: 
            return format_html('<div style="text-align:right"></div>', )
    show_average_her.short_description = 'Avg Her'

    def show_average_his(self, obj):
        from django.db.models import Avg
        from django.utils.html import format_html
        
        result = His.objects.filter(alt_initial=obj).aggregate(Avg('his_integer'))
        if result['his_integer__avg']:
            number = '{:,.2f}'.format(result['his_integer__avg'])
            if result['his_integer__avg'] < 0:
                return format_html('<div style="text-align:right;color:red">{}</div>', number)
            else: 
                return format_html('<div style="text-align:right">{}</div>', number)
        else: 
            return format_html('<div style="text-align:right"></div>', )
    show_average_his.short_description = 'Avg His'

    def show_diff_average(self, obj):
        from django.db.models import Avg
        from django.utils.html import format_html
        
        his_result = His.objects.filter(alt_initial=obj).aggregate(Avg('his_integer'))
        her_result = Her.objects.filter(alt_initial=obj).aggregate(Avg('her_integer'))
        
        if his_result['his_integer__avg'] or her_result['her_integer__avg']:
            his_number = his_result['his_integer__avg'] if his_result['his_integer__avg'] else 0
            her_number = her_result['her_integer__avg'] if her_result['her_integer__avg'] else 0
            number = '{:,.2f}'.format(his_number - her_number)
            if his_number - her_number < 0:
                return format_html('<div style="text-align:right;color:red">{}</div>', number)
            else: 
                return format_html('<div style="text-align:right">{}</div>', number)
        else: 
            return format_html('<div style="text-align:right"></div>', )
    show_diff_average.short_description = 'Avg Diff'

    def view_her_link(self, obj):
        count = Her.objects.filter(alt_initial=obj).count()
        if count > 0:
            url = (
                reverse("admin:mylearning_her_changelist")
                + "?"
                + urlencode({"alt_initial__id": f"{obj.id}"})
            )
            return format_html('<div style="text-align:right"><a href="{}">{} hers</a></div>', url, count)
        else:
            return format_html('<div style="text-align:right"></div>', )
    view_her_link.short_description = 'Cnt Her'

    def view_his_link(self, obj):
        count = His.objects.filter(alt_initial=obj).count()
        if count > 0:
            url = (
                reverse("admin:mylearning_his_changelist")
                + "?"
                + urlencode({"alt_initial__id": f"{obj.id}"})
            )
            return format_html('<div style="text-align:right"><a href="{}">{} hiss</a></div>', url, count)
        else:
            return format_html('<div style="text-align:right"></div>', )
    view_his_link.short_description = 'Cnt His'

    list_display = ('__str__', 
        'show_counter', 'show_money', 
        'show_average', 
        'show_sum_alternative', 
        # 'show_average_his', 'show_average_her', 
        'view_his_link', 'view_her_link',
        'show_diff_average', 'my_truth')

###########################################################
###########################################################
###########################################################

@admin.register(Subsequent)
class SubsequentSite(admin.ModelAdmin):
    list_filter = ('your_char', 'your_initial')
    list_per_page = 25
    fieldsets = (
        (None, {
            'fields': ('your_char','your_integer'),
            'classes': ('wide', 'extrapretty',),
            'description': 'This section is mandatory'
        }),
        ('Optional', {
            'classes': ('collapse',),
            'fields': ('your_initial',),
            'description': 'You may skip these - however, it is recommended to complete the form'
        }),
    )
    def show_integer(self, obj):
        from django.utils.html import format_html
        if obj.your_integer:
            number = '{:,.0f}'.format(obj.your_integer)
            if obj.your_integer < 0:
                return format_html('<div style="text-align:right;color:red">{}</div>', number)
            else: 
                return format_html('<div style="text-align:right">{}</div>', number)
        else: 
            return format_html('<div style="text-align:right"></div>', )
    show_integer.short_description = "INT"

    list_display = ('__str__', 'your_initial', 'show_integer', 'your_creation', 'your_update')

@admin.register(His)
class HisSite(admin.ModelAdmin):
    list_filter = ('alt_initial',)
    list_per_page = 10
    list_editable = ('alt_initial', )
    # save_on_top = True
    fieldsets = (
        (None, {
            'fields': (('alt_char', 'his_char'), ('alt_initial', 'alt_decimal'),),
            'classes': ('wide', 'extrapretty',),
            'description': 'This section is mandatory'
        }),
        ('Optional', {
            'classes': ('collapse',),
            'fields': ('his_integer', ),
            'description': 'You may skip these - however, it is recommended to complete the form'
        }),
    )
    def show_integer(self, obj):
        from django.utils.html import format_html
        if obj.his_integer:
            number = '{:,.0f}'.format(obj.his_integer)
            if obj.his_integer < 0:
                return format_html('<div style="text-align:right;color:red">{}</div>', number)
            else: 
                return format_html('<div style="text-align:right">{}</div>', number)
        else: 
            return format_html('<div style="text-align:right"></div>', )
    show_integer.short_description = "INT"

    def show_money(self, obj):
        from django.utils.html import format_html
        if obj.alt_decimal:
            number = '{:,.2f}'.format(obj.alt_decimal)
            if obj.alt_decimal < 0:
                return format_html('<div style="text-align:right;color:red">{} €</div>', number)
            else: 
                return format_html('<div style="text-align:right">{} €</div>', number)
        else: 
            return format_html('<div style="text-align:right"></div>', )
    show_money.short_description = 'Money'

    list_display = ('__str__', 'alt_initial', 'show_money', 'show_integer', 'alt_creation', 'alt_update')


class HerAdminForm(forms.ModelForm):
    class Meta:
        model = Her
        fields = "__all__"

    def clean_her_char(self):
        if self.cleaned_data["her_char"][0] == "Z":
            raise forms.ValidationError("There are no Z-ts")
        return self.cleaned_data["her_char"]
    def clean_alt_decimal(self):
        if self.cleaned_data["alt_decimal"] > 10**6 or self.cleaned_data["alt_decimal"] < 10**6 * -1:
            raise forms.ValidationError("Don't stretch it")
        return self.cleaned_data["alt_decimal"]

@admin.register(Her)
class HerSite(admin.ModelAdmin):
    list_filter = ('alt_initial',)
    list_per_page = 10
    form = HerAdminForm
    fieldsets = (
        (None, {
            'fields': (('alt_char', 'her_char'), 'alt_initial', 'alt_decimal',),
            'classes': ('wide', 'extrapretty',),
            'description': 'This section is mandatory'
        }),
        ('Optional', {
            'classes': ('collapse',),
            'fields': ('her_integer', ),
            'description': 'You may skip these - however, it is recommended to complete the form'
        }),
    )
    def show_integer(self, obj):
        from django.utils.html import format_html
        if obj.her_integer:
            number = '{:,.0f}'.format(obj.her_integer)
            if obj.her_integer < 0:
                return format_html('<div style="text-align:right;color:red">{}</div>', number)
            else: 
                return format_html('<div style="text-align:right">{}</div>', number)
        else: 
            return format_html('<div style="text-align:right"></div>', )
    show_integer.short_description = "INT"

    def show_money(self, obj):
        from django.utils.html import format_html
        if obj.alt_decimal:
            number = '{:,.2f}'.format(obj.alt_decimal)
            if obj.alt_decimal < 0:
                return format_html('<div style="text-align:right;color:red">{} €</div>', number)
            else: 
                return format_html('<div style="text-align:right">{} €</div>', number)
        else: 
            return format_html('<div style="text-align:right"></div>', )
    show_money.short_description = 'Money'

    def view_her_history(self, obj):
        url = (
            reverse("admin:mylearning_her_history", args=(obj.id,))
        )
        return format_html('<div style="text-align:center"><a href="{}">history</a></div>', url)
    view_her_history.short_description = 'History'

    list_display = ('__str__', 'alt_initial', 'show_money', 'show_integer', 'alt_creation', 'alt_update', 'view_her_history')

# Register your models here.
class MyAdminSite(admin.AdminSite):
    site_header = 'Special Administration: MyLearning'

admin_site = MyAdminSite(name='MyLearning')
admin_site.register(Initial)


    
    