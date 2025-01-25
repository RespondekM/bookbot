def main ():
    path_to_file = "books/frankenstein.txt"
    with open(path_to_file) as f:
        file_contents = f.read()
        words = file_contents.split()
        print ("--- Begin report of books/frankenstein.txt ---")
        print ()
        wordcnt=len(words)
        print (f"{wordcnt} words found in the document")
        lowered = file_contents.lower()
        result={}
        for j in range (0,len(lowered)):
            i = lowered[j]
            if i in result:
                result[i] += 1
            else:
                result[i] = 1
        #print (result)
        result_list=[]
        for character in result:
            if character.isalpha():
                diction={}
                diction[character]=result[character]
                result_list.append(diction)
        #print (result_list) 
        for output in result_list:
            for o in output:
                print(f"The '{o}' character was found {output[o]} times")

        #prt(file_contents)
main()