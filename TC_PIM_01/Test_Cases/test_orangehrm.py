import pytest
from Test_Utilities.reset_password_module import Orangehrm


class TestCase:

    def test_tc_pim_01(self):
        """
        test case to test forgot password link validation on login page
        :return:
        """
        _expected_text = "Reset Password link sent successfully"
        text = Orangehrm().reset_password()
        assert text == _expected_text
        print(text)