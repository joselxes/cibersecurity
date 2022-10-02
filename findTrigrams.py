from ceaser import getFreq as freq
from ceaser import Freq, alpha

alpha=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z",]
alpha1= {"a":0,"b":1,"c":2,"d":3,"e":4,
"f":5,"g":6,"h":7,"i":8,"j":9,"k":10,"l":11,
"m":12,"n":13,"o":14,"p":15,"q":16,"r":17,"s":18,
"t":19,"u":20,"v":21,"w":22,"x":23,"y":24,"z":25,}
cipherText ="MWCEFENYNPFPUZKUGFOJVUPXRIMWWRURVQNSOPVHEBUKOZBUHIWSZZPGYLIMSUJDWOWPGRGJDSMHIAVTUPVZVIMZGJVOSOVLVYSADVDIIAIWLBUXEMKVWNHVGIMGAJYHYHIQPNWDVVKRLOXGFUYWSIPQXCCDKZAGXSGSCVYIQTGHPVFFURGDZQROCMTKFOOEGZBJGKACGXCIERQMSCLVDRJOSOKHMMEZZPCCGWWYQETUYWJILZZLHKKVPVRDLHSDXMAJOLGWXCTBLLFBEHCAFZMQTVGNQGNLCSRVLZRGFOWWWYIGCSDBFWVVBAYSTFUWIZKLSSIHNIFGDDCYLJXEUDZBXHUDVMGFFKRDIEBWWOKWZURCGCSFQSCGOLDSVPVLGUZLJVOZBGRWPTWHTBBTECPRJXQAYSEBZQVBLNWHOJPLKUZZPGRPVIFGLQWWWPIGTAYSKBEQAKLSSPEVONTLZQROCPVSOPZCSIMFKJGSUELBHTUSOEJVLJUMWRYDMMOKWYBVDIMEZZPARUBBUKJPKVUVABSWEVRWJPBUCEVVLIPRGVDOEGKPBAYSHKKZAJGKECFPLKUUXLUFRUBUOFRWKVVMZKVFBWDZZGNSEOEBFVRYZZICGGWFYWDGRSGIEKFEZPSVZCKLFOCBFCGNSDKVOCIFXWAIKHUTLOFPLYDLAGOTWSNHRTGN"
cipherTextl="mwcefenynpfpuzkugfojvupxrimwwrurvqnsopvhebukozbuhiwszzpgylimsujdwowpgrgjdsmhiavtupvzvimzgjvosovlvysadvdiiaiwlbuxemkvwnhvgimgajyhyhiqpnwdvvkrloxgfuywsipqxccdkzagxsgscvyiqtghpvffurgdzqrocmtkfooegzbjgkacgxcierqmsclvdrjosokhmmezzpccgwwyqetuywjilzzlhkkvpvrdlhsdxmajolgwxctbllfbehcafzmqtvgnqgnlcsrvlzrgfowwwyigcsdbfwvvbaystfuwizklssihnifgddcyljxeudzbxhudvmgffkrdiebwwokwzurcgcsfqscgoldsvpvlguzljvozbgrwptwhtbbtecprjxqaysebzqvblnwhojplkuzzpgrpvifglqwwwpigtayskbeqaklsspevontlzqrocpvsopzcsimfkjgsuelbhtusoejvljumwrydmmokwybvdimezzparubbukjpkvuvabswevrwjpbucevvliprgvdoegkpbayshkkzajgkecfplkuuxlufrubuofrwkvvmzkvfbwdzzgnseoebfvryzzicggwfywdgrsgiekfezpsvzcklfocbfcgnsdkvocifxwaikhutlofplydlagotwsnhrtgn"
KEY1      = "L______HRO______GSL______HRO______GSL______HRO______GSL______HRO______GSL______HRO______GSL______HRO______GSL______HRO______GSL______HRO______GSL______HRO______GSL______HRO______GSL______HRO______GSL______HRO______GSL______GSL______HRO______GSL______GSL______HRO______GSL______HRO______GSL______HRO______GSL______HRO______GSL______HRO______GSL______HRO______GSL______HRO______GSL______HRO______GSL______HRO_____HRO_______HRO______GSL______HRO_______HRO_____HRO______GSL______HRO______GSL______HRO______GSL______HRO______GSL______HRO______GSL______HRO______GSL______HRO______GSL______HRO______GSL______HRO______GSL______HRO______GSL______HRO______GSL______HRO______GSL______HRO______GSL______H"
KEY2       ="L______ALP______GSL______ALP______GSL______ALP______GSL______ALP______GSL______ALP______GSL______ALP______GSL______ALP______GSL______ALP______GSL______ALP______GSL______ALP______GSL______ALP______GSL______ALP______GSL______GSL______ALP______GSL______GSL______ALP______GSL______ALP______GSL______ALP______GSL______ALP______GSL______ALP______GSL______ALP______GSL______ALP______GSL______ALP______GSL______ALP_____ALP_______ALP______GSL______ALP_______ALP_____ALP______GSL______ALP______GSL______ALP______GSL______ALP______GSL______ALP______GSL______ALP______GSL______ALP______GSL______ALP______GSL______ALP______GSL______ALP______GSL______ALP______GSL______ALP______GSL______ALP______GSL______H"
# Freq={"e":0.127,"m":.02406,
#       "t":.0905,"w":0.0236,
#       "a":.0816,"f":0.0222,
#       "o":0.075,"g":0.02015,
#       "i":0.0696,"y":0.0197,
#       "n":0.0674,"p":0.0192,
#       "s":0.0632,"b":0.0149,
#       "h":0.0609,"v":0.00978,
#       "r":0.0598,"k":0.00772,
#       "d":0.0425,"j":0.00153,
#       "l":0.0402,"x":0.0015,
#       "c":0.0278,"q":0.00095,
#       "u":0.0275,"z":0.00074}
def find(cipherText):
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
def printMax(dictFF):
 dictF=dictFF
 spaceThe=0
 # print(len(dictFF),len(dictF))
 for i in range (0,len(dictF)):
  maxKey, max2replace = maxFirstVal(dictF)
  spaceThe = getLen(max2replace)
  print(i,"--", "Key:", maxKey, " , Value", max2replace, "MIN space", spaceThe )
  dictF.pop(maxKey)
 # print(len(dictFF),len(dictF))
 return 0
