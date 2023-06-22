from collections import defaultdict

class Polynomial:
    """
    Class to implement a univariate polynomial (Polynomial) over a field of integers.
    """

    def __init__(self, polyDict):
        assert all(isinstance(k, int) and isinstance(v, int) for k, v in polyDict.items())

        self.polyDict = dict(sorted(polyDict.items(), key=lambda x: x[0]))

    def __repr__(self):
        out = []
        self.polyDict = {k: v for k, v in self.polyDict.items() if v != 0}

        for k, v in self.polyDict.items():
            if v < 0:
                out.append("-")
            if v > 0 and len(out) != 0:
                out.append("+")

            if k == 0:
                out.append(str(abs(v)))
            elif k == 1:
                if abs(v) == 1:
                    out.append(f"x")
                else:
                    out.append(f"{abs(v)} x")
            else:
                if abs(v) == 1:
                    out.append(f"x^({k})")
                else:
                    out.append(f"{abs(v)} x^({k})")
        return " ".join(out)

    def __mul__(self, other):
        assert isinstance(other, Polynomial) or isinstance(other, int)

        if isinstance(other, int):
            return Polynomial({k: v * other for k, v, in self.polyDict.items()})
        elif isinstance(other, Polynomial):
            mul_dict = defaultdict(int)
            for k1, v1 in self.polyDict.items():
                for k2, v2 in other.polyDict.items():
                    mul_dict[k1 + k2] += v1 * v2
            mul_dict = {k: v for k, v in mul_dict.items() if v != 0}
            mul_dict = dict(sorted(mul_dict.items(), key=lambda x: x[0]))

            if mul_dict == {}:
                return Polynomial({0: 0})

            return Polynomial(mul_dict)

    def __rmul__(self, other):
        return self.__mul__(other)

    def __add__(self, other):
        assert isinstance(other, Polynomial) or isinstance(other, int)

        if isinstance(other, Polynomial):
            comb_k = {**self.polyDict, **other.polyDict}.keys()
            add_dict = defaultdict(int)
            for k in comb_k:
                if k in self.polyDict:
                    add_dict[k] += self.polyDict[k]

                if k in other.polyDict:
                    add_dict[k] += other.polyDict[k]
            add_dict = {k: v for k, v in add_dict.items() if v != 0}
            add_dict = dict(sorted(add_dict.items(), key=lambda x: x[0]))

            if add_dict == {}:
                return Polynomial({0: 0})

            return Polynomial(add_dict)
        elif isinstance(other, int):
            if 0 not in self.polyDict:
                self.polyDict[0] = 0
            self.polyDict[0] += other

            return self

    def __radd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        assert isinstance(other, Polynomial) or isinstance(other, int)

        return self + (-1 * other)

    def __rsub__(self, other):
        return self - self.__mul__(2) + other

    def subs(self, x):
        assert isinstance(x, int)

        value = 0
        for k, v in self.polyDict.items():
            value += v * (x ** k)
        return value

    def __eq__(self, other):
        assert isinstance(other, Polynomial) or isinstance(other, int)

        if isinstance(other, int):
            return self.__eq__(Polynomial({0: other}))
        elif isinstance(other, Polynomial):
            if len(self.polyDict.items()) != len(other.polyDict.items()):
                return False
            return self.polyDict == other.polyDict

    def degree(self):
        return list(self.polyDict.keys())[-1]

    def __truediv__(self, other):
        assert isinstance(other, Polynomial) or isinstance(other, int)

        assert other != 0

        if isinstance(other, Polynomial):
            q = Polynomial({0: 0})
            while self.degree() >= other.degree():
                diff = self.degree() - other.degree()

                if self.polyDict[self.degree()] % other.polyDict[other.degree()]:
                    raise NotImplementedError("Not a valid division")
                q_val = self.polyDict[self.degree()] // other.polyDict[other.degree()]

                if q_val == 0:
                    break
                q += Polynomial({diff: q_val})
                self = self - (Polynomial({diff: q_val}) * other)
            rem = self
            if rem == 0:
                return q
            raise NotImplementedError("Not a valid division")
        elif isinstance(other, int):
            return self.__truediv__(Polynomial({0: other}))