from django.db import migrations


def assign_symbols(apps, schema_editor):
    Candidate = apps.get_model('voting', 'Candidate')
    
    # Mapping: candidate name -> symbol SVG path
    symbol_map = {
        'Riddhi Gaikwad': 'symbols/surya.svg',
        'Aryan Takbhate': 'symbols/diva.svg',
        'Swara Malekar': 'symbols/chandra.svg',
        'Janhvi Vasave': 'symbols/chatri.svg',
        'Riya Raut': 'symbols/tara.svg',
        'Prabhat Pandey': 'symbols/daftar.svg',
        'Adarsh Sasane': 'symbols/phool.svg',
        'Gayatri Chate': 'symbols/amba.svg',
        'Om Suryavanshi': 'symbols/om.svg',
        'Aarti Pathade': 'symbols/tv.svg',
        'Altamash Sheikh': 'symbols/kathi.svg',
        'Sharvari Mane': 'symbols/duster.svg',
        'Swaraj Gore': 'symbols/pencil.svg',
        'Aryan Mhaske': 'symbols/topi.svg',
        'Shrividya Yeldi': 'symbols/pen.svg',
        'Aryan Panchal': 'symbols/chavi.svg',
        'Spandan Bilmar': 'symbols/ghadayal.svg',
        'Viraj Chavan': 'symbols/cricket_bat.svg',
        'Rajvir Ankush': 'symbols/pustake.svg',
        'Ganesh Nandure': 'symbols/badminton.svg',
        'Bhakti Kharat': 'symbols/pipe.svg',
        'Shreyas Dhotre': 'symbols/jhad.svg',
        'Shruti Misal': 'symbols/vati.svg',
        'Vishakha Kachare': 'symbols/rangit_aakar.svg',
        'Pranjal Dhare': 'symbols/table.svg',
        'Arvi Khandare': 'symbols/cup.svg',
        'Ganesh Rathod': 'symbols/khurchi.svg',
        'Namrata Dhadhe': 'symbols/laptop.svg',
        'Pradeep Kachare': 'symbols/phala.svg',
        'Punam Sharma': 'symbols/ring.svg',
        'Prajwal Shinde': 'symbols/chamcha.svg',
        'Pari Ahire': 'symbols/bhande.svg',
        'Arnav Kumbhar': 'symbols/kapat.svg',
        'Sambhav Lags': 'symbols/trikon.svg',
        'Nayan Yenpure': 'symbols/bulb.svg',
        'Rupesh Shinde': 'symbols/chendu.svg',
        'Ambika Tondare': 'symbols/bottle.svg',
        'Gauri Rathod': 'symbols/kodrabar.svg',
        'Durva Kharat': 'symbols/eraser.svg',
        'Rudra Vadtya': 'symbols/pankha.svg',
    }
    
    for name, symbol_path in symbol_map.items():
        Candidate.objects.filter(name=name).update(symbol_image=symbol_path)


def remove_symbols(apps, schema_editor):
    Candidate = apps.get_model('voting', 'Candidate')
    Candidate.objects.all().update(symbol_image='')


class Migration(migrations.Migration):

    dependencies = [
        ('voting', '0005_add_symbol_image'),
    ]

    operations = [
        migrations.RunPython(assign_symbols, remove_symbols),
    ]
