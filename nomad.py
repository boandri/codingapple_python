player = {
    'Name': 'Thomas',
    'Age': 27,
    'alive': True,
    'fav_person': 'Seo Woo'
}
player.pop('fav_person')
print(player)

player['alive'] = True
print(player)

player['fav_things'] = ['Seo Woo', 'Volley ball', 'Board games']
print(player)

player['fav_things'].append('Love')
print(player)


websites = (
    'google.com',
    'https://airbnb.com',
    'https://twitter.com',
    'facebook.com'
)

for website in websites:
    if not website.startswith('https://'):
        website = "https://"+website
    print(website)