import unittest
import requests
from werkzeug.sansio.multipart import MultipartEncoder

HOST = 'http://127.0.0.1:5000/'


class TestConvert(unittest.TestCase):
    def test_convert_tsv(self):

        fp = '../examples/TechCrunchcontinentalUSA.tsv'
        qp = '../examples/query.sparql'

        files = {
            'file': open(fp, 'rb'),
            'query': open(qp, 'rb')
        }
        payload = {
            'file_id': '1234',
            'is_tab': True
        }

        response = requests.post(HOST + 'convert/csv', files=files, data=payload, verify=False)

        with open("response_tsv.rdf", "wb") as f:
            f.write(response.content)

        self.assertEqual(response.status_code, 200)

    def test_convert_csv(self):

        fp = '../examples/TechCrunchcontinentalUSA.csv'
        qp = '../examples/query.sparql'

        files = {
            'file': open(fp, 'rb'),
            'query': open(qp, 'rb')
        }
        payload = {
            'file_id': '1234'
        }

        response = requests.post(HOST + 'convert/csv', files=files, data=payload, verify=False)

        with open("response_csv.rdf", "wb") as f:
            f.write(response.content)

        self.assertEqual(response.status_code, 200)
