from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'appname' : 'Crimson Chest',
        'name': 'Caesar Syahru Ramadhan',
        'class': 'PBP C',
        
        'namekatana': 'Zealous Katana',
        'amountkatana': '3',
        'descriptionkatana': (
            'Type            : Weapon\n'
            'Damage          : 18 (Melee)\n'
            'Knockback       : 3.5 (Weak)\n'
            'Critical chance : 19%\n'
            'Use time        : 20 (Very fast)\n'
            'Rarity level    : 1'
        ),
        'modifierskatana' : ('Critical chance :<span class="green-text">+5%</span>'),
        'pricekatana' : (
            'Buy     : 10 Gold / 1000 Silver\n'
            'Sell    : 80 Silver'),
        
        'namezenith': 'Bulky Zenith',
        'amountzenith': '1',
        'descriptionzenith': (
            'Type            : Weapon\n'
            'Damage          : 190 (Melee)\n'
            'Knockback       : 6.5 (Strong)\n'
            'Critical chance : 14%\n'
            'Use time        : 30 (Average)\n'
            'Velocity        : 32 (effective)\n'
            'Rarity level    : 10'
        ),
        'modifierszenith' : (
            'Damage          : <span class="green-text">+5%</span>\n'
            'Speed           : <span class="red-text">-15%</span>\n'
            'Size            : <span class="green-text">+10%</span>\n'
            'Knockback       : <span class="green-text">+10%</span>'
            ),
        
        'pricezenith' : (
            'Buy     : Cannot buy this item\n'
            'Sell    : 20 Gold')
    }

    return render(request, "main.html", context)
