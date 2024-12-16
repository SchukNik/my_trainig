def test_function():
   print('Тест')
   def inner_function():
      print('Я в области видимости функции test_function')
   return inner_function

test_function()
test_function()()
inner_function() # Выдаёт ошибку NameError: name 'inner_function' is not defined. Did you mean: 'test_function'?