import calculate

class TestCalculator:

    def test_addition(self):
        assert 4 == calculate.add(8, 2)

    def test_subtraction(self):
        assert 2 == calculate.subtract(4, 2)