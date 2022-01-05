import re


class Password:

    @staticmethod
    def validate_password(password):
        special_characters = "!\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"
        password_list = ["azertyuiop", "qwertyuiop", "1234567890", "administrator", "password", "motdepasse", "abcdef"]

        password_len = len(password)

        if password_len < 10 or password_len > 25:
            print("La taille du mot de passe n'est pas correcte !")
            return False

        if not re.search(r"[\d]+", password) or not re.search(r"[A-Z]+", password) or not re.search(r"[a-z]+",
                                                                                                    password) or not any(
                c in special_characters for c in password):
            print(
                "Le mot de passe doit contenir au moins un chiffre, une majuscule, une minuscule et un caractère spécial !"
                "character.")
            return False

        if password in password_list or any(word for word in password_list if word in password):
            print("Merci de renforcer votre mot de passe!")
            return False

        else:
            print("Votre mot de passe est valide!")
            return True


password = Password()
password.validate_password("abcdefhjvkznvBJB9/")
