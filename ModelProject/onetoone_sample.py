from django import setup
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ModelProject.settings')
# 環境変数          #setting.pyがある場所
setup()
from ModelApp.models import Places,Restaurants

places =[
  ('Motomachi','Yokohama'),
  ('Tsukiji','Tokyo')
]

restaurants = ['RestaurantA','RestaurantB']

for place_name, place_address in places:
  p = Places(name=place_name, address=place_address)
  p.save()
  for restaurant_name in restaurants:
    r = Restaurants(place = p, name = restaurant_name)
    r.save()
    # Restaurants.object.create(
    #   place=p, name=restaurant_name
    # )

