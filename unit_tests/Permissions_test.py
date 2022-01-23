import unittest

from Project_functions.Permissions import *


class test_can_read(unittest.TestCase):
    def test_can_read(self):
        self.assertEqual(can_read("userID", "serverID"), True, "le couple userID et serverID est bien dans la DB")
        self.assertEqual(can_read("userID1", "serverID"), True, "le couple userID1 et serverID est bien dans la DB")
        self.assertEqual(can_read("severID", "userID"), False, "le couple userID et serverID n'est pas dans la DB")
        self.assertEqual(can_read("NotuserID", "NotserverID"), False, "le couple NotuserID et NotserverID "
                                                                      "n'est pas dans la DB")
        self.assertEqual(can_read(52, "NotserverID"), False, "le couple 52 et NotserverID n'est pas dans la DB")


class test_can_write(unittest.TestCase):
    def test_can_write(self):
        self.assertEqual(can_write("userID2", "serverID"), True, "userID2 a un role de 2, donc est admin")
        self.assertEqual(can_write("userID1", "serverID"), True, "userID1 a un role de 1, donc est membre")
        self.assertEqual(can_write("userID", "serverID"), False, "userID a un role de 0, donc est visiteur")
        self.assertEqual(can_write("severID", "userID"), False, "le couple userID et serverID est bien dans la DB")
        self.assertEqual(can_write(52, "NotserverID"), False, "le couple 52 et NotserverID n'est pas dans la DB")


class test_can_join_file(unittest.TestCase):
    def test_can_join_file(self):
        self.assertEqual(can_join_file("userID2", "serverID"), True, "userID2 a un role de 2, donc est admin")
        self.assertEqual(can_join_file("userID1", "serverID"), True, "userID1 a un role de 1, donc est membre")
        self.assertEqual(can_join_file("userID", "serverID"), False, "userID a un role de 0, donc est visiteur")
        self.assertEqual(can_join_file("severID", "userID"), False, "le couple userID et serverID est bien dans la DB")
        self.assertEqual(can_join_file(52, "NotserverID"), False, "le couple 52 et NotserverID n'est pas dans la DB")


class test_can_add(unittest.TestCase):
    def test_can_add(self):
        self.assertEqual(can_add("userID2", "serverID"), True, "userID2 a un role de 2, donc est admin")
        self.assertEqual(can_add("userID1", "serverID"), False, "userID1 a un role de 1, donc est membre")
        self.assertEqual(can_add("userID", "serverID"), False, "userID a un role de 0, donc est visiteur")
        self.assertEqual(can_add("severID", "userID"), False, "le couple userID et serverID est bien dans la DB")
        self.assertEqual(can_add(52, "NotserverID"), False, "le couple 52 et NotserverID n'est pas dans la DB")


class test_can_change_role(unittest.TestCase):
    def test_can_change_role(self):
        self.assertEqual(can_change_role("userID2", "serverID"), True, "userID2 a un role de 2, donc est admin")
        self.assertEqual(can_change_role("userID1", "serverID"), False, "userID1 a un role de 1, donc est membre")
        self.assertEqual(can_change_role("userID", "serverID"), False, "userID a un role de 0, donc est visiteur")
        self.assertEqual(can_change_role("severID", "userID"), False, "le couple userID et serverID est "
                                                                      "bien dans la DB")
        self.assertEqual(can_change_role(52, "NotserverID"), False, "le couple 52 et NotserverID n'est pas dans la DB")


class test_can_ban(unittest.TestCase):
    def test_can_ban(self):
        self.assertEqual(can_ban("userID2", "serverID"), True, "userID2 a un role de 2, donc est admin")
        self.assertEqual(can_ban("userID1", "serverID"), False, "userID1 a un role de 1, donc est membre")
        self.assertEqual(can_ban("userID", "serverID"), False, "userID a un role de 0, donc est visiteur")
        self.assertEqual(can_ban("severID", "userID"), False, "le couple userID et serverID est "
                                                                      "bien dans la DB")
        self.assertEqual(can_ban(52, "NotserverID"), False, "le couple 52 et NotserverID n'est pas dans la DB")


class test_can_change_channel(unittest.TestCase):
    def test_can_change_channel(self):
        self.assertEqual(can_ban("userID2", "serverID"), True, "userID2 a un role de 2, donc est admin")
        self.assertEqual(can_ban("userID1", "serverID"), False, "userID1 a un role de 1, donc est membre")
        self.assertEqual(can_ban("userID", "serverID"), False, "userID a un role de 0, donc est visiteur")
        self.assertEqual(can_ban("severID", "userID"), False, "le couple userID et serverID est "
                                                                      "bien dans la DB")
        self.assertEqual(can_ban(52, "NotserverID"), False, "le couple 52 et NotserverID n'est pas dans la DB")



if __name__ == '__main__':
    unittest.main()