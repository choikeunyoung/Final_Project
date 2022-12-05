
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('articles', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shipping_price', models.IntegerField()),
                ('total_price', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('order_status', models.CharField(default='결제완료', max_length=250)),
                ('contact_number', models.CharField(max_length=250, null=True)),
                ('delivery_option', models.CharField(choices=[('부재시 문 앞에 놓아주세요.', '부재시 문앞에 놓아주세요.'), ('부재시 경비실에 맡겨주세요.', '부재시 경비실에 맡겨주세요.'), ('부재시 전화 또는 문자주세요.', '부재시 전화 또는 문자 주세요.'), ('택배함에 넣어주세요.', '택배함에 넣어주세요.'), ('파손위험이 있는 상품입니다. 배송 시 주의해주세요.', '파손위험이 있는 상품입니다. 배송 시 주의해주세요.'), ('배송 전에 연락주세요.', '배송 전에 연락주세요.')], max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('address', models.CharField(max_length=250)),
                ('zip_code', models.CharField(max_length=20)),
                ('city', models.CharField(max_length=20)),
                ('art', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='articles.art')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='CartItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('art', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='articles.art')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '장바구니',
                'verbose_name_plural': '장바구니 목록',
                'ordering': ['-pk'],
            },
        ),
    ]