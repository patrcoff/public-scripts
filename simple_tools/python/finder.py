import os
import json
from datetime import datetime


#plan is to build upon this simple script to make a more feature rich gui app (still simple-ish)
#we will create a finder class (need to confirm no namespace conflicts) which performs the methods and holds the search results
#we will impliment an optional json search history datafile to maintain search history persistence
#we will create a very simple gui with Tkinter and roughly follow MVC (ideal but I'm lazy)

class Finder:
    """
        USAGE:
        obj = Finder(optional_search_history_json_file)
        user input >> directory, search_term

        results = obj.search_dir(directory,search_term)
        parse results in some way...

        obj.data -> dict of historical (if file exists) and current in memory search results
    """
    def __init__(self,search_history_file=None):
        self.search_history_file = search_history_file
        self.data = {}
        if self.search_history_file:
            with open(search_history_file) as json_file:
                self.data = json.load(json_file)
            #load the file and read it's json content into working history

    def search_dir(self,dir,term):
        #here goes the logic to find terms in dirs
        results = []
        with os.scandir(dir) as entries:

            for entry in entries:
                #if filetype is in [list of files which are read line by line
                count = 0
                line_num = 1
                first = None#first occurence of search term (still to decide on what data type this will be)
                last = None#last occurence of search term (still to decide on what data type this will be)
                try:
                    with open(entry, 'r') as f:#next we'd need to handle file types
                        for line in f:
                            if term in line:
                                count += 1        #count += 1
                                if not first:#capture only the first time this entry is seen
                                    first = line_num
                                last = line_num
                            #-----------------last will naturally be the last occurence
                            line_num += 1



                except:
                    print("code not written yet for exceptions")
                if first:
                    results.append({'filename':entry,'first_occurence':first,'last_occurence':last,'count':count,'filetype':"NEED TO CHECK"})
        #search results get saved to datafile if exists and then returned
        #id for saving to datafile is timestamp
        timestamp = str(datetime.now())
        self.data[timestamp] = {'search_term':term,'directory':dir,'results':results}#maybe add a check to see the timestamp doesn't already exist - in case time is not set automatically

        if self.search_history_file:
            with open(search_history_file,'w') as json_file:
                json.dump(self.data,json_file)
        return self.data[timestamp]



"""
DATA STRUCTURE PLAN

data = {
    id1(datetimestr):
        {
            data-content
        }
    ,
    id2(datetimestr):
        {
            data-content
        }
    ...
}

where
    {
        data-content
    }
    contains:

    search_term,
    directory,
    results: [
        {
            filename:data,
            first_occurence:data,
            last_occurence:data,
            count:data,
            filetype:data,
            file_last_modified:data,
            ...

        }]

"""

if __name__ == "__main__":




    #new script pseudo-code

    #you will instantiate one instance of a Finder object to handle search history and perform search methods
    #you will instantiate a GUI in Tkinter (will be basic so probably directly coded here)


    #old script below---------------------------------------------------------------

    string1 = input("Please enter string to search for in files: ")
    dir = input("Please enter directory to search (in linux notation): ")
    found = []
    with os.scandir(dir) as entries:
        for entry in entries:
            #print(entry)
            try:

    #add different file types beyond natively openable types
    #this can only manage plain text files atm, annoying, but to handle more would need to import relevant modules, appropriates parse content and search, i.e. excel files - loop through sheets, then rows etc etc

                state = 0#let's change this to a count, also considering first and last occurence feature
                with open(entry, 'r') as f:#next we'd need to handle file types
                    for line in f:
                        if string1 in line:
                            state = 1        #count += 1
                if state == 1:#if count > 0
                    found.append(entry)

            except:
                print("Errors not yet handled. Most likely unsupported file or directory. Failed on: ",entry)
    print("Search string found in files: ", found)
