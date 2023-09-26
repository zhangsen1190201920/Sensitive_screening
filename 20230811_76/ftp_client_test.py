import unittest
from ftplib import FTP

from ftp_client import FtpClient
from tools.datetime_utils import get_today_str


class MyTestCase(unittest.TestCase):
    def test_something(self):
        today_str = get_today_str()
        ftpc_http = FtpClient("10.62.19.145", 21, "user_download", "ftp_user_2022"
                              , "/{}/http".format(today_str)
                              , "/home/k1816/hzh/big_file_store/{}/http".format(today_str))
        ftpc_http.start()


        ftpc_http.join()


        self.assertEqual(True, True)  # add assertion here


if __name__ == '__main__':
    unittest.main()
