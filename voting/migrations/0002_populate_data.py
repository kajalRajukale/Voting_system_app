from django.db import migrations


def create_symbols(apps, schema_editor):
    Symbol = apps.get_model('voting', 'Symbol')
    symbols = [
        ('Star', 'symbols/star.svg'),
        ('Book', 'symbols/book.svg'),
        ('Pen', 'symbols/pen.svg'),
        ('Pencil', 'symbols/pencil.svg'),
        ('Flower', 'symbols/flower.svg'),
        ('Tree', 'symbols/tree.svg'),
        ('Cycle', 'symbols/cycle.svg'),
        ('Car', 'symbols/car.svg'),
        ('Apple', 'symbols/apple.svg'),
        ('Fish', 'symbols/fish.svg'),
        ('Moon', 'symbols/moon.svg'),
        ('Sun', 'symbols/sun.svg'),
        ('House', 'symbols/house.svg'),
        ('Heart', 'symbols/heart.svg'),
        ('Bell', 'symbols/bell.svg'),
        ('Butterfly', 'symbols/butterfly.svg'),
        ('Bird', 'symbols/bird.svg'),
        ('Umbrella', 'symbols/umbrella.svg'),
        ('Ball', 'symbols/ball.svg'),
        ('Candle', 'symbols/candle.svg'),
    ]
    for name, image in symbols:
        Symbol.objects.get_or_create(name=name, defaults={'image': image})


def create_machine_state(apps, schema_editor):
    MachineState = apps.get_model('voting', 'MachineState')
    MachineState.objects.get_or_create(pk=1, defaults={'is_locked': False, 'total_students': 800})


def remove_data(apps, schema_editor):
    apps.get_model('voting', 'Symbol').objects.all().delete()
    apps.get_model('voting', 'MachineState').objects.all().delete()


class Migration(migrations.Migration):

    dependencies = [
        ('voting', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_symbols, remove_data),
        migrations.RunPython(create_machine_state, remove_data),
    ]
