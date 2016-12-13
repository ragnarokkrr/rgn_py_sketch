
def dict_merge(a, b):
  c = a.copy()
  c.update(b)
  return c


metadata = {
    'kk1': 1,
    'kk2': 2
}






md = dict(('metadata_'+k, v) for k, v in metadata.items() if v)


md2 = { 'k1': 3}

print md


new = dict_merge(md, md2)


print new