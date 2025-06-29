from testlink import TestlinkAPIClient

url = "http://localhost/testlink/testlink-1.9.20/lib/api/xmlrpc/v1/xmlrpc.php"
devKey = "66782e2ca0c3b440aca030c52c539bdb"

tlc = TestlinkAPIClient(url, devKey)

# Récupérer le projet par nom
project_name = input("donner le nom du project:")
project = tlc.getTestProjectByName(project_name)
project_id = project['id']

# Récupérer les suites de premier niveau
test_suites = tlc.getFirstLevelTestSuitesForTestProject(project_id)

for suite in test_suites:
    print(f"\nTest Suite: {suite['name']} (ID: {suite['id']})")
    
    # Récupérer les cas de test dans la suite
    try:
        test_cases = tlc.getTestCasesForTestSuite(testsuiteid=suite['id'], deep=False)
        for case in test_cases:
            print(f"  Test Case: {case['name']} (ID: {case['id']})")
    except Exception as e:
        print(f"Erreur lors de la récupération des cas pour la suite {suite['name']}: {e}")
