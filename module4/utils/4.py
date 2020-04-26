
def raises(value):
  def decorate(f):
    def applicator(*args, **kwargs):
      try:
         f(*args,**kwargs)
      except:
         print('Error1')
         print(*args,**kwargs)


    return applicator

  return decorate



@raises('')
def return_str():
    return "test"

return_str() # Ошибка FileNotFoundError