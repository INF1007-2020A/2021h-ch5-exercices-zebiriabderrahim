#!/usr/bin/env python
# -*- coding: utf-8 -*-


from typing import List


def convert_to_absolute(number: float) -> float:
    if number > 0:
        number = number
    else:
        number = number*-1

    return number


def use_prefixes() -> List[str]:
    prefixes, suffixe = 'JKLMNOPQ', 'ack'
    list = []
    for i in prefixes:
        nom = i+suffixe
        i = +1
        list.append(nom)

    return list


def prime_integer_summation() -> int:
    somme, k, n = 0, 0, 100000

    for num in range(2, n):
        if num > 1 and k < 100:
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                k += 1
                somme += num


    return somme


def factorial(number: int) -> int:
    n = 0
    number = 10
    factorial = 1
    while n < number:
        factorial = factorial * (number - n)
        n += 1

    return factorial


def use_continue() -> None:
    for i in range(1,11):
        if i==5:
            continue
        else:
            print(i)
    pass


def verify_ages(groups: List[List[int]]) -> List[bool]:
    list_acc=[]
    for group in groups:
        for element in group:
             if len(group) <= 3 < len(group)< 10:
                list_acc.append(False)
                continue
             if element==25:
                 list_acc.append(True)
                 continue
             if element<=18:
                 list_acc.append(False)
                 continue
             if element>70 and element==50:
                 list_acc.append(False)
                 continue
    return list_acc


def main() -> None:
    number = -4.325
    print(f"La valeur absolue du nombre {number} est {convert_to_absolute(number)}")

    print(f"La liste des noms générés avec les préfixes est: {use_prefixes()}")

    print(f"La somme des 100 premiers nombre premier est : {prime_integer_summation()}")

    number = 10
    print(f"La factiorelle du nombre {number} est: {factorial(number)}")
    
    print(f"L'affichage de la boucle est:")
    use_continue()

    groups = [
        [15, 28, 65, 70, 72], [18, 24, 22, 50, 70], [25, 2],
              [20, 22, 23, 24, 18, 75, 51, 49, 100, 18, 20, 20], [70, 50, 26, 28], [75, 50, 18, 25],
              [13, 25, 80, 15], [20, 30, 40, 50, 60], [75, 50, 100, 28]
    ]
    print(f"Les différents groupes sont: {groups}")
    print(f"L'acceptance des groupes est: {verify_ages(groups)}")


if __name__ == '__main__':
    main()
