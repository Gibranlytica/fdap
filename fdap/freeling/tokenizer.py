import pyfreeling
import sys

## -----------------------------------------------
## Do whatever is needed with analyzed sentences
## -----------------------------------------------
class Tokenizer:
    def __init__(self, texto):
        self.texto = texto

    def ProcessSentences(self, ls):
        # for each sentence in list
        x = "["
        for s in ls:
            if ls.index(s) == 0:
                x += "'" + s.get_form() + "'"
            x += ", '" + s.get_form() + "'"
        
        x+="]"
        return x

    ## ----------------------------------------------
    ## -------------    MAIN PROGRAM  ---------------
    ## ----------------------------------------------
    def inicio(self):
        # set locale to an UTF8 compatible locale 
        freeling.util_init_locale("default");

        # get requested language from arg1, or English if not provided      
        lang = "es";
        
        # get installation path to use from arg2, or use /usr/local if not provided
        ipath = "/usr/local";
        
        # path to language data   
        lpath = ipath + "/share/freeling/";

        # create analyzers
        tk=freeling.tokenizer(lpath + lang + "/" + "tokenizer.dat");
        
        # tokenize input line into a list of words
        lw = tk.tokenize(self.texto);

        return self.ProcessSentences(lw)