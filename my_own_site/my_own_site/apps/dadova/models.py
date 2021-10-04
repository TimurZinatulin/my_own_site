from django.db import models


class Category(models.Model):

	name = models.CharField('Имя категории', max_length=255)
	slug = models.SlugField(unique=True)

	def __str__(self):
		return self.name

	class Meta:
		verbose_name_plural = 'Categories'


class Product(models.Model):

	category = models.ForeignKey(Category, on_delete=models.CASCADE)

	title = models.CharField('Название продукта', max_length=255)
	price = models.CharField('Цена продукта', max_length=255)
	img = models.ImageField('Изображение')
	description = models.TextField('Описание')

	def __str__(self):
		return self.title


class Cart(models.Model):

	products = models.ManyToManyField(Product, blank=True)


class Mouse(Product):

	dpi = models.CharField('DPI', max_length=255)
	max_click_amount = models.CharField('Максимальное число кликов', max_length=255)
	material = models.CharField('Материал изготовления', max_length=255)

	def __str__(self):
		return self.title


class Keyboard(Product):

	rgb = models.BooleanField(default=True)
	max_push_amount = models.CharField('Максимальное число нажатий', max_length=255)
	material = models.CharField('Материал изготовления', max_length=255)

	def __str__(self):
		return self.title


class Review(models.Model):

	product = models.ForeignKey(Product, on_delete=models.CASCADE)

	text = models.TextField('Текст отзыва')