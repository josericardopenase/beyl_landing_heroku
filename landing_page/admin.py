from django.contrib import admin
from .models  import Plan, PlanInclude, PlanFeature, TeamMember, Feature, Faq, Emails


class PlanIncludeInline(admin.TabularInline):
    model = PlanInclude
    extra = 0


class PlanAdmin(admin.ModelAdmin):
    inlines = [PlanIncludeInline,]

class EmailAdmin(admin.ModelAdmin):
    list_display = ('email', 'name', 'social_media', 'rssc', 'has_used_other_tool')
admin.site.register( Plan , PlanAdmin )
admin.site.register(PlanFeature)
admin.site.register(TeamMember)
admin.site.register(Feature)
admin.site.register(Faq)
admin.site.register(Emails, EmailAdmin)
