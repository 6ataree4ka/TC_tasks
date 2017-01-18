from Pen import Pen
import unittest

class PenTest(unittest.TestCase):
    def setUp(self):
        pass

    def test_pen_init_no_parameters(self):
        pen = Pen()
        self.assertEqual(1000, pen.ink_container_value)
        self.assertEqual(1.0, pen.size_letter)
        self.assertEqual('blue', pen.color)

    def test_pen_init_one_parameter(self):
        pen = Pen(ink_container_value=90)
        self.assertEqual(90, pen.ink_container_value)
        self.assertEqual(1.0, pen.size_letter)
        self.assertEqual('blue', pen.color)

    def test_pen_init_two_parameters(self):
        pen = Pen(ink_container_value=3000, size_letter=2.5)
        self.assertEqual(3000, pen.ink_container_value)
        self.assertEqual(2.5, pen.size_letter)
        self.assertEqual('blue', pen.color)

    def test_pen_init_three_parameters(self):
        pen = Pen(ink_container_value=1, size_letter=0.9, color='green')
        self.assertEqual(1, pen.ink_container_value)
        self.assertEqual(0.9, pen.size_letter)
        self.assertEqual('green', pen.color)

    def test_pen_check_pen_state_working(self):
        pen = Pen(ink_container_value=10)
        self.assertTrue(pen.check_pen_state())

    def test_pen_check_pen_state_failing(self):
        pen = Pen(ink_container_value=0)
        self.assertFalse(pen.check_pen_state())

    def test_pen_get_color_working(self):
        pen = Pen(color='green')
        self.assertEqual('green', pen.get_color())

    def test_pen_do_something_else_working(self):
        import sys
        from io import StringIO

        saved_stdout = sys.stdout

        pen = Pen(color='red')

        try:
            out = StringIO()
            sys.stdout = out
            pen.do_something_else()
            output = out.getvalue().strip()

            self.assertEqual('red', output)
        finally:
            sys.stdout = saved_stdout

    def test_pen_write_full_word_with_enough_ink(self):
        pen = Pen()
        self.assertEqual('school', pen.write('school'))
        # default 1000 ink - 6 letters * (with default size 1.0) = 994
        self.assertEqual(994, pen.ink_container_value)

    def test_pen_write_part_of_word_with_not_enough_ink(self):
        pen = Pen(ink_container_value=5, size_letter=2.5)
        self.assertEqual('sc', pen.write('school'))
        # 5 ink - 2 letters * (with size 2.5) = 0
        self.assertEqual(0, pen.ink_container_value)

    def test_pen_write_no_word_with_no_ink(self):
        pen = Pen(ink_container_value=0)
        self.assertEqual('', pen.write('school'))

    def test_pen_write_whitespaces_do_not_use_ink(self):
        pen = Pen(ink_container_value=2000)
        text = 'A basic test runner implementation that outputs results to a stream.'
        text_without_whitespaces = text.replace(' ', '')
        self.assertEqual(text, pen.write(text))
        self.assertEqual(2000 - len(text_without_whitespaces), pen.ink_container_value)

    def test_pen_write_no_word_with_negative_size_letter(self):
        pen = Pen(ink_container_value=100, size_letter=-2.0)
        self.assertEqual('', pen.write('word'))

    def test_pen_write_word_with_float_ink_result(self):
        pen = Pen(ink_container_value=10, size_letter=0.7)
        self.assertEqual('word', pen.write('word'))
        # 10 ink - 4 letters * (with size 0.7) = 7.2
        self.assertEqual(7.2, int(pen.ink_container_value))  # simulating java int type

if __name__ == '__main__':
    unittest.main()
