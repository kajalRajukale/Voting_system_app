from django.db import migrations


def create_candidates(apps, schema_editor):
    Candidate = apps.get_model('voting', 'Candidate')
    
    candidates = [
        ('Riddhi Gaikwad', 'रिद्धी गायकवाड'),
        ('Aryan Takbhate', 'आर्यन ताकभाते'),
        ('Swara Malekar', 'स्वरा मळेकर'),
        ('Janhvi Vasave', 'जान्हवी वसावे'),
        ('Riya Raut', 'रिया रावडे'),
        ('Prabhat Pandey', 'प्रभात पांडे'),
        ('Adarsh Sasane', 'आदर्श ससाणे'),
        ('Gayatri Chate', 'गायत्री चाटे'),
        ('Om Suryavanshi', 'ओम सूर्यवंशी'),
        ('Aarti Pathade', 'आरती पठाडे'),
        ('Altamash Sheikh', 'अल्तमश शेख'),
        ('Sharvari Mane', 'शर्वरी माने'),
        ('Swaraj Gore', 'स्वराज गोरे'),
        ('Aryan Mhaske', 'आर्यन म्हस्के'),
        ('Shrividya Yeldi', 'श्रीविद्या येल्दी'),
        ('Aryan Panchal', 'आर्यन पांचाळ'),
        ('Spandan Bilmar', 'स्पंदन बिलमर'),
        ('Viraj Chavan', 'विराज चव्हाण'),
        ('Rajvir Ankush', 'राजवीर अंकुशे'),
        ('Ganesh Nandure', 'गणेश नांदुरे'),
        ('Bhakti Kharat', 'भक्ती खरात'),
        ('Shreyas Dhotre', 'श्रेयस धोत्रे'),
        ('Shruti Misal', 'श्रुती मिसाळ'),
        ('Vishakha Kachare', 'विशाखा कचरे'),
        ('Pranjal Dhare', 'प्रांजल धारे'),
        ('Arvi Khandare', 'आर्वी खंदारे'),
        ('Ganesh Rathod', 'गणेश राठोड'),
        ('Namrata Dhadhe', 'नम्रता धडे'),
        ('Pradeep Kachare', 'प्रदीप कचरे'),
        ('Punam Sharma', 'पुनम शर्मा'),
        ('Prajwal Shinde', 'प्रज्वल शिंदे'),
        ('Pari Ahire', 'परी अहिरे'),
        ('Arnav Kumbhar', 'अर्णव कुंभार'),
        ('Sambhav Lags', 'संभव लगस'),
        ('Nayan Yenpure', 'नयन येनपुरे'),
        ('Rupesh Shinde', 'रुपेश शिंदे'),
        ('Ambika Tondare', 'अंबिका तोंडारे'),
        ('Gauri Rathod', 'गौरी राठोड'),
        ('Durva Kharat', 'दुर्वा खरात'),
        ('Rudra Vadtya', 'रुद्र वडत्या'),
    ]
    
    for name, name_marathi in candidates:
        Candidate.objects.get_or_create(
            name=name,
            defaults={'name_marathi': name_marathi}
        )


def remove_candidates(apps, schema_editor):
    apps.get_model('voting', 'Candidate').objects.all().delete()


class Migration(migrations.Migration):

    dependencies = [
        ('voting', '0003_replace_symbol_with_candidate'),
    ]

    operations = [
        migrations.RunPython(create_candidates, remove_candidates),
    ]
