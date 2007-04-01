from django.contrib import admin

from voiture.models import Reviews

# Register your models here.
class ReviewsAdmin(admin.ModelAdmin):
	list_display=('voiture', 'auteur', 'reviews')


admin.site.register(Reviews, ReviewsAdmin)