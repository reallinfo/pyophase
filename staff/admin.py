from django.contrib import admin
from django.template import loader
from django.template.response import SimpleTemplateResponse

import staff.models
import ophasebase.models


class TutorFilter(admin.SimpleListFilter):
    title = "Tutorenstatus"
    parameter_name = "tutorstatus"

    def lookups(self, request, model_admin):
        choices = [('onlytutors', 'Alle Tutoren')]
        for gc in ophasebase.models.GroupCategory.objects.all():
            choices.append((gc.id, gc.label))
        choices.append(('notutors', 'Keine Tutoren'))
        return choices

    def queryset(self, request, queryset):
        if self.value() is None:
            return queryset
        if self.value() == 'onlytutors':
            return queryset.filter(is_tutor=True)
        if self.value() == 'notutors':
            return queryset.filter(is_tutor=False)
        return queryset.filter(tutor_for__id=self.value())


class PersonAdmin(admin.ModelAdmin):
    list_display = ['prename', 'name', 'is_tutor', 'is_orga', 'is_helper', 'created_at']
    list_filter = [TutorFilter, 'is_orga', 'is_helper']
    list_display_links = ['prename', 'name']
    search_fields = ['prename', 'name']
    readonly_fields = ('created_at', 'updated_at')
    actions = ['mail_export']

    fieldsets = [
        ('Stammdaten', {'fields':
            ['ophase', 'prename', 'name', 'email', 'phone', 'dress_size', 'remarks']}),
        ('Bewerbung', {'fields':
            ['matriculated_since', 'degree_course', 'experience_ophase', 'why_participate']}),
        ('In der Ophase', {'fields':
            ['is_tutor', 'tutor_for', 'is_orga', 'orga_jobs', 'is_helper', 'helper_jobs']}),
        ('Sonstiges', {'fields': ['created_at', 'updated_at']}),
    ]

    filter_horizontal = ('orga_jobs', 'helper_jobs')

    def mail_export(self, request, queryset):
        template = loader.get_template("staff/mail_export.html")
        context = {'persons' : queryset}
        return SimpleTemplateResponse(template, context)
    mail_export.short_description = "E-Mail Mass Subscription Export"


class SettingsAdmin(admin.ModelAdmin):
    list_display = ['tutor_registration_enabled', 'orga_registration_enabled', 'helper_registration_enabled']
    list_display_links = ['tutor_registration_enabled', 'orga_registration_enabled', 'helper_registration_enabled']


admin.site.register(staff.models.Person, PersonAdmin)
admin.site.register(staff.models.DressSize)
admin.site.register(staff.models.Settings, SettingsAdmin)
