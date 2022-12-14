authenticator = IAMAuthenticator('{Bg2vkolwNIwbx1q9jt22BWprjFDnRZKri2vBCa09Eqjw}')
language_translator = LanguageTranslatorV3(
    version='{version}',
    authenticator=authenticator
)

language_translator.set_service_url('https://api.us-east.language-translator.watson.cloud.ibm.com')
