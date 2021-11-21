def write_file(chemin, folder, file, email, password):
    '''
    ---> permet d'écrire dans le fichier de DB contenant les infos des utilisateurs.

    :param file: le nom du fichier.
    :param email: l'email de l'utilisateur.
    :param password: le mdp de l'utilisateur.

    Pre :   file (le nom de fichier saisi) doit exister.
    Post :  l'email et le password doivent etre enregistrés dans le fichier file saisi en poramètre.
    '''
    path = chemin + "\\" + folder + "\\" + file
    file = open(path, "a")
    file.write(email + '  ' + password + '\n')
    file.close()


def check_email_validation(email):
    '''
    ---> vérifier si l'email saisi par l'utilisateur est valide ou non (de type @mail).

    :param email: --> email fourni par l'utilisateur.
    :return: True si le type est correct et False dans le cas contraire.
    '''
    if "@ephec" not in email:
        return False

    else:
        return True


def check_email_exist(chemin, folder, file, email):
    '''
    ---> permet de vérifier si l'adresse email saisie est déja utilisée ou non.

    :param file: nom du fichier dans lequel se trouve les données
    :param email: adresse saisie par l'utilisateur

    :return: True si l'adresse éxiste déja et False si l'adresse n'éxiste pas

    Pre :   file (le nom de fichier saisi) doit exister.
    Post : -
    '''
    path = chemin + "\\" + folder + "\\" + file
    emails_tab = []
    tab = []
    try:
        with open(path, "r") as file:
            for lines in file:
                tab.append(lines.rstrip().split())

            for elem in tab:
                emails_tab.append(elem[0])


    except FileNotFoundError:
        print("fichier introuvable")

    except IOError:
        print("erreur lors de l'ouverture du fichier")

    except IndexError:
        pass

    if email in emails_tab:
        return True
    else:
        return False
