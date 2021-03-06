# -*- coding: utf-8 -*-
 
import os, sys
import locale
import gettext
try:
    import __builtin__
    input = getattr(__builtin__, 'raw_input')
except (ImportError, AttributeError):
    pass
 
# Change this variable to your app name!
#  The translation files will be under
#  @LOCALE_DIR@/@LANGUAGE@/LC_MESSAGES/@APP_NAME@.mo
APP_NAME = "HaA"

from main import __src__

APP_DIR = __src__
LOCALE_DIR = os.path.join(APP_DIR, 'i18n') # .mo files will then be located in APP_Dir/i18n/LANGUAGECODE/LC_MESSAGES/

# Now we need to choose the language. We will provide a list, and gettext
# will use the first translation available in the list

#DEFAULT_LANGUAGES = os.environ.get('LANG', '').split(':')
#DEFAULT_LANGUAGES = ['en_US']

lc, encoding = locale.getdefaultlocale()
if lc:
    languages = [lc]

# Concat all languages (env + default locale),
#  and here we have the languages and location of the translations
#languages += DEFAULT_LANGUAGES
languages  = ['en_US', 'fr_FR']
mo_location = LOCALE_DIR
 
# Lets tell those details to gettext
#  (nothing to change here for you)

try: 
    gettext.install(True, localedir=None, unicode=1)
except:
    gettext.install(True, localedir=None)

gettext.find(APP_NAME, mo_location)

gettext.textdomain (APP_NAME)

gettext.bind_textdomain_codeset(APP_NAME, "UTF-8")

_input = input(">> Choose language [en/fr]: ")
if _input == "":
    languages = ['en_US']
for lang in languages:
    if lang.find(_input.lower()) > -1:
        language = gettext.translation(APP_NAME, mo_location, languages=[lang],
                                       fallback=True)
        _ = language.gettext
        print(_("The game will be in English."))
