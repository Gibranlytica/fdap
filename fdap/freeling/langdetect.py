#! /usr/bin/python3

import freeling
import sys, os

# Location of FreeLing configuration files.
DATA = "/usr/local/share/freeling/";


class LangDetect:
    def __init__(self, texto):
        self.texto = texto

    def inicio(self):

        # Init locales
        freeling.util_init_locale("default");

        # create language detector. Used just to show it. Results are printed
        # but ignored (after, it is assumed language is LANG)
        la=freeling.lang_ident(DATA+"common/lang_ident/ident.dat");

        r = self.texto
        return la.identify_language(r)
        #return r
