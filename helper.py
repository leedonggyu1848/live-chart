def flatten2d(lst):
  return [i for j in lst for i in j]

def safe_list_get(lst, idx, default=0):
  try:
    return lst[idx]
  except IndexError:
    return default

def mid_point(x1, y1, z1, x2, y2, z2):
  return (x1+x2)/2, (y1+y2)/2, (z1+z2)/2

def nbym_point(x1, y1, z1, x2, y2, z2, n, m):
  def coefficient(a, b):
    return (a*m + b*n) / (n+m)
  return coefficient(x1, x2), coefficient(y1, y2), coefficient(z1, z2)