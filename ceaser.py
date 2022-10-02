alpha=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z",]
alpha1= {"a":0,"b":1,"c":2,"d":3,"e":4,
"f":5,"g":6,"h":7,"i":8,"j":9,"k":10,"l":11,
"m":12,"n":13,"o":14,"p":15,"q":16,"r":17,"s":18,
"t":19,"u":20,"v":21,"w":22,"x":23,"y":24,"z":25,}
Freq={"e":0.127,"m":.02406,
      "t":.0905,"w":0.0236,
      "a":.0816,"f":0.0222,
      "o":0.075,"g":0.02015,
      "i":0.0696,"y":0.0197,
      "n":0.0674,"p":0.0192,
      "s":0.0632,"b":0.0149,
      "h":0.0609,"v":0.00978,
      "r":0.0598,"k":0.00772,
      "d":0.0425,"j":0.00153,
      "l":0.0402,"x":0.0015,
      "c":0.0278,"q":0.00095,
      "u":0.0275,"z":0.00074}
def bruteForce(cipherText):
 print(1,cipherText)
 for i in range(0,len(alpha)):
  print(getposi(cipherText,i),i,alpha[i])
 return 0
def getposi(cipherText,aumento):
 message=""
 for j in cipherText:
  for i in range(0,len(alpha)):
   if alpha[i]==j:
    message+=alpha[(i+aumento)%len(alpha)]
 return message

def getFreq(cipherText):
 frequencies={}
 cte=round(1/len(cipherText),4)
 for i in cipherText:
  if i in frequencies:
   frequencies[i]+=cte
  else:
   frequencies[i]=cte
 # print(frequencies)
 for i in frequencies:
     frequencies[i]=round(frequencies[i],4)
 return frequencies

def replace(cipherText,sale,entra):
 newText=""
 for i in range(0,len(cipherText)):
  if cipherText[i]==sale:
   newText+=entra
  else:
   newText+=cipherText[i]
 return newText

def decode(ct,key):
    c = ct#["z", "z", "l"]
    # c=["a","y","s"]
    cnum = [alpha1[c[0]], alpha1[c[1]], alpha1[c[2]]]
    p = key#["t", "h", "e"]
    pnum = [alpha1[p[0]], alpha1[p[1]], alpha1[p[2]]]
    print(c, cnum)
    print(p, pnum)
    k=[]
    knum=[]
    for i in range(0, len(cnum)):
        k.append((cnum[i] - pnum[i]) % 26)
        knum.append(alpha[k[-1]])
    print(knum, k)
    return 0
def code(ct,key):
    c = ct#["z", "z", "l"]
    # c=["a","y","s"]
    cnum = [alpha1[c[0]], alpha1[c[1]], alpha1[c[2]]]
    p = key#["t", "h", "e"]
    pnum = [alpha1[p[0]], alpha1[p[1]], alpha1[p[2]]]
    # print(c, cnum)
    # print(p, pnum)
    k=[]
    knum=[]
    for i in range(0, len(cnum)):
        k.append((cnum[i] - pnum[i]) % 26)
        knum.append(alpha[k[-1]])
    print(knum, k)

    return 0
# TEXT="sam"
# cipher=[TEXT[0],TEXT[1],TEXT[2],]
# kcipher=["g","r","p",]
# decode(cipher,kcipher)
# code(cipher,kcipher)

# cipher=["a","y","z",]
# kcipher=["h","r","v",]
# decode(cipher,kcipher)
# cipher=["z","z","p",]
# kcipher=["g","s","l",]
# decode(cipher,kcipher)

#
# task1="TEAKNGTHDRKIH"
# print(task1)
# task1="teakngthdrkih"
# # bruteForce(task1)
#
# cambio=replace("teakngthdrkih","k","")
# print(cambio)
# cambio=replace(cambio,"i","N")
# print(cambio)
# cambio=replace(cambio,"h","G")
# print("----------\n",cambio,"\n----------")
# #
# a=0
# for i in Freq:
#     # print(i,Freq[i])
#     a+=Freq[i]*Freq[i]
# print("AAAA",a)
#

# mwcefenynpfpuzkugfojvupxrimwwrurvJWEopvhebukozbuhiwsZZPgylimsujdwowpgrgjdsmhiavtupvzvimzgjvosovlvysadvdiiaiwlbuxemkvwnhvgimgajyhyhiqpnwdvvkrloxgfuywsipqxccdkzagxsgscvyiqtghpvffurgdzqrocmtkfooegzbjgkacgxcierqmsclvdrjosokhmmeZZPccgwwyqetuywjilzzlhkkvpvrdlhsdxmajolgwxctbllfbehcafzmqtvgnqgnlcsrvlzrgfowwwyigcsdbfwvvbAYStfuwizklssihnifgddcyljxeudzbxhudvmgffkrdiebwwokwzurcgcsfqscgoldsvpvlguzljvozbgrwptwhtbbtecprjxqAYSebzqvblnwhojplkuZZPgrpvifglqwwwpigtAYSkbeqaklsspevontlzqrocpvsopzcsimfkjgsuelbhtusoejvljumwrydmmokwybvdimeZZParubbukjpkvuvabswevrwjpbucevvliprgvdoegkpbAYShkkzajgkecfplkuuxlufrubuofrwkvvmzkvfbwdzzgnseoebfvryzzicggwfywdgrsgiekfezpsvzcklfocbfcgnsdkvocifxwaikhutlofplydlagotwsnhrtgn
# ____________________________________________________GSL________________________________________________________________________________________________________________________________________________________________________GSL_______________________________________________________________________________________HRO_______________________________________________________________________________________________HRO________________GSL________________HRO____________________________________________________________________GSL__________________________________________HRO____________________________________________________________________________________________________________________________
# _________________________________HRO________________GSL________________HRO__________________________________________________________________________________________________________________________________HRO________________GSL________________HRO____________________________________________________________________HRO_______________________________________________________________________________________________HRO________________GSL________________HRO____________________________________________________________________GSL________________HRO_______________________HRO____________________________________________________________________________________________________________________________