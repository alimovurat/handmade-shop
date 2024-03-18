from django.db import models
from django.utils.translation import gettext_lazy as _


class Category(models.Model):

    name = models.CharField(max_length=50, verbose_name='Название')
    parent = models.ForeignKey(
        "self",
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        verbose_name='Родительская категория'
    )

    class Meta:
        verbose_name = _("категория")
        verbose_name_plural = _("категории")

    def __str__(self):
        return f'{self.name} | родитель - {self.parent}' if self.parent else self.name

    @classmethod
    def get_default_pk(cls):
        obj, created = cls.objects.get_or_create(name="Нет категории")
        return obj.pk


class Product(models.Model):

    category = models.ForeignKey(
        Category,
        on_delete=models.SET_DEFAULT,
        default=Category.get_default_pk,
        related_name='+',
        verbose_name='Категория'
    )
    image = models.ImageField(upload_to='product', null=True, verbose_name='Изображение')
    title = models.CharField(max_length=255, blank=False, verbose_name='Название')
    description = models.TextField(blank=True, verbose_name='Описание')
    price = models.IntegerField(blank=False, verbose_name='Цена')
    discount_price = models.IntegerField(blank=True, default=0, verbose_name='Цена со скидкой')
    count = models.IntegerField(default=1, verbose_name='Количество')
    genre = models.CharField(max_length=255, blank=True, verbose_name='Жанр')
    technique = models.CharField(max_length=255, blank=False, verbose_name='Техника')
    size = models.CharField(max_length=255, blank=False, null=True, verbose_name='Размер')
    material = models.CharField(max_length=255, blank=False, null=True, verbose_name='Материал')
    frame = models.BooleanField(null=True, blank=True, verbose_name='Подрамник')
    baguette = models.BooleanField(null=True, blank=True, verbose_name='Багет')
    passe_partout = models.BooleanField(null=True, blank=True, verbose_name='Паспарту')
    decor = models.CharField(max_length=255, blank=True, verbose_name='Оформление')
    creation_year = models.IntegerField(default=0, blank=True, verbose_name='Год создания')
    is_active = models.BooleanField(default=True, verbose_name='Активный')
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name='Дата создания'
    )
    updated_at = models.DateTimeField(
        auto_now=True, verbose_name='Дата обновления'
    )

    class Meta:
        verbose_name = _("продукт")
        verbose_name_plural = _("продукты")

    def __str__(self):
        return f'{self.title} ({self.price})'


class Customer(models.Model):

    name = models.CharField(max_length=200)

    class Meta:
        verbose_name = _("покупатель")
        verbose_name_plural = _("покупатели")

    def __str__(self):
        return self.name


class CustomerInformation(models.Model):

    name = models.CharField(max_length=255, blank=False)
    surname = models.CharField(max_length=255, blank=False)
    city = models.CharField(max_length=255, blank=False)
    street = models.CharField(max_length=255, blank=False)
    apartment = models.IntegerField(default=0, blank=False)
    phone = models.TextField(max_length=255, blank=False)
    email = models.CharField(max_length=255, blank=False)
    password = models.CharField(max_length=255, blank=False)
    confirm_password = models.CharField(max_length=255, blank=False)


class Delivery(models.Model):

    russia_curier_price = models.DecimalField(max_digits=7, decimal_places=2)
    nab_chelny_curier_price = models.DecimalField(max_digits=7, decimal_places=2)
    pickup = models.DecimalField(max_digits=7, decimal_places=2)

    class Meta:
        verbose_name = _("доставка")
        verbose_name_plural = _("доставки")

    def __str__(self):
        return f'{self.russia_curier_price}, {self.nab_chelny_curier_price}, {self.pickup}'


class Order(models.Model):

    class StatusChoices(models.TextChoices):
        NOT_PAID = 'not_paid', 'Не оплачено'
        PAID = 'paid', 'Оплачено'

    customer = models.ForeignKey(
        "main.Customer",
        on_delete=models.SET_NULL,
        null=True
    )
    status = models.CharField(
        max_length=10,
        default=StatusChoices.NOT_PAID,
        choices=StatusChoices.choices
    )
    created_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _("заказ")
        verbose_name_plural = _("заказы")

    def __str__(self):
        return f'{self.id} - {self.customer} ({self.get_status_display()})'


class OrderItems(models.Model):

    product = models.ForeignKey(
        "main.Product",
        on_delete=models.PROTECT,
        related_name='order_items'
    )
    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        # limit_choices_to={'status': 'not_paid'},
        related_name='items'
    )
    quantity = models.PositiveSmallIntegerField(default=1)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    created_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _("предмет заказа")
        verbose_name_plural = _("предметы заказа")
        unique_together = (('product', 'order'),)

    def __str__(self):
        return f'{self.order} - {self.product} {self.quantity}'