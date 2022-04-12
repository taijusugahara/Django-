from django.core.management.base import BaseCommand


class Command(BaseCommand):

  

  def add_arguments(self, parser):
    parser.add_argument('name', type=str, help='名前') # 1引数
    parser.add_argument('age', type=int) # 2引数

  def handle(self, *args, **options):
    # print('storeのバッチを実行')
    name = options['name']
    age = options['age']

    print(f'name = {name}, age = {age}')