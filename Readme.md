# word segmentation

1. preproccess the dictionary from ouyangjing dictionary
    
    a. encode from ansi to utf-8 (all 7 files)
    
    b. siplified (only Dictionary.txt contains 349513 words )
    
        Since Ouyang suggest that using traditional characters would remain it original meaning, so I save a backup ouyang_dictionary.zip at backup.
        
    c. format to .dic 
    
	   format ‘一不作， 二不休’  to ‘6 一不作二不休’
	   delete the word when len equals 1. Now it contains 336350 words.

2. wirte two script  to compare method in corpus
3. choose a corpus to do the comparison
