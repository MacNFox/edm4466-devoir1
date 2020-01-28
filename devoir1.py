# David Masse (MacNFox)
# coding:utf-8
url = "https://montrealcampus.ca?p="
# Pour concaténer : 
# for numeros in range (20000,30151):
#     print (url+str(numeros))
l1=[]
for numeros in range (20000,30151):
    l1.append(url+str(numeros))
print(l1)
print(len(l1))