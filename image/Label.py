from PyQt5 import QtCore, QtGui, QtWidgets, uic

class Label(QtWidgets.QLabel):
    def __init__(self,lineedit=None):
        super().__init__()
        self.setAcceptDrops(True)
        self.lineedit = lineedit
        # self.image_path =None
        # self center alignment of image label
        self.setAlignment(QtCore.Qt.AlignCenter)
        #set text on image label
        self.setText("Drag your image here!!!")
        # set the label style
        self.setStyleSheet('''background-color: rgb(255,255,255); color:rgb(39,86,115);   
                            font:75 9pt "MS Shell Dlg 2";''')
    def dragEnterEvent(self,event):
        # check if event has image or not
        if event.mimeData().hasImage:
            #if event has image then
            #accept the event to drag
            event.accept()
        else:
            #if event doesn't have image then ignore
            #the event drag
            event.ignore()
    def mouseDoubleClickEvent(self,event):
        print("mouseDoubleClickEvent triggered")
        try:
            fname = QtWidgets.QFileDialog.getOpenFileName(self,'Select Image',
                                                          '.',"Image Types(*.jpg *.png *.jpeg)")
            if fname:
                self.image_path = fname[0]
                self.set_image(self.image_path)
        except Exception as e: print(e)
    def dropEvent(self,event):
        #check if  event has image or not
        if event.mimeData().hasImage:
            #set drop actionwith copying dragged image
            event.setDropAction(QtCore.Qt.CopyAction)
            #get_selected image path
            image_path=event.mimeData().urls()[0].toLocalFile()
            self.image_path = image_path
            # call set_image() function to load
            #image with image path parameter
            self.set_image(image_path)
            #if event has image then
            #accept the event to drop
            event.accept()
        else:
            #if event doesn't have image
            #then ignore yhe event to drop
            event.ignore()
    def set_image(self,image_path):
        #load and display image
        try:
            if self.lineedit:
                self.lineedit.setText(image_path)
            image_path = QtGui.QPixmap(image_path)
            image_path = image_path.scaled( QtCore.QSize(self.width(),
                                                         self.height()),
                                            QtCore.Qt.KeepAspectRatio,
                                            QtCore.Qt.SmoothTransformation)
            self.setPixmap(image_path)
        except Exception as e: print(e)


if __name__ == "__main__":
    import sys
    print('running')
    try:

        app = QtWidgets.QApplication(sys.argv)
        ui = uic.loadUi('ocr_label.ui')
        imgddlabel = Label() 
        ui.imgLayout.addWidget(imgddlabel)
        ui.show()
        app.exec_()
    except Exception as e: print(e)
    print('running finished')



                    

