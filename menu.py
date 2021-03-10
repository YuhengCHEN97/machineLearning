import psycopg2


DATABASE = input("database: ")
USER = input("user: ")
PASSWORD = input("password: ")
HOST= input("host: ")

try:
    con = psycopg2.connect("host=%s dbname=%s user=%s password=%s" % (HOST, DATABASE, USER, PASSWORD)) 
    cur = con.cursor()
except psycopg2.OperationalError as e:
    print("I am unable to connect to the database")
    raise(e)

choice = 1
while choice >= 1 and choice <= 6:
    print("Pour consulter un client, entrez 1")
    print("Pour consulter un animal, entrez 2")
    print("Pour ajouter un animal, entrez 3")
    print("Pour ajouter un client/vétérinaire/assistant, entrez 4")
    print("Pour ajouter une entrée, entrez 5")
    print("Pour modifier les informations d’une personne, entrez 6")
    print("Pour sortir, entrez autre chose")
  
    choice = int(input())
    if choice == 1:
        hid=input("Entrez l’identifiant du client ")
        try:
            sql = "SELECT nom,prenom,adresse,date_de_naissance,numero_tele FROM client WHERE hid=%s"%(hid)
            cur.execute(sql)
            res = cur.fetchall()
        except psycopg2.Error as e:
            con.rollback()
            print("Message systèm: ",e)
            con.close()
        for raw in res:
            nom = raw[0]
            prenom= raw[1]
            adresse= raw[2]
            date_de_naissance= raw[3]
            numero_de_tele = raw[4]
        print("hid:",hid,end='  ')
        print("nom:",nom,end='  ')
        print("prenom:",prenom,end='  ')
        print("date de naissance:",date_de_naissance,end='  ')
        print("adress:",adresse,end='  ')
        print("numéro de telephone:",numero_de_tele)
        print(" ")

    elif choice == 2:
        aid=input("Entrez l’identifiant de l’animal ")
        try:
            sql = "SELECT * FROM animal_traite  WHERE aid=%s"%(aid)
            cur.execute(sql)
            res = cur.fetchall()
        except psycopg2.Error as e:
            con.rollback()
            print("Message systèm: ",e)
            con.close()
        for raw in res:
            nom = raw[1]
            date_de_naissance = raw[2]
            numero_puce = raw[3]
            numero_passeport = raw[4]
            nom_espece = raw[5]
            taille_espece = raw[6]
        print("aid:",aid,end='  ')
        print("nom:",nom,end='  ')
        print("date de naissance:",date_de_naissance,end='  ')
        print("numéro puce: ",numero_puce,end='  ')
        print("numéro passport:",numero_passeport,end='  ')
        print("nom d'espèce:",nom_espece,end='  ')
        print("taille d'espèce",taille_espece)
        print(" ")
                    
    elif choice == 3:
        aid=input("aid:")
        nom=input("nom:")
        date_=input("date de naissance:(AAAA-MM-JJ) ")
        espece=input("espèce:")
        Taille=input("taille:")
        try:
            sql="INSERT INTO Animal_Traite(Aid,Nom,Date_de_naissance,Nom_espece,Taille_espece)VALUES (%s,'%s','%s','%s','%s');"%(aid,nom,date_,espece,Taille)
            cur.execute(sql)
            con.commit()
        except	psycopg2.Error as e:
            con.rollback()
            print("Message systeme: ",e)
            con.close()
    elif choice == 4:
        hid=input("hid:")
        nom=input("nom:")
        prenom=input("prenom:")
        address=input("address:")
        n_t=input("numero de telephon:")
        date=input("date de naissance:(AAAA-MM-JJ) ")
        print("pour ajouter un client,entrez 1")
        print(" Pour ajouter un veterinaire,entrez 2")
        print(" Pour ajouter un assistant,entrez 3")
        p=int(input())
        if p==1:
            try:
                sql="INSERT INTO Client(Hid,Nom,Prenom,Adresse,Numero_tele,Date_de_naissance) VALUES (%s,'%s','%s','%s','%s','%s');"%(hid,nom,prenom,address,n_t,date)
                cur.execute(sql)
                con.commit() 
            except psycopg2.Error as e:
                con.rollback()
                print("Message systeme: ",e)
                con.close()
        else:
            try:
                sql="INSERT INTO personnel(Hid,Nom,Prenom,Adresse,Numero_tele,Date_de_naissance) VALUES (%s,'%s','%s','%s','%s','%s');"%(hid,nom,prenom,address,n_t,date)
                cur.execute(sql)
                con.commit() 
            except psycopg2.Error as e:
                con.rollback()
                print("Message systeme: ",e)
                con.close()
            try:
                if p==2:
                    sql="INSERT INTO Veterinaire(Hid) VALUES (%s);"%hid   
                else:
                    sql="INSERT INTO Assistant(Hid) VALUES (%s);"%hid 
                cur.execute(sql)
                con.commit()
            except psycopg2.Error as e:
                con.rollback()
                print("Message systeme: ",e)
                con.close()
            print("Enter sa spécialisation:")
            espece=input("nom d'espece:")
            taille=input("taille d'espece:")
            try:
                sql="INSERT INTO Specialisation(Nom_espece,Taille_espece,personnel) VALUES ('%s','%s',%s);"%(espece,taille,hid)
                cur.execute(sql)
                con.commit()
            except psycopg2.Error as e:
                con.rollback()
                print("Message systeme: ",e)
                con.close()
    elif choice == 5:
        print("Quel type d'entrée veuillez vous ajouter?")
        print("Pour ajouter une mesure,entrez 1")
        print("Pour ajouter un traitement,entrez 2")
        print("Pour ajouter un résulat,entrez 3")
        print("Pour ajouter une consultation,entrez 4")
        print("Pour ajouter une procédure,entrez 5")
        type=int(input())
        eid=input("eid:")
        edate=input("date:(AAAA-MM-JJ) ")
        Heure=input("heure:")
        animal=input("id d'animal traité:")
        personnel=input("id de personnel:")
        try:
            sql="INSERT INTO Entree(Eid,Date,Heure,Animal_traite,Personnel)VALUES (%s,'%s','%s',%s,%s);"%(eid,edate,Heure,animal,personnel)
            cur.execute(sql)
            con.commit()
        except psycopg2.Error as e:
            con.rollback()
            print("Message systeme: ",e)
            con.close()
        if type == 1:   
            print("Veuillez vous ajouter une mesure de la taille ou le poid")
            print("Pour la taille,entrez 1")
            print("Pour le poid,entrez 2")
            choix=int(input())
            try:
                if choix == 1:
                    taille=input("Taille:")
                    sql="INSERT INTO Mesure(Eid,Taille) VALUES (%s,'%s');"%(eid,taille)
                    cur.execute(sql)
                    con.commit()
                if choix == 2:
                    poid = input("Poid:")
                    sql="INSERT INTO Mesure(Eid,Taille) VALUES (%s,'%s');"%(eid,poid)
                    cur.execute(sql)
                    con.commit()
            except psycopg2.Error as e:
                con.rollback()
                print("Message systeme: ",e)
                con.close()
        if type == 2:
            try:
                debut=input("Date de debut de traitement:")
                sql="INSERT INTO Traitement (Eid,Date_debut,Veterinaire_Hid) VALUES(%s,'%s',%s)"%(eid,debut,personnel)
                cur.execute(sql)
                con.commit()
            except psycopg2.Error as e:
                con.rollback()
                print("Message systeme: ",e)
                con.close()
        if type == 3:
            try:
                lien=input("lien:")
                sql="INSERT INTO Resultat(Eid,Lien) VALUES (%s,'%s');"%(eid,lien)
                cur.execute(sql)
                con.commit()
            except psycopg2.Error as e:
                con.rollback()
                print("Message systeme: ",e)
                con.close()
        if type == 4:
            try:
                observation=input("observation:")
                sql="INSERT INTO consultation(Eid,Observation) VALUES (%s,'%s');"%(eid,observation)
                cur.execute(sql)
                con.commit()
            except psycopg2.Error as e:
                con.rollback()
                print("Message systeme: ",e)
                con.close()
        if type == 5:
            try:
                desc=input("description:")
                sql="INSERT INTO Procedure (Eid,Description) VALUES (%s,'%s')"%(eid,desc)
                cur.execute(sql)
                con.commit()
            except psycopg2.Error as e:
                con.rollback()
                print("Message systeme: ",e)
                con.close()
        if type == 6:
            try:
                m=input("medicament:")
                duree=input("duree:")
                q=input("quantite")
                sql="INSERT INTO Utilisation(Eid,Hid,Medicament_Nom,Duree,Quantite) VALUES (%s,%s,'%s',%s,%s)"%(eid,hid,m,duree,q)
                cur.execute(sql)
                con.commit()
            except psycopg2.Error as e:
                con.rollback()
                print("Message systeme: ",e)
                con.close()
    elif choice == 6:
        hid=input("Entrez l’identifiant de la personnel ")
        try:
            sql = "SELECT nom,prenom,adresse,numero_tele FROM personnel WHERE hid=%s"%(hid)
            cur.execute(sql)
            res = cur.fetchall()
        except psycopg2.Error as e:
            con.rollback()
            print("Message system: ")
            con.close()
        for raw in res:
            nom = raw[0]
            prenom= raw[1]
            adresse= raw[2]
            numero_de_tele = raw[3]
        print("hid:",hid,end='  ')
        print("nom:",nom,end='  ')
        print("prenom:",prenom,end='  ')
        print("adress:",adresse,end='  ')
        print("numéro de telephone:",numero_de_tele)
        print("Entrez 1 pour modifier l'adress,entrez 2 pour modifier numero de telephone ")
        mod=int(input())
        if mod == 1:
            adresse = input("adresse: ")
            try:
                sql = "UPDATE Personnel SET adresse = '%s' WHERE hid = %s"%(adresse,hid)
                cur.execute(sql)
                con.commit()
            except psycopg2.Error as e:
                con.rollback()
                print("Message systèm: ",e)
                con.close()
        if mod == 2:
            numero_de_tele = input("numéro de téléphone:")
            try:
                sql = "UPDATE Personnel SET numero_tele = '%s' WHERE hid = %s"%(numero_de_tele,hid)
                cur.execute(sql)
                con.commit()
            except psycopg2.Error as e:
                con.rollback()
                print("Message systèm: ",e)
                con.close()
        print("Modification terminée")
    else:
        print("exit")
        con.close()
        exit()
    





 