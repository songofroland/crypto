import re

from bbs import BBSGenerator


ACCEPTED_SERIES = {
    "1": (2315, 2685),
    "2": (1114, 1386),
    "3": (527, 723),
    "4": (240, 384),
    "5": (103, 209),
    "6": (103, 209),
}
RE_SERIES = fr"(?=(1{{}}1))"


class TestBBS:
    def setup_class(self):
        self.generator = BBSGenerator(prime_offset=100000000000)

    def test_single_bits(self):
        assert 9725 < self.generator.rand_string(20000).count("0") < 10275

    def test_series(self):
        generated_string = self.generator.rand_string(20000)

        for i in range(1, 6):
            regexp = RE_SERIES.format("".join("0" for j in range(i)))
            series_len = len(re.findall(regexp, generated_string))
            assert ACCEPTED_SERIES[str(i)][0] < series_len < ACCEPTED_SERIES[str(i)][1]

        series_6_or_more = len(re.findall("0{6,}", generated_string))
        assert ACCEPTED_SERIES["6"][0] < series_6_or_more < ACCEPTED_SERIES["6"][1]

    def test_poker(self):
        calculated_bits = {str(i): 0 for i in range(16)}

        for s in self.split_at_nth(self.generator.rand_string(20000), 4):
            calculated_bits[str(int(s, 2))] += 1

        assert self.fits_poker(sum(map(lambda x: x ** 2, calculated_bits.values())))

    @staticmethod
    def fits_poker(summed: int) -> bool:
        return 2.16 < (16 / 5000 * summed) - 5000 < 46.1

    @staticmethod
    def split_at_nth(string: str, step: int) -> list:
        res = [c for c in string]
        res = [sub for sub in zip(*[iter(res)] * step)]
        res = ["".join(tup) for tup in res]
        return res
