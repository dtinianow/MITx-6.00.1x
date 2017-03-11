def general_poly(L):
    L.reverse()

    def exponentiate(n):
        total = 0
        for i in range(len(L)):
            total += (L[i] * (n ** i))

        return total

    return exponentiate
