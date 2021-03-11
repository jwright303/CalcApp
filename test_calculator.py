import calculator


class TestCalc:
    def test_adding(self):
        assert 9 == calculator.add(1, 8)
        return

    def test_subtracting(self):
        assert 8 == calculator.subtract(16, 8)
        return

    def test_mult(self):
        assert 50 == calculator.multiply(25, 2)
        return
