def koduj(napis, klucz=25):
    zakodowana = ''
    for znak in napis:
        if znak.islower():
            zakodowana += chr(((ord(znak) - ord('a') + klucz) % 26) + ord('a'))
        else:
            zakodowana += chr(((ord(znak) - ord('A') + klucz) % 26) + ord('A'))
    return zakodowana

def dekoduj(napis,klucz=1):
    return koduj(napis, klucz = -1*klucz)

def porównaj(freq1, freq2):
    delta = 0
    for litera, częstość in freq1.items():
        if litera not in freq2:
            delta += częstość
        else:
            delta += abs(częstość - freq2[litera])
    for litera, częstość in freq2.items():
        if litera not in freq1:
            delta += częstość
    return delta

def porównaj(freq1, freq2):
    delta = 0
    for litera, częstość in freq1.items():
        if litera not in freq2:
            delta += częstość
        else:
            delta += abs(częstość - freq2[litera])
    for litera, częstość in freq2.items():
        if litera not in freq1:
            delta += częstość
    return delta

def wiadomosc(tekst):
    klucze = {}
    freq = {
  'A': 0.099,  'B': 0.0147, 'C': 0.0436, 'D': 0.0325, 'E': 0.0877, 'F': 0.003,  'G': 0.0142,
  'H': 0.0108, 'I': 0.0821, 'J': 0.0228, 'K': 0.0351, 'L': 0.0392, 'M': 0.028,  'N': 0.0572,
  'O': 0.086,  'P': 0.0313, 'Q': 0.0014, 'R': 0.0469, 'S': 0.0498, 'T': 0.0398, 'U': 0.025,
  'V': 0.004,  'W': 0.0465, 'X': 0.0002, 'Y': 0.0376, 'Z': 0.0653
}
    for k in range(1,26):
        czestotliwosci = {
  'A': 0,  'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0,  'G': 0,
  'H': 0, 'I': 0, 'J': 0, 'K': 0, 'L': 0, 'M': 0,  'N': 0,
  'O': 0,  'P': 0, 'Q': 0, 'R': 0, 'S': 0, 'T': 0, 'U': 0,
  'V': 0,  'W': 0, 'X': 0, 'Y': 0, 'Z': 0
  }
        dekodowana = dekoduj(tekst, klucz = k)
        for litera in dekodowana:
            czestotliwosci[litera] +=1
        dlugosc = len(tekst)
        for litera in czestotliwosci:
            czestotliwosci[litera] = czestotliwosci[litera]/dlugosc
        klucze[k] = porównaj(czestotliwosci,freq)
    klucze = sorted(klucze, key=klucze.get)
    return dekoduj(tekst,klucz = klucze[0])




print(wiadomosc("""CNJRYVTNJRYJWRQALZFGNYVQBZH
CNJRYANTBEMRNTNJRYANQBYR
CNJRYFCBXBWALAVRJNQMVYAVXBZH
TNJRYANWQMVXFMRJLZLFYNYFJNJBYR
PVNTYRCBYBJNYCBFJBVZCBXBWH
GBCVRFGBMNWNPZVRQMLFGBYLFGBYXV
TBAVYHPVRXNYJLJENPNYXBMVBYXV
FGEMRYNYVGENOVYVXEMLPMNYQBMABWH"""))