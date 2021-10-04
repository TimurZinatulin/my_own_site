from django.contrib import admin
from .models import *
from django.forms import ModelChoiceField


class MouseAdmin(admin.ModelAdmin):

	def formfield_for_foreignkey(self, db_field, request, **kwargs):
		if db_field.name == 'category':
			return ModelChoiceField(Category.objects.filter(slug='mouses'))
		super().formfield_for_foreignkey(db_field, request, **kwargs)


class KeyboardAdmin(admin.ModelAdmin):

	def formfield_for_foreignkey(self, db_field, request, **kwargs):
		if db_field.name == 'category':
			return ModelChoiceField(Category.objects.filter(slug='keyboards'))
		super().formfield_for_foreignkey(db_field, request, **kwargs)


admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Cart)
admin.site.register(Mouse, MouseAdmin)
admin.site.register(Keyboard, KeyboardAdmin)
admin.site.register(Review)