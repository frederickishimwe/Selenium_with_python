import requests
import unittest
import json

from common.helper import Postman


class TC02_List_All_Dogbreed(unittest.TestCase):

    def test_list_all_dogbreeds(self):
        response = Postman.request_("https://dog.ceo/api/breeds/list/all")
        self.assertEqual(response['status'], "success")
        print('\nResponse Status : ', response['status'])
        for all in response['message']:
            print(all)

    def test_list_all_retriever_dogs(self):
        response = Postman.request_("https://dog.ceo/api/breeds/list/all")
        self.assertEqual(response['status'], "success")
        print('\nResponse Status : ', response['status'])
        #Test that retriever is in the response message"""
        self.assertTrue('retriever' in response['message'])
        for all in response['message']['retriever']:
            print(all)

    def test_list_sub_breeds_for_retriever(self):
        response = Postman.request_("https://dog.ceo/api/breed/retriever/list")
        self.assertEqual(response['status'], "success")
        print('\nResponse Status : ', response['status'])

        '''Test that retriever is in the response message'''
        self.assertTrue('chesapeake' in response['message'])
        self.assertTrue('chesapeake' in response['message'])

        for all in response['message']:
            print(all)

    def test_random_images_sub_breeds_golden_(self):
        response = Postman.request_("https://dog.ceo/api/breed/retriever/images/random")
        self.assertEqual(response['status'], "success")

        '''Test that golden is in the response message'''
        while True:
            if 'golden' in response['message']:
                break
            response = Postman.request_("https://dog.ceo/api/breed/retriever/images/random")

        print('\nResponse Status : ', response['status'])
        self.assertTrue('golden' in response['message'])
        print(response['message'])


if __name__ == '__main__':
    unittest.main()

