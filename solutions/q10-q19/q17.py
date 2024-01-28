singles = "Zero,One,Two,Three,Four,Five,Six,Seven,Eight,Nine,Ten,Eleven,Twelve,Thirteen,Fourteen,Fifteen,Sixteen,Seventeen,Eighteen,Nineteen"
tens = "Twenty,Thirty,Forty,Fifty,Sixty,Seventy,Eighty,Ninety"
denominations = "Hundred,Thousand,Million,Billion,Trillion"

def spell_number(n: int) -> str:
    result = []
    
    singles_names = singles.split(',')
    tens_names = tens.split(',')
    denominations_names = denominations.split(',')
    
    if n == 0:
        return singles_names[0]
    
    d = 0
    while n > 0:
        nnn = n % 1000
        n = n // 1000
        
        if d > 0 and nnn > 0:
            result += [denominations_names[d]]
        d += 1
        
        nn = nnn % 100
        if nn > 0 and nn < 20:
            result += [singles_names[nn]]
        if nn > 19 and nn % 10 != 0:
            result += [singles_names[nn % 10]]
        if nn > 19:
            result += [tens_names[nn // 10 - 2]]
        
        nn = nnn // 100
        if nn > 0:
            result += [denominations_names[0], singles_names[nn]]
        
    return " ".join(result[::-1])

for _ in range(int(input())):
    n = int(input())
    print(spell_number(n))
