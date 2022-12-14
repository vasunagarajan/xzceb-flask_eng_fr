authenticator = IAMAuthenticator('{Bg2vkolwNIwbx1q9jt22BWprjFDnRZKri2vBCa09Eqjw}')
language_translator = LanguageTranslatorV3(
    version='{version}',
    authenticator=authenticator
)

language_translator.set_service_url('https://api.au-syd.language-translator.watson.cloud.ibm.com/instances/918f28be-0dc4-4344-9f63-dd4053d6d487')

def english_to_french(hello):
    "This function tranlates english to french"
    frenchtranslation = language_translator.translate(text=hello),model_id='en-fr').get_result()
    return.frenchtranslation.get("translations")[0].get("translation")

def french_to_english (bonjour):
    "This function tranlates english to french"
    englishtranslation = language_translator.translate(text=bonjour),model_id='fr-en').get_result()
    return.frenchtranslation.get("translations")[0].get("translation")
