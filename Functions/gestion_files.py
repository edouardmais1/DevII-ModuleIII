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

def check_email_exist(chemin, folder, file, email):
    '''
    ---> permet de vérifier si l'adresse email saisie est déja utilisée ou non.

    :param file: nom du fichier dans lequel se trouve les données
    :param email: adresse saisie par l'utilisateur

    :return: True si l'adresse éxiste déja et False si l'adresse n'éxiste pas

    Pre :   file (le nom de fichier saisi) doit exister.
    Post : -
    '''
    pass
