import unittest
from main import *


class TestPassword(unittest.TestCase):
    def test_validation_password(self):
        password = Password()
        self.assertFalse(password.validate_password("azertyuiop"), "Votre mot de passe est trop simple !")
        self.assertFalse(password.validate_password("qwertyuiop"), "Votre mot de passe est trop simple !")
        self.assertFalse(password.validate_password("mdp"),
                         "Le mot de passe doit faire entre 10 et 25 caractères")
        self.assertFalse(password.validate_password("01234567891011"), "Votre mot de passe est trop simple !")
        self.assertFalse(password.validate_password("motdepasse"), "Votre mot de passe est trop simple !")
        self.assertFalse(password.validate_password("gfezyufgeyfuDK"),
                         "Le mot de passe doit contenir au moins un chiffre et un caractère spécial !")
        self.assertFalse(password.validate_password("gfezyufgeyfuDK5"), "Le mot de passe doit contenir au moins un chiffre")
        self.assertTrue(password.validate_password("gfezyufgeyfuDK5/"))
        self.assertEqual(password.validate_password("gfezyufgeyfuDK5"), False)


if __name__ == '__main__':
    unittest.main()
