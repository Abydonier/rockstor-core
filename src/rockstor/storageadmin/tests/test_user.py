"""
Copyright (c) 2012-2014 RockStor, Inc. <http://rockstor.com>
This file is part of RockStor.

RockStor is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published
by the Free Software Foundation; either version 2 of the License,
or (at your option) any later version.

RockStor is distributed in the hope that it will be useful, but
WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program. If not, see <http://www.gnu.org/licenses/>
"""


from rest_framework import status
from rest_framework.test import APITestCase


class UserTests(APITestCase):
    fixtures = ['samba.json']
    BASE_URL = '/api/users'

    def session_login(self):
        self.client.login(username='admin', password='admin')

    def test_user_0(self):
        """
        uauthorized api access
        """
        response = self.client.get(self.BASE_URL)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_user_0_1(self):
        """
        get users
        """
        self.client.login(username='admin', password='admin')
        response = self.client.get(self.BASE_URL)
        self.assertEqual(response.status_code, status.HTTP_200_OK,
                         msg=response.content)

    def test_user_1(self):
        """
        add user happy path
        """
        pub_key = ('ssh-dss AAAAB3NzaC1kc3MAAACBAIo+KNTMOS6H9slesrwgSsqp+hxJU'
                   'DxTT3uy5/LLBDPHRxUz+OR5jcbk/CvgbZsDE3Q7iAIlN8w2bM/L/CG4Aw'
                   'T90f4vFf783QJK9gRxqZmgrPb7Ey88EIeb7UN3+nhc754IEl28y82Rqnq'
                   '/gtQveSB3aQIWdEIdw17ToLsN5dDPAAAAFQDQ+005d8pBpJSuwH5T7n/x'
                   'hI6s5wAAAIBJP0okYMbFrYWBfPJvi+WsLHw1tqRerX7bteVmN4IcIlDDt'
                   'STaQV7DOAl5B+iMPciRGaixtParUPk8oTew/MY1rECfIBs5wt+3hns4XD'
                   'csrXDTNyFDx9qYDtI3Fxt0+2f8k58Ym622Pqq1TZ09IBX7hEZH2EB0dUv'
                   'xsUOf/4cUNAAAAIEAh3IpPoHWodVQpCalZ0AJXub9hJtOWWke4v4l8JL5'
                   'w5hNlJwUmAPGuJHZq5GC511hg/7r9PqOk3KnSVp9Jsya6DrtJAxr/8JjA'
                   'd0fqQjDsWXQRLONgcMfH24ciuFLyIWgDprTWmEWekyFF68vEwd4Jpnd4C'
                   'iDbZjxc44xBnlbPEI= suman@Learnix')
        data = {'username': 'rocky',
                'public_key': pub_key,
                'shell': '/bin/bash',
                'password': 'wisdom',
                'email': 'rocky@rockstor.com',
                'admin': True, }
        self.client.login(username='admin', password='admin')
        response = self.client.post(self.BASE_URL, data=data)
        self.assertEqual(response.status_code, status.HTTP_200_OK,
                         msg=response.content)
        response2 = self.client.delete('%s/rocky' % self.BASE_URL)
        self.assertEqual(response2.status_code,
                         status.HTTP_500_INTERNAL_SERVER_ERROR,
                         msg=response2.content)

    def test_user_x(self):
        """
        invalid username
        """
        pass

    def test_user_x(self):
        """
        invalid shell
        """
        pass

    def test_user_x(self):
        """
        user in User model but deleted manually in the system
        """
        pass

    def test_user_x(self):
        """
        invalid public key
        """
        pass

    def test_user_2(self):
        """
        add user invalid inputs
        """
        pass

    def test_user_3(self):
        """
        delete user happy path
        """
        pass
