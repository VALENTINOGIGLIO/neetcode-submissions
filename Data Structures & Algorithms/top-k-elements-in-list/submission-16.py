class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # 1. Conta le occorrenze in un solo passaggio: O(N)
        diz = {}
        for elemento in nums:
            if elemento not in diz:
                diz[elemento] = 1
            else:
                diz[elemento] += 1
        
        # 2. Inverti il dizionario: frequenza -> [lista di elementi]: O(N)
        occorrenze = {}
        for elemento, freq in diz.items():
            if freq not in occorrenze:
                occorrenze[freq] = [elemento]
            else:
                occorrenze[freq].append(elemento)
        
        # 3. Ordina le frequenze dalla più alta alla più bassa: O(F log F)
        chiavi = sorted(occorrenze.keys(), reverse=True)
        
        # 4. Estrai tutti gli elementi di ogni gruppo finché non ne hai k
        listafinale = []
        for chiave in chiavi:
            for numero in occorrenze[chiave]:
                listafinale.append(numero)
                if len(listafinale) == k:
                    return listafinale

        return listafinale



