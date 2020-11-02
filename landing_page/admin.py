from django.contrib import admin
from .models  import Plan, PlanInclude, PlanFeature, TeamMember, Feature


class PlanIncludeInline(admin.TabularInline):
    model = PlanInclude
    extra = 0


class PlanAdmin(admin.ModelAdmin):
    inlines = [PlanIncludeInline,]

admin.site.register( Plan , PlanAdmin )
admin.site.register(PlanFeature)
admin.site.register(TeamMember)
admin.site.register(Feature)