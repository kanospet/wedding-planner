from django.contrib import admin
from .models import Tutorial, TutorialSeries, TutorialCategory
from tinymce.widgets import TinyMCE
from django.db import models


# Register your models here.


class TutorialAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Title/date", {"fields": ["tutorial_title",
                                   "tutorial_published", ]}),
        ("ULR", {"fields": ["tutorial_slug", ]}),
        ("Series", {"fields": ["tutorial_series", ]}),
        ("Content", {"fields": ["tutorial_content"]})
    ]
    formfield_overrides = {
        models.TextField: {'widget': TinyMCE()},
    }


admin.site.register(Tutorial, TutorialAdmin)
admin.site.register(TutorialCategory)
admin.site.register(TutorialSeries)
