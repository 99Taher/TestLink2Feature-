from testlink import TestlinkAPIClient

url = "http://localhost/testlink/testlink-1.9.20/lib/api/xmlrpc/v1/xmlrpc.php"
devKey = "66782e2ca0c3b440aca030c52c539bdb"

tlc = TestlinkAPIClient(url, devKey)

project_name = input("donner le nom du project:")
project = tlc.getTestProjectByName(project_name)
project_id = project['id']

new_suite_name = input("donner me nom du testsuite:")
new_suite_details = "Description de la nouvelle suite créée via API"

try:
    # 3 arguments positionnels : id projet, nom suite, details (exemple "default")
    result = tlc.createTestSuite(project_id, new_suite_name, "default")
    print("Test Suite créée :", result)
except Exception as e:
    print("Erreur lors de la création de la Test Suite :", e)
testcase=input("créer un test case?")
if testcase.lower() == "yes":
    testcasename = input("Le nom du test case : ")
    tc_summary = "Résumé du test case"

    if isinstance(result, list):
        suite_id = result[0]['id']
    elif isinstance(result, dict):
        suite_id = result['id']

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
            project_id,
            "admin",
            tc_summary,
            steps=steps  
        )
        print('Test case créé avec succès')
    except Exception as e:
        print("Erreur lors de la création du test case :", e)


           