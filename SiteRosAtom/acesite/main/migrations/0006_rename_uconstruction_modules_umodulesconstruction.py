

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_products'),
    ]

    operations = [
        migrations.RenameField(
            model_name='modules',
            old_name='uConstruction',
            new_name='uModulesConstruction',
        ),
    ]
