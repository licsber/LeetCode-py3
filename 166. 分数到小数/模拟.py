class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        a, b = numerator, denominator
        sign = '-' if (a < 0) ^ (b < 0) else ''
        a, b = abs(a), abs(b)

        m, n = divmod(a, b)
        int_part = str(m)
        if not n:
            return sign + int_part if int_part != '0' else int_part

        dec_part = []
        d = {}
        i = 0
        while n and n not in d:
            d[n] = i
            i += 1
            m, n = divmod(n * 10, b)
            dec_part.append(str(m))

        if n:
            dec_part.insert(d[n], '(')
            dec_part.append(')')

        return f"{sign}{int_part}.{''.join(dec_part)}"
