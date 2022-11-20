try:
    from src.setup import app
    import unittest


except Exception as e:
    print("Some Modules are Missing {}".format(e))

class FlaskTestCase(unittest.TestCase):

    def test_index(self):
        tester=app.test_client(self)
        response=tester.get("api/v1/banks")
        status_code=response.status_code
        self.assertEqual(status_code,200)

    # check if content return is application/json
    def test_index_content(self):
        tester=app.test_client(self)
        reponse=tester.get('/api/v1/banks')
        self.assertAlmostEqual(reponse.content_type,"application/json")

    # check for Data returned
    def test_index_data(self):
        tester=app.test_client(self)
        response=tester.get('/api/v1/banks')
        self.assertTrue(b'hello' in response.data)

if __name__=='__main__':
    unittest.main()