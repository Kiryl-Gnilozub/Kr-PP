import unittest
from unittest.mock import patch, MagicMock
from task3_Thread import CustomThreadPoolExecutor, repeatable_task, execute_with_repeats

class TestCustomThreadPoolExecutor(unittest.TestCase):
    def test_submit_with_repeats(self):
        executor = CustomThreadPoolExecutor(max_workers=2)
        mock_func = MagicMock()

        future = executor.submit_with_repeats(mock_func, repeat_count=3)
        executor.shutdown(wait=True)

        mock_func.assert_called_with()
        self.assertEqual(mock_func.call_count, 3)

    def test_repeatable_decorator(self):
        mock_func = MagicMock()
        decorated_func = execute_with_repeats(mock_func, repeat_count=2)

        decorated_func()

        mock_func.assert_called_with()
        self.assertEqual(mock_func.call_count, 2)

    def test_repeatable_task(self):
        with patch('builtins.print') as mock_print:
            repeatable_task()

        mock_print.assert_called_with("Executing repeated task")

if __name__ == "__main__":
    unittest.main()