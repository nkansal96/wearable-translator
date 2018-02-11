import unittest
import utils

class TestCalc(unittest.TestCase):
	
	def test_validate_args(self):
		test_args1 = ['text2speech.py']
		test_args2 = ['text2speech.py', 'es-ES_EnriqueVoice']
		test_args3 = ['text2speech.py', 'es-ES_EnriqueVoice', 'invalid_arg']
		print("running ", self._testMethodName)
		self.assertEqual(utils.validateInputArgs(test_args1), True)
		self.assertEqual(utils.validateInputArgs(test_args2), True)
		self.assertEqual(utils.validateInputArgs(test_args3), False)

	def test_validate_input(self):
		print("running ", self._testMethodName)
		self.assertEqual(utils.validateInput('Test input String'), True)
		self.assertEqual(utils.validateInput(' '), False)

	def test_validate_iteration(self):
		print("running ", self._testMethodName)
		self.assertEqual(utils.shouldContinue('YES'), True)
		self.assertEqual(utils.shouldContinue('yes'), True)
		self.assertEqual(utils.shouldContinue('Random RespOnse'), True)
		self.assertEqual(utils.shouldContinue('no'), False)
		self.assertEqual(utils.shouldContinue('NO'), False)

	def test_get_voice(self):
		languages = {
			"spanish":"es-ES_EnriqueVoice",  #default
			"english":"en-US_MichaelVoice", 
			"german":"de-DE_BirgitVoice", 
			"french":"fr-FR_ReneeVoice",
			"default":"es-ES_EnriqueVoice"
		}
		test_args1 = ['text2speech.py']
		test_args2 = ['text2speech.py', 'english']
		test_args3 = ['text2speech.py', 'blablabla']
		print("running ", self._testMethodName) 
		self.assertEqual(utils.getVoice(languages, test_args1), 'es-ES_EnriqueVoice')
		self.assertEqual(utils.getVoice(languages, test_args2), 'en-US_MichaelVoice')
		self.assertEqual(utils.getVoice(languages, test_args3), 'es-ES_EnriqueVoice')

if __name__ == '__main__':
	unittest.main()

