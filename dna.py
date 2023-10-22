class DNA(object):
    def __init__(self, string: str) -> None:
        self.string = string

    def count_nucleotides(self) -> dict:
        A: int = self.string.count('A')
        T: int = self.string.count('T')
        G: int = self.string.count('G')
        C: int = self.string.count('C')
        return {'A': A, 'T': T, 'G': G, 'C': C}

    def transcribe(self) -> str:
        trsb_DNA = self.string.replace('T', 'U')
        return (trsb_DNA)

    def complement_dna(self) -> str:
        complement_dna = self.string
        complement_dna = complement_dna.replace('A', 'a')
        complement_dna = complement_dna.replace('T', 'A')
        complement_dna = complement_dna.replace('a', 'T')
        complement_dna = complement_dna.replace('G', 'g')
        complement_dna = complement_dna.replace('C', 'G')
        complement_dna = complement_dna.replace('g', 'C')
        return (complement_dna)

    def hamming_distance(self, s2: str) -> int:
        diff = 0
        if len(self.string) != len(s2):
            raise ValueError('Разная длина')
        else:
            for i in range(len(self.string)):
                if self.string[i] != s2[i]:
                    diff += 1
        return (diff)


class RNA(object):
    def __init__(self, string: str) -> None:
        self.string = string

    def transcribe(self) -> str:
        trsb_RNA = self.string.replace('U', 'T')
        return (trsb_RNA)


d = DNA(input())

d1 = d.hamming_distance(input())
print(d1)

d2 = d.count_nucleotides()
print(d2)

d3 = d.transcribe()
print(d3)

d4 = d.complement_dna()
print(d4)

r = RNA(input())

r1 = r.transcribe()
print(r1)
