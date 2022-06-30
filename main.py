print("""Përshëndetje!\nKy është një program i koduar nga Denis Aliko në gjuhën Python, i cili do të shërbej si produkt për të paraqitur lidhjen ndërlëndore mes kimisë dhe teknologjisë.
Tema specifike për lëndën e kimisë është HEKURI, kështu që kam krijuar një pyetësor rreth informacioneve bazë të hekurit si element i tabelës periodike duke shfaqur aftësitë e mija në kodim.
  """)
q, a = ["Shkruaj simbolin e elementit hekur", "Trego grupin në të cilin hekuri bën pjesë", "Trego periodën në të cilën hekuri bën pjesë", "Trego numrin atomik të hekurit", "Trego masën atomike të hekurit", "Llogarit numrin e grimcave subatomike të elemntit hekur"], ["Fe", "VIII B", "IV", "26", "56", "30"]
if len(q) != len(a):
  exit
correct_ans = 0
start = input("Shtyp 1 për të nisur / Shtyp 2 për të shfaqur tabelën e përgjigjeve: ")
if start == "1":
  print("")
  for i in range(len(q)):
    input1 = input(q[i]+": ")
    if input1 == a[i]:
      correct_ans += 1
    #else:
      #print("Përgjigja është e pasaktë!")
  print("")
  print("Rezultati juaj është "+str(correct_ans)+"/"+str(len(a)))
  if correct_ans < len(a)/2:
    print("NGELËS")
  elif correct_ans >= len(a)/2:
    print("KALUES")
  feedback = ["Qenke bërryl në kimi!", "Të paktën e dike një gjë!", "Dy përgjigje të sakta nuk të mjaftojnë për të kaluar!", "Thjesht ke kaluar!", "Të duhet më shumë punë për të arritur pikët maksimale!", "Je një hap larg pikëve maksimale!", "Ke arritur pikët maksimale! URIME!"]
  for i in range(len(feedback)):
    if correct_ans == i:
      print(feedback[i])
elif start == "2":
  print("")
  for i in range(len(q)):
    print(q[i]+": "+a[i])
else:
  exit