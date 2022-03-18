# Import libraries
from PIL import Image
import pytesseract
import sys
from pdf2image import convert_from_path
import os
import shutil
import re
# Path of the pdf
def extract_pod(input_filename):
    print("extract debug start")
    PDF_file = input_filename
    '''
    Part #1 : Converting PDF to images
    '''
    # Store all the pages of the PDF in a variable
    pages = convert_from_path(PDF_file, 500)
    print("extract debug pages")
    # Counter to store images of each page of PDF to image
    image_counter = 1
    # Iterate through all the pages stored above
    for page in pages: # DON'T NEED THIS STEP AS ALL SINGLE PAGE FILES??? CHECK HOW BATCH SCANNING WORKS, MAY BE GOOD TO KEEP JUST IN CASE (BUT THEN ADD HANDLING OF INDIVIDUAL PODS FOR OUTPUT)
        # Declaring filename for each page of PDF as JPG
        # For each page, filename will be:
        # PDF page 1 -> page_1.jpg
        # PDF page 2 -> page_2.jpg
        # PDF page 3 -> page_3.jpg
        # ....
        # PDF page n -> page_n.jpg
        filename = "page_"+str(image_counter)+".jpg"
        # Save the image of the page in system
        page.save(filename, 'JPEG')

        # Increment the counter to update filename
        image_counter = image_counter + 1
    print("extract debug before part 2")
    '''
    Part #2 - Recognizing text from the images using OCR
    3
    '''
    # Variable to get count of total number of pages
    filelimit = image_counter-1
    # Creating a text file to write the output
    #outfile = "out_text.txt"
    # Open the file in append mode so that
    # All contents of all images are added to the same file
    #f = open(outfile, "a")
    # Iterate from 1 to total number of pages
    for i in range(1, filelimit + 1): #in this loop we shouold be checking if order num can be found at all in any of the pages (or even just not try to do multi-page ones)
        # Set filename to recognize text from
        # Again, these files will be:
        # page_1.jpg
        # page_2.jpg
        # ....
        # page_n.jpg
        filename = "page_"+str(i)+".jpg"
        # Recognize the text as string in image using pytesserct
        print("extract debug before tesseract call")
        print(filename)
        text = str(((pytesseract.image_to_string(Image.open(filename)))))
        print("extract debug after tesseract call")
        # The recognized text is stored in variable text
        # Any string processing may be applied on text
        # Here, basic formatting has been done:
        # In many PDFs, at line ending, if a word can't
        # be written fully, a 'hyphen' is added.
        # The rest of the word is written in the next line
        # Eg: This is a sample text this word here GeeksF-
        # orGeeks is half on first line, remaining on next.
        # To remove this, we replace every '-\n' to ''.
        #print(text)
        #print("---------------------------------------------------------------")
        text = text.replace('-\n', '')
        print(text)
        # Finally, write the processed text to the file.
        try:
            del_note = text.split("Delivery Note No.: ")[1][0:8]
        except:
            try:
                del_note = text.split("C.O.D. Receipt No: ")[1][0:8]
            except:
                try:
                    del_note = text.split("C.0.D. Receipt No: ")[1][0:8] #like how does this even happen, are they manually typing stuff in invoices/pods etc???? fuck!
                except:
                    try:
                        del_note = text.split("Order No.")[1].split(': ')[1][0:6]
                    except:
                        try:
                            del_note = text.split("Pick List Number: ")[1][0:8] # pick lists needs tested
                        except:
                            try:
                                del_note = text.split("Pick List Number : ")[1][0:8]
                            except:
                                try:#for pink depot invoices - match the 6 digit sequence between order no and cus order strings
                                    del_array = text.split("ORDER NO")[1].split("CUS ORDER")[0]
                                    del_note = re.findall(r"\D(\d{6})\D", del_array)[0]
                                except:
                                    try:
                                        del_note = text
                                    except:
                                        del_note = "bad"
                        #print("Error obtaining text from: ",filename)
        #try:
        #    del_note = re.match(
        print(del_note)
    try:
        return del_note
    except:
        return "number of pages not detected"
     #if multiple files in one pdf then only returns the last (needs updated if batch scan saves to one file)
        #print(text)#f.write(text)
    # Close the file after writing all the text.
    #f.close()

#End functions------------------------------------------------------------------


#Initial testing----------------------------------------------------------------
#result = extract_pod('test_input/001052-1.pdf')
#print(result)
#result2 = extract_pod('C:/scanned_pods_input/237409-1.pdf')
#print(result)
#extract_pod('test_input/262051-1.pdf')

#End testing--------------------------------------------------------------------
#files_and_pods = {}
#lst = []
#dir = r'C:\Users\patrick.coffey\OneDrive - Flanagan Flooring\Desktop\scannedpods_test\test_input'
dir= r'C:\Users\patrick.coffey\OneDrive - Flanagan Flooring\Desktop\scannedpods_test\test_input'
print("Debug1")
for file in os.listdir(dir):
    print("Files...")
    if file.endswith("pdf"): #what if there are duplicate files in the dir? add logic for this too / or add a check at the output stage
        print("Attempting to read: ",file)
        filepath = dir +'\\' + file
        print(filepath)
        try:
            print("Running function \'extract_pod()\'")
            ext = extract_pod(filepath) #otherwise only the last entry is taken
            print("EXT: ",ext)
            print("Function ran, error in returned value?")

            if ext != None:
                print("Returned value is this long:",len(ext))

                if (len(ext) == 8) and re.match('[\d-]+$',ext) :
                    print("Ensure file is not open or the file won\'t move")
                    outputFilePath = "C:\\Users\\patrick.coffey\\OneDrive - Flanagan Flooring\\Desktop\\scannedpods_test\\test_output\\" + ext + ".pdf"
			#'C:\\scanned_pods_output\\' + ext + '.pdf'
                    print(outputFilePath)
                    shutil.move(filepath,outputFilePath) #check for duplicate filename first (maybe get list of filenames before running this loop in case this adds processing time significantly)
                elif (len(ext) == 6) and re.match('[\d-]+$',ext) :
                    ext = ext + "-1"
                    print("Ensure file is not open or the file won\'t move")
                    outputFilePath = 'C:\\Users\\patrick.coffey\\OneDrive - Flanagan Flooring\\Desktop\\scannedpods_test\\test_output\\' + ext + '.pdf'
                        #'C:\\scanned_pods_output\\' + ext + '.pdf'
                    print(outputFilePath)
                    shutil.move(filepath,outputFilePath) #check for duplicate filename first (maybe get list of filenames before running this loop in case this adds processing time significantly)
                else:
                    print("Did not validate - printing first 15 characters of order num:")
                    print(ext[0:15])

            #lst.append(ext)
        except:
            print("Failed to open: ",file,"\n")

#print(files_and_pods)
print("-----------------------------------------------------------------------")
#print(lst)
#Real code----------------------------------------------------------------------
