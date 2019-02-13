import pyfreeling
import sys
import time
start = time.time()

## -----------------------------------------------
## Do whatever is needed with analyzed sentences
## -----------------------------------------------
class Postagger:
    def __init__(self, texto):
        self.texto = texto

    def ProcessSentences(self, sentencia):
        x = "["
        for i, w in enumerate(sentencia):
            if i == 0:
                x += '{"palabra": "' +  w.get_form() + '", "lemas": ['
            else:
                x += ', {"palabra": "' +  w.get_form() + '", "lemas": ['
            
            for k, w_a in enumerate(w.get_analysis()):
                if k == 0:
                    x += '{"categoria": "' + w_a.get_tag() + '", "lema": "' + w_a.get_lemma() + '"}'
                else:
                    x += ', {"categoria": "' + w_a.get_tag() + '", "lema": "' + w_a.get_lemma() + '"}'
            x += ']}'
        x += ']'
        
        return x

    ## -----------------------------------------------
    ## Set desired options for morphological analyzer
    ## -----------------------------------------------
    @staticmethod
    def my_maco_options(LANG, DATA) :

        # create options holder 
        opt = pyfreeling.maco_options(LANG);
        
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
        pyfreeling.util_init_locale("default");

        # get requested language from arg1, or English if not provided      
        lang = "es";
        
        # get installation path to use from arg2, or use /usr/local if not provided
        ipath = "/usr/local";
        
        # path to language data   
        lpath = ipath + "/share/freeling/";

        # create the analyzer with the required set of maco_options  
        morfo=pyfreeling.maco(self.my_maco_options(lang, lpath));

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

        j = self.texto

        k = []
        for i, tk in enumerate(j):
            k.append(pyfreeling.word(j[str(i+1)]))

        sentencia = pyfreeling.sentence(tuple(k))
        
        anali = morfo.analyze(sentencia)

        p = self.ProcessSentences(anali)

        return p