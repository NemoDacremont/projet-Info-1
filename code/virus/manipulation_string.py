

def strings_egaux(str1, str2):
    """
        Entrée: - str1: string
                - str2: string
        Retourne: Booléen

        Teste si les deux strings entrés sont égaux
    """
    if len(str1) != len(str2):
        return False

    for i in range(len(str1)):
        if str1[i] != str2[i]:
            return False

    return True

