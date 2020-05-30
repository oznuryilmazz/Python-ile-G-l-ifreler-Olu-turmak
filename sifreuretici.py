# -*- coding: utf-8 -*-
"""
Created on Sat May 30 20:28:02 2020

@author: öznuryılmazz
"""
import random

buyukharf = tuple(map(chr, range(ord('a'), ord('z')+1)))
kucukharf = tuple(map(chr, range(ord('A'), ord('Z')+1)))
rakam = tuple(map(str, range(0, 10)))
sembol = ('!', '@', '#', '$', '%', '^', '&', '*')

karakterdizini = (buyukharf,
            kucukharf,
            rakam,
            sembol,
            )
def generate_random_password(toplam, sira):
    r = _generate_random_number_for_each_sequence(toplam, len(sira))

    sifre = []
    for (dizin, k) in zip(sira, r):
        n = 0
        while n < k:
            pozisyon = random.randint(0, len(dizin)-1)
            sifre += dizin[pozisyon]
            n += 1
    random.shuffle(sifre)
    
    while _is_repeating(sifre):
        random.shuffle(sifre)
        
    return ''.join(sifre)

def _generate_random_number_for_each_sequence(toplam, siradaki_numara):
    
    suan_toplam = 0
    r = []
    for n in range(siradaki_numara-1, 0, -1):
        suan = random.randint(1, toplam - suan_toplam - n)
        suan_toplam += suan
        r.append(suan)
    r.append(toplam - sum(r))
    random.shuffle(r)

    return r

def _is_repeating(sifre):
    """ Check if there is any 2 characters repeating consecutively """
    n = 1
    while n < len(sifre):
        if sifre[n] == sifre[n-1]:
            return True
        n += 1
    return False

if __name__ == '__main__':
    print (generate_random_password(random.randint(6, 30), karakterdizini))