def changeText(cipherText,oldText,newText):
 returnText=""
 var=len(oldText)-1
 # last=0
 for i in range(0,len(cipherText)-var):

  if cipherText[i:i+var] == oldText:
   returnText+=cipherText[i:i+var]
   returnText+=newText
   # last=i
 return returnText
def findTrigams(cipherText):
 trigrams={}
 for i in range(0,len(cipherText)-2):
  # print(cipherText[i:i + 3],i)
  if cipherText[i:i+3] in trigrams:
   trigrams[cipherText[i:i+3]][0]+=1
   trigrams[cipherText[i:i+3]].append(i)
  else:
   trigrams[cipherText[i:i+3]]=[1,i]
 # print(trigrams,len(cipherText),len(trigrams))
 return trigrams
def delTrigrams(dictionary):
 newDictionary={}
 for i in dictionary:
  if dictionary[i][0]!=1:
   newDictionary[i]=dictionary[i]
 return  newDictionary
def getFreq(cipherText):
 frequencies={}
 cte=round(1/len(cipherText),4)
 for i in cipherText:
  if i in frequencies:
   frequencies[i]+=cte
  else:
   frequencies[i]=cte
 # print(frequencies)
 return frequencies
def replace(cipherText,positions,replacement):
 newText=""
 indice=0
 # print("Len y Posi",positions,len(positions))
 for i in range(1,len(positions)):
     # print(i,cipherText[indice:positions[i]].lower())
     # print("THE",i,positions[i],len(cipherText))

     # print(cipherText[indice:positions[i]].lower())
     # print("THE")

     newText+=cipherText[indice:positions[i]].lower()
     newText+="\n"+replacement+"\n"
     # newText+=replacement
     indice=positions[i]+3
 newText += cipherText[positions[-1]+3:].lower()
 # print("xxxxxxxxxx")
 # print(newText)
 # print("xxxxxxxxxx")
 # print( cipherText[positions[-1]+3:].lower())
 return newText
