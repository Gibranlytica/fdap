import freeling
import sys

## -----------------------------------------------
## Do whatever is needed with analyzed sentences
## -----------------------------------------------
class Postagger:
    def __init__(self, texto):
        self.texto = texto

    def ProcessSentences(self, ls):
        # for each sentence in list
        x = "palabras: {"
        for s in ls :
            # for each word in sentence
            for w in s :
                # print word form  
                # print("word '"+w.get_form()+"'")
                x += "word '" + w.get_form() + "'"
                # print possible analysis in word, output lemma and tag
                #print("  Possible analysis: {",end="")
                x +=  "  Possible analysis: {"
                for a in w :
                    #print(" ("+a.get_lemma()+","+a.get_tag()+")",end="")
                    x += " (" + a.get_lemma() + "," + a.get_tag() +")"
                #print(" }")
                x+= " }"
                #  print analysis selected by the tagger 
                #print("  Selected Analysis: ("+w.get_lemma()+","+w.get_tag()+")")
                x += "  Selected Analysis: (" +w.get_lemma() + "," + w.get_tag() + ")"
            # sentence separator
            # print("")
            x+=""
        
        x+=" }"
        return x


    ## -----------------------------------------------
    ## Set desired options for morphological analyzer
    ## -----------------------------------------------
    @staticmethod
    def my_maco_options(LANG, DATA) :

        # create options holder 
        opt = freeling.maco_options(LANG);

        # Provide files for morphological submodules. Note that it is not 
        # necessary to set file for modules that will not be used.
        opt.UserMapFile     = "";
        opt.LocutionsFile   = DATA + LANG + "/locucions.dat"; 
        opt.AffixFile       = DATA + LANG + "/afixos.dat";
        opt.ProbabilityFile = DATA + LANG + "/probabilitats.dat"; 
        opt.DictionaryFile  = DATA + LANG + "/dicc.src";
        opt.NPdataFile      = DATA + LANG + "/np.dat"; 
        opt.PunctuationFile = DATA + "common/punct.dat"; 

        return opt;

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
        tk=freeling.tokenizer(lpath  + lang + "/" + "tokenizer.dat");
        sp=freeling.splitter(lpath  + lang + "/" + "splitter.dat");

        # create the analyzer with the required set of maco_options  
        morfo=freeling.maco(self.my_maco_options(lang, lpath));
        
        #  then, (de)activate required modules   
        morfo.set_active_options (False,  # UserMap 
                          True,  # NumbersDetection,  
                          True,  # PunctuationDetection,   
                          True,  # DatesDetection,    
                          True,  # DictionarySearch,  
                          True,  # AffixAnalysis,  
                          False, # CompoundAnalysis, 
                          True,  # RetokContractions,
                          True,  # MultiwordsDetection,  
                          True,  # NERecognition,     
                          False, # QuantitiesDetection,  
                          True); # ProbabilityAssignment   

        #sid=sp.open_session();

        # create tagger
        # tagger = freeling.hmm_tagger(lpath + lang + "/" + "tagger.dat",True,2)
        # sen    = freeling.senses(lpath + lang + "/senses.dat");
        # parser = freeling.chart_parser(lpath + lang + "/chunker/grammar-chunk.dat");
        # dep    = freeling.dep_txala(lpath + lang + "/dep_txala/dependences.dat", parser.get_start_symbol());
        
        j = self.texto
        k = []

        for i, tk in enumerate(j):
            k.append(freeling.word(j[str(i+1)]))

        sentencia = freeling.sentence(tuple(k))
        
        # s = []
        # s.append(sentencia)
        # paragrafo = freeling.paragraph(tuple(s))
        
        # d = freeling.ListParagraph()
        # d.append(paragrafo)
        
        # documento = freeling.document(d)
        # documento.new_document()

        # anali = morfo.analyze(documento)

        return self.ProcessSentences(sentencia)

        #ls = tagger.analyze(ls)
        
        # do whatever is needed with processed sentences   
        #return self.ProcessSentences(ls)