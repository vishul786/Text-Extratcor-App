def mouseDoubleClickEvent(self,event):
        print("mouseDoubleClickEvent triggered")
        try:
            fname = QtWidgets.QFileDialog.getOpenFileName(self,'Select Image',
                                                          '.',"(*.jpg,*.png,*.jpeg)")
            if fname:
                self.image_path = fname[0]
                self.set_image(self.image_path)
        except Exception as e: print(e)