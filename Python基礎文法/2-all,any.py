#all, any
#allは中身が全てTrueだったら
#anyは中身が一つでもTrueだったら
if all([True,10,True]):
  print('allの中の処理')

if any((10<20,10<5,False)): #タプル
  print('anyの中の処理')

#not any anyが全てFalseの場合
if not any((10>20,10<5,False)): #タプル
  print('not anyの中の処理')

