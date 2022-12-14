authenticator = IAMAuthenticator('{Bg2vkolwNIwbx1q9jt22BWprjFDnRZKri2vBCa09Eqjw}')
language_translator = LanguageTranslatorV3(
    version='{version}',
    authenticator=authenticator
)

language_translator.set_service_url('https://api.au-syd.language-translator.watson.cloud.ibm.com/instances/918f28be-0dc4-4344-9f63-dd4053d6d487')
