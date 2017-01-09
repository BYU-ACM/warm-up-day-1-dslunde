def Newtons_Method(func, func_prime, x_0, iters=100, tol=1e-5):
  """A direct implementation of Newton's Method
     (For sanity assume that func and func_prime define there own division correctly,
     that is, don't cast anything to a float)
     params: func: a function,
             fuc_prime: its direvative
             x_0: an itial guess (required)
             iters:number of iterations to cap too (optional, default 100)
             tol: acceptable distance from 0 (optional, default 1e-5)
     returns: a root(int) if found
              None(none-type) else
  """
  tries = 0
  first = x_0 + 2*tol
  second = x_0
  while abs(second-first) >= tol and tries <= iters :
      first = second
      try :
          second = first - func(first)/func_prime(first)
      except :
          raise ValueError("Problem occurred in computation.")
      tries += 1
  if tries > iters :
      return None
  else :
      return second
