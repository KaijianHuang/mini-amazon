# Generated by Django 4.1.5 on 2023-04-24 00:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0009_warehouse_truck_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='warehouse',
            name='total',
            field=models.IntegerField(default=0),
        ),
        migrations.CreateModel(
            name='ShoppingCart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_num', models.IntegerField(default=1)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='shoppingcart', to=settings.AUTH_USER_MODEL)),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='shoppingcart', to='users.product')),
            ],
        ),
    ]