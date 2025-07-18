class open_doc():
    def __init__(self):
        pass

    def open(self):
        raise NotImplementedError("Didn't find a file!")
    

class open_pdf(open_doc):
    def __init__(self):
        super().__init__()
    
    def open(self):
        print("pdf is open now..")

class open_img(open_doc):
    def __init__(self):
        super().__init__()
    def open(self):
        print("img is open now..")

class open_jpg(open_img):
    def __init__(self):
        super().__init__()
    def open(self):
        print("file type not supported..")


myPdf=open_pdf()
myImg=open_img()
myJpg=open_jpg()
doc=open_doc()

myPdf.open()
myJpg.open()

# doc.open()




