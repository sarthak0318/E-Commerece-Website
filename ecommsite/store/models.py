from django.db import models

# Create your models here.

class product(models.Model):

    def __str__(self):
        return self.name

    name = models.CharField(max_length=500)
    category = models.CharField(max_length=200)
    description = models.TextField(max_length=10000)
    price = models.IntegerField()
    discount_price = models.IntegerField()
    image = models.CharField(max_length=500, default="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAOEAAADhCAMAAAAJbSJIAAAASFBMVEXh5urDzdbCzNPb4OXR2Nzc5OrL0tjR2t/h5uvV29/X3+Th6OzDzdfCzdLCzdXO2dvM1NvT3uDI0djZ4urDztG/ydDR3N7K1Ne85QaTAAADmElEQVR4nO3ciXKqMBiGYQki0UCKtNT7v9OTsCib5bSC8uP7TGfooCKfwWyAux0AAAAAAAAAAAAAAAAAAAAAAAAAAADwbrRe+g0W3v40s/D29eKf4cT7b+Q93pw+LenV6RwdKhtY//fTIgh+fPjuk9X+1fmcUAXLIeFTkJCEJHy9JqGv5edig2SFCRexzYT+WGgOiPUlVPZxne2tKaH75iTZcQ5xXZBrS+jFs4wWo2KdZVgmnGWLJHw2Ev4HYzrf360lNOHlctkfW2s2lFC7fOfUKj9LUGTVOrOthNpkqa0bP5uH9eoNJdyZrAmTuA6DqucNt5TwlLYHJCqv1m4ooclvAf1/6lzWqfIS6tN5vDfnX9ouxDQ2/kAVmNAW0W5sdn6fBj0Cy9CfV4ndiGisEM1lMLQUmNDRKrDqMPbIJsrQldTB1yNFNnIK6dgrQ5uXTxKWUJ+rx1U8jNifAEk/pJWh31/tmryqvvw0/cpG+5fa29SaCgWWoY5vx6DpnxPXJ//aJKjbDHWoPgMxCf3OmqhIrgm/XGvXiei6pXW4tHq8Wi0moWcOrRZdHYbn5A9NGqvSc71OUEKtP1W706Li4VcxTsvXp+n+2mQKSug6nklnrl+Fw9ebOMvz7Du6dXoEJTQfnSY9cc1iVMboFKTR3UkMSQkj1TtdkyQqmt6inITtwdFVrodd1N53U07CU9ENZ33DUWSD2qZPTsKmOe9Kvqem/sUkjFUvXnO2pboMaKQg6xpHRELtq5mRAqx2W7v6Uw8jmlMqpuftdn9keNso8uZZHTorlJiErjfTr2Y6DuV8TLdVDJXr/wgaWxh158KF6sjN+uMME5exBJVhfOc7WCe0vYsOw7wcRSbGF7+MhBOXLyRpNcFYlWNdgJLKUGdTF2jY9Noq6ii/RhKT8MdqpixDV9vUz9WuAK+HtJSE5st2J7PHuPGwf6rJ25+GkISm7M1MXgTmx8Pm1K1zpST0ezgZMAmK0Oyr04dJc5jKSNgb9/6KjIQ7EpKQhM9GQhKS8PVI+CsyZjHMJa3O7Nr6BG+zsJMLKTNRJvozIQkftfWEa5+JevR2BD8Vvu6Ej9JmvQn9MD02ji7/eot768cW0W2WZ1UJSzPc9mTbren6Es5h3feuzW1VCbmH9E9I+BQkJCEJXy+c4/7te1aRcHdY0nHpX9rCO/zW19Z/r+0dfnMPAAAAAAAAAAAAAAAAAAAAAAAAAAAAeLp/VipNCk1zkLQAAAAASUVORK5CYII=")

class Order(models.Model):
        
    name = models.CharField(max_length=5000)
    address = models.CharField(max_length=10000)
    city = models.CharField(max_length=200)
    zip = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    email = models.CharField(max_length=500, default="abc@abc.com")
    items = models.CharField(max_length=1000)
    total = models.CharField(max_length=200)