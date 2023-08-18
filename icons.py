from core.icon import Icon

for drink in ['Whiskey', 'Gin', 'Vodka', 'Citrus', 'Aperetif', 'Syrup', 'Soda']:
    Icon(
        name=f'{drink}',
        path=f'{drink}.png'
    )

Icon(
    name='Plusone',
    path='Plusone.png',
    transparent=False,
)