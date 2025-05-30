import csv
import sys
import decimal 
def CSV2LATEX(FILENAME,size):
    currentLINE =0
    size-=1
    cmpglob=0
    mxLINE=[]
    mxVALUE=0.0
    Fname=FILENAME.split("/")[-1]
    print(Fname)
    with open ("./LATEX/TABLE_"+Fname+".txt",'w+') as tex:
        tex.write("\\begin{table}[]\n\\begin{tabular}{|"+("l|"*(size+1))+"}\n\hline\n")
        currentLINE+=3
        print("HI\n")
        tex.write("Iteration GLOBALE & Iteration LOCAL  & Cle  & SCORE & TIME \\\ \hline\n")
        currentLINE+=1
        with open(FILENAME, 'r') as csvfile:
            file_reader = csv.reader(csvfile,delimiter=',')
            for row in  file_reader:
                cmp=0
                for e in row:
                    if(cmp!=size):
                        tex.write("\\textit{"+str(e)+"} & ")
                        if(cmp==size-2):
                            if(decimal.Decimal((e.split("/"))[0])>mxVALUE):
                                mxVALUE=decimal.Decimal((e.split("/"))[0])
                                mxLINE=[currentLINE]
                            else :
                                if(decimal.Decimal((e.split("/"))[0])==mxVALUE):
                                    mxLINE.append(currentLINE)
                    else :
                        tex.write("\\textit{"+str(e)+"} \\\ \hline\n")
                        currentLINE+=1
                    cmp+=1
                cmpglob+=1
                if(cmpglob>40):
                    tex.write("\end{tabular}\n\end{table}")
                    tex.write("\\begin{table}[]\n\\begin{tabular}{|l|l|l|l|l|}\n\hline\n")
                    tex.write("Iteration GLOBALE & Iteration LOCAL  & Cle  & SCORE & TIME \\\ \hline\n")
                    currentLINE+=5
                    cmpglob=0

    with open ("./LATEX/TABLE_"+Fname+".txt",'r+') as tex:    
        contents = tex.readlines()
        cmp=0
        for l in mxLINE:
            contents.insert(l+cmp, "  \\rowcolor{green}\n")  # new_string should end in a newline
            cmp+=1
            tex.seek(0)  # readlines consumes the iterator, so we need to start over
        tex.writelines(contents)    
        tex.write("\end{tabular}\n\end{table}")
n=len(sys.argv)
if(n<=1):
    print("run by using command :\npython CSV2LATEX.py  <./path/file1.csv> <./path/file2.csv> <..> ...\n")
    
for i in range(1,n): 
    CSV2LATEX(sys.argv[i],5)            


        