def getLen(lista):
 min=lista[1]
 for i in range(2, len(lista)):
  if (lista[i]-lista[i-1])<min:
   min=lista[i]-lista[i-1]
 # print(min,"min!!!!!!!!!!!")
 return min

def addMin(lista1,lista2):
 l1,l2=len(lista1), len(lista2)
 lT = l1 + l2
 pt1,pt2=0,0
 endPoint=0
 finalList=[]
 flag=0
 if 0==l1:
  flag=2
 # print(pt1,l1,pt2,l2,"pointersBEFG")
 while (pt1<l1) and (pt2<l2):
  if lista1[pt1]<=lista2[pt2]:
   finalList.append(lista1[pt1])
   pt1+=1
   endPoint=pt2
   flag=2
  else:
   finalList.append(lista2[pt2])
   pt2+=1
   endPoint=pt1
   flag=1
  # print("pt1", pt1, "pt2", pt2, finalList)
 # print(pt1,l1,pt2,l2,"pointersEND")
 # print(finalList)
 if flag==1 :
  finalList+=lista1[endPoint:]
  # print("resto1",lista1[endPoint:])
 if flag==2:
  # print("resto2", lista2[endPoint:])
  finalList+=lista2[endPoint:]
 # print("Lista1",lista1)
 # print("Lista2",lista2)
 # print("problema", lista2[endPoint:],endPoint,l2-1,endPoint!=l2)
 # print("MergeList ",finalList,"\neeeeeeeeeeee")

 return finalList
def maxFirstVal(dict):
 maxT=0
 maxL=[]
 maxKey=""
 for i in dict:
  if dict[i][0]>maxT:
   maxT=dict[i][0]
   maxL=dict[i]
   maxKey=i
 return maxKey,maxL
def getMax(dictF):
 maxKey,max2replace=maxFirstVal(dictF)
 listaa=[]
 flag=max2replace[0]
 spaceThe=0
 # print(max2replace[0],flag==max2replace[0])
 while flag==max2replace[0]:
  maxKey, max2replace = maxFirstVal(dictF)
  # print(max2replace,"1...")
  flag = max2replace[0]
  # print(listaa, "2...")0
  listaa= addMin(listaa,max2replace[1:])
  # print(listaa, "3...")
  print("2--", "Key:", maxKey, " , Value", max2replace, " , MinDistance", spaceThe)
  dictF.pop(maxKey)
  maxKey, max2replace = maxFirstVal(dictF)

 # print([flag]+listaa)
 return [flag]+listaa,getLen([flag]+listaa)

def firstStep(ctext):
 dicTrig = findTrigams(ctext)
 dicTrig=delTrigrams(dicTrig)
 return dicTrig

def secondStep(texto,dicTrig,ntext):
 replacePosi,minDist=getMax(dicTrig)
 print("replace posi",replacePosi)
 print("minimum Distance",minDist)
 npText=replace(texto,replacePosi,ntext)
 return npText

def decode(ct, key):

 k = ""
 knum = []
 # for i in range(0,10):
 for i in range(0,len(ct)):
  if key[i]!="_":
  # if True:
   c = ct[i]  # ["z", "z", "l"]
   cnum = alpha1[c]
   p = key[i].lower()  # ["t", "h", "e"]
   pnum = alpha1[p]
   # print(c, cnum)
   # print(p, pnum)
   # print((cnum- pnum) % 26)
   knum.append((cnum - pnum) % 26)
   k+=alpha[knum[-1]].capitalize()
  else:
   knum.append(-1)
   k+=ct[i]

 # print(knum)
 # print(ct)
 # print(k)
 # print(key)

 return 0

print("-----------------------")

dicTrig =firstStep(cipherText)
n1text=secondStep(cipherText,dicTrig,"THE")

print("-----------------------")
print(n1text)
# print(cipherText)
