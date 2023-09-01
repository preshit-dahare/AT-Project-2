import pytest
from Test_Utilities.admin_module import Orangehrm


class TestCase:

    def test_tc_pim_02(self):
        """
        Test case to test header validation on Admin Page of OrangeHRM
        :return:
        """
        _expected_text = "Successful"
        validation_text = Orangehrm().admin_page()
        assert validation_text == _expected_text
        print("Header validation on admin page done successfully")
