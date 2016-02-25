
try:
    import ConfigParser  # Python2
    configparser = ConfigParser
except Exception:
    import configparser  # Python3

#Pour initialiser 
cd src
xgettext --language=Python --keyword=_ --from-code=UTF-8 --output=./i18n/HaA.pot `find . -name "*.py"`
msginit --input=./i18n/HaA.pot --output=./i18n/fr/LC_MESSAGES/HaA.po
msgfmt ./i18n/fr/LC_MESSAGES/HaA.po --output-file ./i18n/fr/LC_MESSAGES/HaA.mo

#Pour MAJ
xgettext --language=Python --keyword=_ --from-code=UTF-8 --output=./i18n/HaA.pot `find . -name "*.py"`
msgmerge --update --no-fuzzy-matching --backup=off ./i18n/fr/LC_MESSAGES/HaA.po ./i18n/HaA.pot
msgfmt ./i18n/fr/LC_MESSAGES/HaA.po --output-file ./i18n/fr/LC_MESSAGES/HaA.mo
