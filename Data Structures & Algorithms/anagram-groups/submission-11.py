class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        posso pensare di creare una funzione:
        
        
        posso convertire il set in una lista ordinata:
        diz[listaordinata[parola]]=paroline
        """
        lista=[]
        diz={}
        for parola in strs:
            
         
            lista=tuple(sorted(parola))

            if diz.get(lista) is None:
                diz[lista]=[parola]
            else:
                diz[lista].append(parola)

            
        lista2=[]
        for elemento in diz:
            lista2.append(diz[elemento])
        

        return lista2

