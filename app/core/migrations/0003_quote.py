# Generated by Django 3.1.5 on 2021-01-31 23:16

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20210131_2313'),
    ]

    operations = [
        migrations.CreateModel(
            name='Quote',
            fields=[
                ('quote_id', models.CharField(default=uuid.uuid4, max_length=255, primary_key=True, serialize=False, unique=True)),
                ('pet_name', models.CharField(default='MAX', max_length=255)),
                ('base_rate', models.DecimalField(decimal_places=2, default=54.11, max_digits=4)),
                ('geographical_factor', models.DecimalField(decimal_places=2, default=0, max_digits=4)),
                ('gender_factor', models.CharField(blank=True, choices=[('Cat', [('Male', 'Male'), ('Female', 'Female')]), ('Dog', [('Male', 'Male'), ('Female', 'Female')])], max_length=6)),
                ('breed_factor', models.CharField(blank=True, choices=[('Dog', [('Affenpinscher\xa0', 'Affenpinscher\xa0'), ('Afghan Hound\xa0', 'Afghan Hound\xa0'), ('Airedale Terrier\xa0', 'Airedale Terrier\xa0'), ('Akita\xa0', 'Akita\xa0'), ('Alaskan Malamute\xa0', 'Alaskan Malamute\xa0'), ('American\xa0Bandogge\xa0Mastiff\xa0', 'American\xa0Bandogge\xa0Mastiff\xa0'), ('American Black and Tan Coonhound\xa0', 'American Black and Tan Coonhound\xa0'), ('American Bulldog\xa0', 'American Bulldog\xa0'), ('American English Coonhound\xa0', 'American English Coonhound\xa0'), ('American Eskimo\xa0', 'American Eskimo\xa0'), ('American Foxhound\xa0', 'American Foxhound\xa0'), ('American Hairless Terrier\xa0', 'American Hairless Terrier\xa0'), ('American Mastiff\xa0', 'American Mastiff\xa0'), ('American Pitbull Terrier\xa0', 'American Pitbull Terrier\xa0'), ('American Staffordshire Bull Terrier\xa0', 'American Staffordshire Bull Terrier\xa0'), ('American Staffordshire Terrier\xa0', 'American Staffordshire Terrier\xa0'), ('American Water Spaniel\xa0', 'American Water Spaniel\xa0'), ('Anatolian Shepherd\xa0', 'Anatolian Shepherd\xa0'), ('Appenzeller\xa0Sennenhunde\xa0', 'Appenzeller\xa0Sennenhunde\xa0'), ('Argentine\xa0Dogo\xa0', 'Argentine\xa0Dogo\xa0'), ('Australian Cattle Dog\xa0', 'Australian Cattle Dog\xa0'), ('Australian Kelpie\xa0', 'Australian Kelpie\xa0'), ('Australian Shepherd\xa0', 'Australian Shepherd\xa0'), ('Australian Silky Terrier\xa0', 'Australian Silky Terrier\xa0'), ('Australian Stumpy Tail Cattle\xa0', 'Australian Stumpy Tail Cattle\xa0'), ('Australian Terrier\xa0', 'Australian Terrier\xa0'), ('Azawakh Hound\xa0', 'Azawakh Hound\xa0'), ('Barbet\xa0', 'Barbet\xa0'), ('Basenji\xa0', 'Basenji\xa0'), ('Basset Fauve de Bretagne\xa0', 'Basset Fauve de Bretagne\xa0'), ('Basset Hound\xa0', 'Basset Hound\xa0'), ('Bavarian Mountain Hound\xa0', 'Bavarian Mountain Hound\xa0'), ('Beagle\xa0', 'Beagle\xa0'), ('Bearded Collie\xa0', 'Bearded Collie\xa0'), ('Beauceron\xa0', 'Beauceron\xa0'), ('Bedlington Terrier\xa0', 'Bedlington Terrier\xa0'), ('Belgian Mastiff\xa0', 'Belgian Mastiff\xa0'), ('Belgian Sheepdog\xa0', 'Belgian Sheepdog\xa0'), ('Bergamasco Sheepdog\xa0', 'Bergamasco Sheepdog\xa0'), ('Berger Picard/Picardy Sheepdog\xa0', 'Berger Picard/Picardy Sheepdog\xa0'), ('Bernese Mountain Dog\xa0', 'Bernese Mountain Dog\xa0'), ('Bichon\xa0Frise\xa0', 'Bichon\xa0Frise\xa0'), ('Black and Tan Coonhound\xa0', 'Black and Tan Coonhound\xa0'), ('Black Russian Terrier\xa0', 'Black Russian Terrier\xa0'), ('Blackmouth Cur\xa0', 'Blackmouth Cur\xa0'), ('Bloodhound\xa0', 'Bloodhound\xa0'), ('Blue Picardy Spaniel\xa0', 'Blue Picardy Spaniel\xa0'), ('Blue Tick Coonhound\xa0', 'Blue Tick Coonhound\xa0'), ('Boerboel\xa0', 'Boerboel\xa0'), ('Bolognese\xa0', 'Bolognese\xa0'), ('Border Collie\xa0', 'Border Collie\xa0'), ('Border Terrier\xa0', 'Border Terrier\xa0'), ('Borzoi/Russian Wolfhound\xa0', 'Borzoi/Russian Wolfhound\xa0'), ('Boston Terrier\xa0', 'Boston Terrier\xa0'), ('Bouvier des\xa0Flandres\xa0', 'Bouvier des\xa0Flandres\xa0'), ('Boxer\xa0', 'Boxer\xa0'), ('Boykin Spaniel\xa0', 'Boykin Spaniel\xa0'), ('Bracco\xa0Italiano\xa0', 'Bracco\xa0Italiano\xa0'), ('Briard\xa0', 'Briard\xa0'), ('Brittany\xa0', 'Brittany\xa0'), ('Brussels Griffon\xa0', 'Brussels Griffon\xa0'), ('Bull Boxer\xa0', 'Bull Boxer\xa0'), ('Bull Terrier\xa0', 'Bull Terrier\xa0'), ('Bullmastiff\xa0', 'Bullmastiff\xa0'), ('Cairn Terrier\xa0', 'Cairn Terrier\xa0'), ('Canaan Dog\xa0', 'Canaan Dog\xa0'), ('Canadian Eskimo/Inuit\xa0', 'Canadian Eskimo/Inuit\xa0'), ('Cane Corso\xa0', 'Cane Corso\xa0'), ('Cardigan Welsh Corgi\xa0', 'Cardigan Welsh Corgi\xa0'), ('Catahoula Leopard Dog\xa0', 'Catahoula Leopard Dog\xa0'), ('Caucasian\xa0Ovcharka\xa0', 'Caucasian\xa0Ovcharka\xa0'), ('Cavalier King Charles Spaniel\xa0', 'Cavalier King Charles Spaniel\xa0'), ('Central Asian Shepherd\xa0', 'Central Asian Shepherd\xa0'), ('Cesky Terrier\xa0', 'Cesky Terrier\xa0'), ('Chesapeake Bay Retriever\xa0', 'Chesapeake Bay Retriever\xa0'), ('Chihuahua\xa0', 'Chihuahua\xa0'), ('Chinese Crested\xa0', 'Chinese Crested\xa0'), ('Chinook\xa0', 'Chinook\xa0'), ('Chipom\xa0', 'Chipom\xa0'), ('Chipoo\xa0', 'Chipoo\xa0'), ('Chow\xa0Chow\xa0', 'Chow\xa0Chow\xa0'), ('Cirneco\xa0dell Etna\xa0', 'Cirneco\xa0dell Etna\xa0'), ('Clumber Spaniel\xa0', 'Clumber Spaniel\xa0'), ('Cockapoo\xa0', 'Cockapoo\xa0'), ('Cocker Spaniel\xa0', 'Cocker Spaniel\xa0'), ('Collie\xa0', 'Collie\xa0'), ('Coonhound\xa0', 'Coonhound\xa0'), ('Coton\xa0de Tulear\xa0', 'Coton\xa0de Tulear\xa0'), ('Curly-Coated Retriever\xa0', 'Curly-Coated Retriever\xa0'), ('Czechoslovakian Wolfdog\xa0', 'Czechoslovakian Wolfdog\xa0'), ('Dachshund\xa0', 'Dachshund\xa0'), ('Dalmatian\xa0', 'Dalmatian\xa0'), ('Dandie\xa0Dinmont Terrier\xa0', 'Dandie\xa0Dinmont Terrier\xa0'), ('Deerhound\xa0', 'Deerhound\xa0'), ('Dingo/Carolina\xa0', 'Dingo/Carolina\xa0'), ('Doberman Pinscher\xa0', 'Doberman Pinscher\xa0'), ('Dogue\xa0de Bordeaux\xa0', 'Dogue\xa0de Bordeaux\xa0'), ('Drever\xa0', 'Drever\xa0'), ('Dunker/Norwegian Hound\xa0', 'Dunker/Norwegian Hound\xa0'), ('Dutch Sheepdog\xa0', 'Dutch Sheepdog\xa0'), ('English Bulldog\xa0', 'English Bulldog\xa0'), ('English Cocker Spaniel\xa0', 'English Cocker Spaniel\xa0'), ('English Foxhound\xa0', 'English Foxhound\xa0'), ('English Setter\xa0', 'English Setter\xa0'), ('English Shepherd\xa0', 'English Shepherd\xa0'), ('English Springer Spaniel\xa0', 'English Springer Spaniel\xa0'), ('English Toy Spaniel\xa0', 'English Toy Spaniel\xa0'), ('English Toy Terrier\xa0', 'English Toy Terrier\xa0'), ('Entlebucher Mountain Dog\xa0', 'Entlebucher Mountain Dog\xa0'), ('Estrela Mountain Dog\xa0', 'Estrela Mountain Dog\xa0'), ('Eurasian/Eurasier\xa0', 'Eurasian/Eurasier\xa0'), ('Field Spaniel\xa0', 'Field Spaniel\xa0'), ('Fila\xa0Brasileiro/Brazillian\xa0Mastiff\xa0', 'Fila\xa0Brasileiro/Brazillian\xa0Mastiff\xa0'), ('Finnish\xa0Lapphund\xa0', 'Finnish\xa0Lapphund\xa0'), ('Finnish Spitz\xa0', 'Finnish Spitz\xa0'), ('Flat-Coated Retriever\xa0', 'Flat-Coated Retriever\xa0'), ('Formosan (Taiwanese) Mountain Dog\xa0', 'Formosan (Taiwanese) Mountain Dog\xa0'), ('Fox Terrier\xa0', 'Fox Terrier\xa0'), ('French Bulldog\xa0', 'French Bulldog\xa0'), ('French Spaniel\xa0', 'French Spaniel\xa0'), ('Ganaraskan\xa0', 'Ganaraskan\xa0'), ('Gascogne Braque\xa0Francais\xa0', 'Gascogne Braque\xa0Francais\xa0'), ('German Pinscher\xa0', 'German Pinscher\xa0'), ('German Pointer\xa0', 'German Pointer\xa0'), ('German Shepherd\xa0', 'German Shepherd\xa0'), ('German Spitz\xa0', 'German Spitz\xa0'), ('German/Mittel Spitz\xa0', 'German/Mittel Spitz\xa0'), ('Giant Schnauzer\xa0', 'Giant Schnauzer\xa0'), ('Glen of\xa0Imaal\xa0Terrier\xa0', 'Glen of\xa0Imaal\xa0Terrier\xa0'), ('Golden Retriever\xa0', 'Golden Retriever\xa0'), ('Goldendoodle\xa0', 'Goldendoodle\xa0'), ('Gordon Setter\xa0', 'Gordon Setter\xa0'), ('Great Dane\xa0', 'Great Dane\xa0'), ('Greater Swiss Mountain Dog\xa0', 'Greater Swiss Mountain Dog\xa0'), ('Greenland Dog\xa0', 'Greenland Dog\xa0'), ('Greyhound\xa0', 'Greyhound\xa0'), ('Groenendael\xa0Belgian Shepherd\xa0', 'Groenendael\xa0Belgian Shepherd\xa0'), ('Hamiltonstovare\xa0', 'Hamiltonstovare\xa0'), ('Harrier\xa0', 'Harrier\xa0'), ('Havanese\xa0', 'Havanese\xa0'), ('Hovawart\xa0', 'Hovawart\xa0'), ('Ibizan Hound\xa0', 'Ibizan Hound\xa0'), ('Icelandic sheepdog\xa0', 'Icelandic sheepdog\xa0'), ('Irish Setter\xa0', 'Irish Setter\xa0'), ('Irish Terrier\xa0', 'Irish Terrier\xa0'), ('Irish Water Spaniel\xa0', 'Irish Water Spaniel\xa0'), ('Irish Wolfhound\xa0', 'Irish Wolfhound\xa0'), ('Italian\xa0Bulldogge\xa0', 'Italian\xa0Bulldogge\xa0'), ('Italian Greyhound\xa0', 'Italian Greyhound\xa0'), ('Jack Russell Terrier\xa0', 'Jack Russell Terrier\xa0'), ('Japanese Chin\xa0', 'Japanese Chin\xa0'), ('Japanese Spitz\xa0', 'Japanese Spitz\xa0'), ('Japanese Terrier\xa0', 'Japanese Terrier\xa0'), ('Kai Ken\xa0', 'Kai Ken\xa0'), ('Karelian Bear Dog\xa0', 'Karelian Bear Dog\xa0'), ('Keeshond\xa0', 'Keeshond\xa0'), ('Kerry Blue Terrier\xa0', 'Kerry Blue Terrier\xa0'), ('Kishu\xa0Ken\xa0', 'Kishu\xa0Ken\xa0'), ('Komondor\xa0', 'Komondor\xa0'), ('Kooikerhondje\xa0', 'Kooikerhondje\xa0'), ('Kuvasz\xa0', 'Kuvasz\xa0'), ('Labradoodle\xa0', 'Labradoodle\xa0'), ('Labrador Retriever\xa0', 'Labrador Retriever\xa0'), ('Laekenois\xa0Belgian Shepherd\xa0', 'Laekenois\xa0Belgian Shepherd\xa0'), ('Lagotto\xa0Romagnolo\xa0', 'Lagotto\xa0Romagnolo\xa0'), ('Lakeland Terrier\xa0', 'Lakeland Terrier\xa0'), ('Lancashire Heeler\xa0', 'Lancashire Heeler\xa0'), ('Landseer\xa0', 'Landseer\xa0'), ('Large\xa0Munsterlander\xa0', 'Large\xa0Munsterlander\xa0'), ('Leonberger\xa0', 'Leonberger\xa0'), ('Lhasa Apso\xa0', 'Lhasa Apso\xa0'), ('Lowchen\xa0', 'Lowchen\xa0'), ('Malinois Belgian Shepherd\xa0', 'Malinois Belgian Shepherd\xa0'), ('Maltese\xa0', 'Maltese\xa0'), ('Maltipoo\xa0', 'Maltipoo\xa0'), ('Manchester Terrier\xa0', 'Manchester Terrier\xa0'), ('Maremma\xa0', 'Maremma\xa0'), ('Mastiff\xa0', 'Mastiff\xa0'), ('Mexican Hairless\xa0', 'Mexican Hairless\xa0'), ('Mi-Ki\xa0', 'Mi-Ki\xa0'), ('Miniature Australian Shepherd\xa0', 'Miniature Australian Shepherd\xa0'), ('Miniature Bull Terrier\xa0', 'Miniature Bull Terrier\xa0'), ('Miniature Dachshund\xa0', 'Miniature Dachshund\xa0'), ('Miniature Pinscher\xa0', 'Miniature Pinscher\xa0'), ('Miniature Poodle\xa0', 'Miniature Poodle\xa0'), ('Miniature Schnauzer\xa0', 'Miniature Schnauzer\xa0'), ('Mixed Breed - Dog - Unknown Size\xa0', 'Mixed Breed - Dog - Unknown Size\xa0'), ('Mudi\xa0', 'Mudi\xa0'), ('Neapolitan Mastiff\xa0', 'Neapolitan Mastiff\xa0'), ('Newfoundland\xa0', 'Newfoundland\xa0'), ('Norfolk Terrier\xa0', 'Norfolk Terrier\xa0'), ('Norrbottenspets\xa0', 'Norrbottenspets\xa0'), ('Norwegian\xa0Buhund\xa0', 'Norwegian\xa0Buhund\xa0'), ('Norwegian Elkhound\xa0', 'Norwegian Elkhound\xa0'), ('Norwich Terrier\xa0', 'Norwich Terrier\xa0'), ('Nova Scotia Duck Tolling Retriever\xa0', 'Nova Scotia Duck Tolling Retriever\xa0'), ('Old Boston\xa0Bulldogge\xa0', 'Old Boston\xa0Bulldogge\xa0'), ('Old English Sheepdog\xa0', 'Old English Sheepdog\xa0'), ('Old Victorian\xa0Bulldogge\xa0', 'Old Victorian\xa0Bulldogge\xa0'), ('Olde English Bulldog\xa0', 'Olde English Bulldog\xa0'), ('Otterhound\xa0', 'Otterhound\xa0'), ('Papillon\xa0', 'Papillon\xa0'), ('Parson Russell Terrier\xa0', 'Parson Russell Terrier\xa0'), ('Patterdale/Fell Terrier\xa0', 'Patterdale/Fell Terrier\xa0'), ('Pekingese\xa0', 'Pekingese\xa0'), ('Pembroke Welsh Corgi\xa0', 'Pembroke Welsh Corgi\xa0'), ('Perro\xa0de Presa\xa0Canario\xa0', 'Perro\xa0de Presa\xa0Canario\xa0'), ('Peruvian Inca Orchid\xa0', 'Peruvian Inca Orchid\xa0'), ('Petit Basset Griffon\xa0Vendeen\xa0', 'Petit Basset Griffon\xa0Vendeen\xa0'), ('Pharaoh Hound\xa0', 'Pharaoh Hound\xa0'), ('Picardy Spaniel\xa0', 'Picardy Spaniel\xa0'), ('Plott\xa0', 'Plott\xa0'), ('Pointer\xa0', 'Pointer\xa0'), ('Polish Lowland Sheepdog\xa0', 'Polish Lowland Sheepdog\xa0'), ('Pomapoo\xa0', 'Pomapoo\xa0'), ('Pomeranian\xa0', 'Pomeranian\xa0'), ('Poodle\xa0', 'Poodle\xa0'), ('Porkie\xa0', 'Porkie\xa0'), ('Portuguese\xa0Podengo\xa0', 'Portuguese\xa0Podengo\xa0'), ('Portuguese Pointer\xa0', 'Portuguese Pointer\xa0'), ('Portuguese Water\xa0', 'Portuguese Water\xa0'), ('Prague Ratter\xa0', 'Prague Ratter\xa0'), ('Pudelpointer\xa0', 'Pudelpointer\xa0'), ('Pug\xa0', 'Pug\xa0'), ('Puggle\xa0', 'Puggle\xa0'), ('Puli\xa0', 'Puli\xa0'), ('Pumi\xa0', 'Pumi\xa0'), ('Pyrenean Mastiff\xa0', 'Pyrenean Mastiff\xa0'), ('Pyrenean Mountain Dog (Great Pyrenees)\xa0', 'Pyrenean Mountain Dog (Great Pyrenees)\xa0'), ('Pyrenean Sheepdog\xa0', 'Pyrenean Sheepdog\xa0'), ('Pyrenean Shepherd\xa0', 'Pyrenean Shepherd\xa0'), ('Pyrenees Braque\xa0Francais\xa0', 'Pyrenees Braque\xa0Francais\xa0'), ('Rafeiro\xa0do\xa0Alentejo\xa0', 'Rafeiro\xa0do\xa0Alentejo\xa0'), ('Rat Terrier\xa0', 'Rat Terrier\xa0'), ('Redbone Coonhound\xa0', 'Redbone Coonhound\xa0'), ('Rhodesian Ridgeback\xa0', 'Rhodesian Ridgeback\xa0'), ('Rottweiler\xa0', 'Rottweiler\xa0'), ('Russian\xa0Bolonka\xa0', 'Russian\xa0Bolonka\xa0'), ('Saint Bernard\xa0', 'Saint Bernard\xa0'), ('Saluki (Gazelle Hound)\xa0', 'Saluki (Gazelle Hound)\xa0'), ('Samoyed\xa0', 'Samoyed\xa0'), ('Schipperke\xa0', 'Schipperke\xa0'), ('Schnoodle\xa0', 'Schnoodle\xa0'), ('Scottish Deerhound\xa0', 'Scottish Deerhound\xa0'), ('Scottish Terrier\xa0', 'Scottish Terrier\xa0'), ('Sealyham Terrier\xa0', 'Sealyham Terrier\xa0'), ('Segugio\xa0Italiano\xa0', 'Segugio\xa0Italiano\xa0'), ('Shar Pei\xa0', 'Shar Pei\xa0'), ('Shetland Sheepdog\xa0', 'Shetland Sheepdog\xa0'), ('Shiba\xa0Inu\xa0', 'Shiba\xa0Inu\xa0'), ('Shih Tzu\xa0', 'Shih Tzu\xa0'), ('Shikoku\xa0', 'Shikoku\xa0'), ('Shiloh Shepherd\xa0', 'Shiloh Shepherd\xa0'), ('Siberian Husky\xa0', 'Siberian Husky\xa0'), ('Silken\xa0Windhound\xa0', 'Silken\xa0Windhound\xa0'), ('Silky Terrier\xa0', 'Silky Terrier\xa0'), ('Skye Terrier\xa0', 'Skye Terrier\xa0'), ('Sloughi\xa0', 'Sloughi\xa0'), ('Small\xa0Munsterlander\xa0', 'Small\xa0Munsterlander\xa0'), ('Snoodle\xa0', 'Snoodle\xa0'), ('Soft Coated Wheaten Terrier\xa0', 'Soft Coated Wheaten Terrier\xa0'), ('Spanish Bulldog\xa0', 'Spanish Bulldog\xa0'), ('Spanish Mastiff\xa0', 'Spanish Mastiff\xa0'), ('Spanish Water Dog\xa0', 'Spanish Water Dog\xa0'), ('Spinone\xa0Italiano\xa0', 'Spinone\xa0Italiano\xa0'), ('St. Johns Waterdog\xa0', 'St. Johns Waterdog\xa0'), ('Stabyhoun\xa0(Stabij)\xa0', 'Stabyhoun\xa0(Stabij)\xa0'), ('Staffordshire Bull Terrier\xa0', 'Staffordshire Bull Terrier\xa0'), ('Standard Schnauzer\xa0', 'Standard Schnauzer\xa0'), ('Sussex Spaniel\xa0', 'Sussex Spaniel\xa0'), ('Swedish Elkhound\xa0', 'Swedish Elkhound\xa0'), ('Swedish\xa0Lapphund\xa0', 'Swedish\xa0Lapphund\xa0'), ('Swedish\xa0Vallhund\xa0', 'Swedish\xa0Vallhund\xa0'), ('Terrier\xa0', 'Terrier\xa0'), ('Terripoo\xa0', 'Terripoo\xa0'), ('Tervuren\xa0Belgian Shepherd\xa0', 'Tervuren\xa0Belgian Shepherd\xa0'), ('Texas Blue Lacey\xa0', 'Texas Blue Lacey\xa0'), ('Thai Ridgeback\xa0', 'Thai Ridgeback\xa0'), ('Tibetan Mastiff\xa0', 'Tibetan Mastiff\xa0'), ('Tibetan Spaniel\xa0', 'Tibetan Spaniel\xa0'), ('Tibetan Terrier\xa0', 'Tibetan Terrier\xa0'), ('Tosa\xa0', 'Tosa\xa0'), ('Toy Fox Terrier\xa0', 'Toy Fox Terrier\xa0'), ('Toy Manchester Terrier\xa0', 'Toy Manchester Terrier\xa0'), ('Toy Poodle\xa0', 'Toy Poodle\xa0'), ('Treeing Walker Coonhound\xa0', 'Treeing Walker Coonhound\xa0'), ('Victorian Bulldog\xa0', 'Victorian Bulldog\xa0'), ('Vizsla\xa0', 'Vizsla\xa0'), ('Weimaraner\xa0', 'Weimaraner\xa0'), ('Welsh Sheepdog (Welsh Collie)\xa0', 'Welsh Sheepdog (Welsh Collie)\xa0'), ('Welsh Springer Spaniel\xa0', 'Welsh Springer Spaniel\xa0'), ('Welsh Terrier\xa0', 'Welsh Terrier\xa0'), ('West Highland White Terrier\xa0', 'West Highland White Terrier\xa0'), ('Whippet\xa0', 'Whippet\xa0'), ('Wirehaired Pointing Griffon\xa0', 'Wirehaired Pointing Griffon\xa0'), ('Yorkiepoo\xa0', 'Yorkiepoo\xa0'), ('Yorkshire Terrier\xa0', 'Yorkshire Terrier\xa0')]), ('Cat', [('Abyssinian\u202f\xa0', 'Abyssinian\u202f\xa0'), ('American Bobtail\u202f\xa0', 'American Bobtail\u202f\xa0'), ('American Curl\u202f\xa0', 'American Curl\u202f\xa0'), ('American Shorthair\u202f\xa0', 'American Shorthair\u202f\xa0'), ('American Wirehair\u202f\xa0', 'American Wirehair\u202f\xa0'), ('Anatolian\u202f\xa0', 'Anatolian\u202f\xa0'), ('Balinese\u202f\xa0', 'Balinese\u202f\xa0'), ('Bengal\u202f\xa0', 'Bengal\u202f\xa0'), ('Birman\u202f\xa0', 'Birman\u202f\xa0'), ('Bombay\u202f\xa0', 'Bombay\u202f\xa0'), ('British Longhair\u202f\xa0', 'British Longhair\u202f\xa0'), ('British Shorthair\u202f\xa0', 'British Shorthair\u202f\xa0'), ('Burmese\u202f\xa0', 'Burmese\u202f\xa0'), ('California Spangled\u202f\xa0', 'California Spangled\u202f\xa0'), ('Chartreux\u202f\xa0', 'Chartreux\u202f\xa0'), ('Chausie\u202f\xa0', 'Chausie\u202f\xa0'), ('Colorpoint\u202fShorthair\u202f\xa0', 'Colorpoint\u202fShorthair\u202f\xa0'), ('Cornish Rex\u202f\xa0', 'Cornish Rex\u202f\xa0'), ('Cymric\u202f\xa0', 'Cymric\u202f\xa0'), ('Devon Rex\u202f\xa0', 'Devon Rex\u202f\xa0'), ('Donskoy\u202f\xa0', 'Donskoy\u202f\xa0'), ('Egyptian Mau\u202f\xa0', 'Egyptian Mau\u202f\xa0'), ('Exotic Longhair\u202f\xa0', 'Exotic Longhair\u202f\xa0'), ('Exotic Shorthair\u202f\xa0', 'Exotic Shorthair\u202f\xa0'), ('Havana Brown\u202f\xa0', 'Havana Brown\u202f\xa0'), ('Himalayan\u202f\xa0', 'Himalayan\u202f\xa0'), ('Japanese Bobtail\u202f\xa0', 'Japanese Bobtail\u202f\xa0'), ('Javanese\u202f\xa0', 'Javanese\u202f\xa0'), ('Korat\u202f\xa0', 'Korat\u202f\xa0'), ('LaPerm\u202f\xa0', 'LaPerm\u202f\xa0'), ('Maine Coon\u202f\xa0', 'Maine Coon\u202f\xa0'), ('Manx\u202f\xa0', 'Manx\u202f\xa0'), ('Mixed Breed - Cat\u202f\xa0', 'Mixed Breed - Cat\u202f\xa0'), ('Munchkin\u202f\xa0', 'Munchkin\u202f\xa0'), ('Nebelung\u202f\xa0', 'Nebelung\u202f\xa0'), ('Norwegian Forest\u202f\xa0', 'Norwegian Forest\u202f\xa0'), ('Ocicat\u202f\xa0', 'Ocicat\u202f\xa0'), ('Oriental\u202f\xa0', 'Oriental\u202f\xa0'), ('Persian\u202f\xa0', 'Persian\u202f\xa0'), ('Peterbald\u202f\xa0', 'Peterbald\u202f\xa0'), ('Pixiebob\u202f\xa0', 'Pixiebob\u202f\xa0'), ('Ragdoll\u202f\xa0', 'Ragdoll\u202f\xa0'), ('Russian Blue\u202f\xa0', 'Russian Blue\u202f\xa0'), ('Savannah\u202f\xa0', 'Savannah\u202f\xa0'), ('Scottish Fold\u202f\xa0', 'Scottish Fold\u202f\xa0'), ('Selkirk Rex\u202f\xa0', 'Selkirk Rex\u202f\xa0'), ('Serengeti\u202f\xa0', 'Serengeti\u202f\xa0'), ('Siamese\u202f\xa0', 'Siamese\u202f\xa0'), ('Siberian\u202f\xa0', 'Siberian\u202f\xa0'), ('Singapura\u202f\xa0', 'Singapura\u202f\xa0'), ('Snowshoe\u202f\xa0', 'Snowshoe\u202f\xa0'), ('Somali\u202f\xa0', 'Somali\u202f\xa0'), ('Sphynx\u202f\xa0', 'Sphynx\u202f\xa0'), ('Thai\u202f\xa0', 'Thai\u202f\xa0'), ('Tiffany\u202f\xa0', 'Tiffany\u202f\xa0'), ('Tonkinese\u202f\xa0', 'Tonkinese\u202f\xa0'), ('Toyger\u202f\xa0', 'Toyger\u202f\xa0'), ('Turkish Angora\u202f\xa0', 'Turkish Angora\u202f\xa0'), ('Turkish Van\u202f\xa0', 'Turkish Van\u202f\xa0'), ('Ojos\u202fAzules\u202f\xa0', 'Ojos\u202fAzules\u202f\xa0')])], max_length=255)),
                ('age_factor', models.CharField(blank=True, choices=[('Dog', [('0-1 year', '0-1 year'), ('1 year', '1 year'), ('2 years', '2 years'), ('3 years', '3 years'), ('4 years', '4 years'), ('5 years', '5 years'), ('6 years', '6 years'), ('7 years', '7 years'), ('8 years', '8 years'), ('9 years', '9 years'), ('10 years', '10 years'), ('11 years', '11 years'), ('12 years', '12 years'), ('13 years', '13 years'), ('14 years', '14 years'), ('15 years', '15 years'), ('16 years', '16 years'), ('17 years', '17 years'), ('18 years', '18 years'), ('19 years', '19 years'), ('20 years or more', '20 years or more')]), ('Cat', [('0-1 year', '0-1 year'), ('1 year', '1 year'), ('2 years', '2 years'), ('3 years', '3 years'), ('4 years', '4 years'), ('5 years', '5 years'), ('6 years', '6 years'), ('7 years', '7 years'), ('8 years', '8 years'), ('9 years', '9 years'), ('10 years', '10 years'), ('11 years', '11 years'), ('12 years', '12 years'), ('13 years', '13 years'), ('14 years', '14 years'), ('15 years', '15 years'), ('16 years', '16 years'), ('17 years', '17 years'), ('18 years', '18 years'), ('19 years', '19 years'), ('20 years or more', '20 years or more')])], max_length=255)),
                ('policy_limit_factor', models.CharField(blank=True, choices=[('$1,000', '$1,000'), ('$2,000', '$2,000'), ('$3,000', '$3,000'), ('$4,000', '$4,000'), ('$5,000', '$5,000'), ('$6,000', '$6,000'), ('$7,000', '$7,000'), ('$8,000', '$8,000'), ('$9,000', '$9,000'), ('$10,000', '$10,000'), ('$11,000', '$11,000'), ('$12,000', '$12,000'), ('$13,000', '$13,000'), ('$14,000', '$14,000'), ('$15,000', '$15,000'), ('$16,000', '$16,000'), ('$17,000', '$17,000'), ('$18,000', '$18,000'), ('$19,000', '$19,000'), ('$20,000', '$20,000'), ('Unlimited', 'Unlimited')], max_length=255)),
                ('deductibale_factor', models.PositiveIntegerField(default=500)),
                ('coinsurance_factor', models.PositiveIntegerField(default=50)),
                ('exam_fee_factor', models.BooleanField(default=False)),
                ('holistic_alternative_treatment_factor', models.BooleanField(default=False)),
                ('boarding_advertising_holoday_cancellation_rate', models.BooleanField(default=False)),
                ('breeding_endorsement', models.CharField(blank=True, choices=[('No', 'No'), ('Male', 'Male'), ('Female', 'Female')], max_length=255)),
                ('discount_factor', models.CharField(blank=True, max_length=255)),
                ('digital_partner_factor', models.BooleanField(default=False)),
                ('affinity_group_factor', models.BooleanField(default=False)),
                ('smart_collar_factor', models.BooleanField(default=False)),
                ('employee_benefit_factor', models.DecimalField(decimal_places=2, default=0, max_digits=4)),
                ('default', models.BooleanField(db_index=True, default=None, help_text='Both "Unknown" and "No" means that the plan is not default', null=True, unique=True)),
                ('available', models.BooleanField(db_index=True, default=False, help_text='Is still available for purchase', verbose_name='available')),
                ('visible', models.BooleanField(db_index=True, default=True, help_text='Is visible in current offer', verbose_name='visible')),
                ('created', models.DateTimeField(db_index=True, verbose_name='created')),
            ],
        ),
    ]