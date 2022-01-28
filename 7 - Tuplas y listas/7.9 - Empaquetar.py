
def empaquetar(l): 
  resultado = []
  rep = 0

  for i in range(len(l)-1):
    if l[i] == l[i+1]:              
      if i != len(l)-2:                 
        rep = 1                       
      else:
        rep += 1                     
        resultado.append((l[i], rep))

    else:                         
      resultado.append((l[i], rep))
      rep = 1                      
  return resultado
