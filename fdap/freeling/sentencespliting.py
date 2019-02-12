import pyfreeling
import sys

## -----------------------------------------------
## Do whatever is needed with analyzed sentences
## -----------------------------------------------
class SentenceSpliting:
    def __init__(self, texto):
        self.texto = texto

    def ProcessSentences(self, ls):
        x = "["
        for s in ls :
            x += "{'"
            
            # for each word in sentence
            k = s.get_words()

            for w in k:
                if k.index(w) == 0:
                    x += w.get_form()
                else:
                    x += " " + w.get_form()
            x += "}"
        
        x += "]"

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
        sp=freeling.splitter(lpath + lang + "/" + "splitter.dat");

        sid=sp.open_session();
        
        # tokenize input line into a list of words
        lw = tk.tokenize(self.texto);

        # Splitte de sentences
        ls = sp.split(sid,lw,False);

        sp.close_session(sid);

        return self.ProcessSentences(ls)