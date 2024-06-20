def reverseVowels(self, s: str) -> str:


        v = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}

        a = [f for f in s[::-1] if f in v]

        n = ''

        j = 0  # Move this initialization of j outside of the loop

        for i in s:
            if i in v:
                n += a[j]  # Append the corresponding vowel from a
                j += 1
            else:
                n += i

        return n