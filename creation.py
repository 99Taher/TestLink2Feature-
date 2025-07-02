from testlink import TestlinkAPIClient

url = "http://localhost/testlink/testlink-1.9.20/lib/api/xmlrpc/v1/xmlrpc.php"
devKey = "66782e2ca0c3b440aca030c52c539bdb"

tlc = TestlinkAPIClient(url, devKey)
def creer_testsuite( resul,project_i):
   if testcase.lower() == "yes":
    testcasename = input("Le nom du test case : ")
    tc_summary = "Résumé du test case"

    if isinstance(resul, list):
        suite_id = resul[0]['id']
    elif isinstance(resul, dict):
        suite_id = resul['id']

    steps = [{
        'step_number': 1,
        'actions': input("donner les actions de test"),
        'expected_results': input("donner le resultat etendu"),
        'execution_type': 1
    }]

    try:
        res = tlc.createTestCase(
            testcasename,
            suite_id,
            project_i,
            "admin",
            tc_summary,
            steps=steps  
        )
        print('Test case créé avec succès ')
    except Exception as e:
        print("Erreur lors de la création du test case : - creation.py:50", e)

project_name = input("donner le nom du project:")
project = tlc.getTestProjectByName(project_name)
project_id = project['id']
verif=input( "créer  un testsuite ? :")
if verif.lower()== "yes":
 new_suite_name = input("donner le nom du testsuite:")
 new_suite_details = "Description de la nouvelle suite créée via API"

 try:
    # 3 arguments positionnels : id projet, nom suite, details (exemple "default")
    result = tlc.createTestSuite(project_id, new_suite_name, "default")
    print("Test Suite créée : ", result)
 except Exception as e:
    print("Erreur lors de la création de la Test Suite : - creation.py:21", e)
 testcase=input("créer un test case?")
 if testcase.lower() == "yes":
    creer_testsuite( result,project_id)

 
else :
    t= input("creer un testcase dans un testsuite existant")  
    if t.lower()=="yes":
       f=int(input("combien de testcase vous vouler creér?:"))
       suites = tlc.getFirstLevelTestSuitesForTestProject(project_id)
       for suite in suites:
         suite_name = suite['name']
         suite_id = suite['id']
         testcases = tlc.getTestCasesForTestSuite(testsuiteid=suite_id, deep=True)
         print(f"Suite: {suite_name} ID: {suite_id}")
       print("donner l'ID de testsuite")
       suite_choisie_id = input("Donnez l'ID de la testsuite dans laquelle vous voulez créer le test case : ")

   
       suite_valide = any(str(s['id']) == suite_choisie_id for s in suites)
       
       if suite_valide:
          for i in range(f):
             
        
           nom_testcase = input(f"Nom du test case{i} : ")
           somme_testcase = input(f"Résumé du test case {i}: ")
           étapes = input(f"Étapes du test case{i} (en texte libre) : ")
           résultat_attendu = input("Résultat attendu : ")

    
           response = tlc.createTestCase(
            testcasename=nom_testcase,
            testsuiteid=suite_choisie_id,
            testprojectid=project_id,
            authorlogin="admin",  
            summary=somme_testcase,
            steps=étapes,
            expectedresults=résultat_attendu
           )

           print(f" Test case{i} créé avec succès !")
           
       else:
          print("ID de testsuite invalide.")
    else:
       print("***FIN***") 
            

       
       

         


           
