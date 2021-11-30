from tkinter import *

root = Tk()

frameForm = Frame (root)
frameForm.pack()

Label(frameForm,
        text='Codigo Producto:',
        font='Arial').grid(row=0,
                           column=0,
                           sticky='w',
                           padx=5,
                           pady=5)

codigo = Entry(frameForm,
               width=40).grid(row=0,
                             column=1,
                             padx=5,
                             pady=5)

btnRegistrar = Button(frameForm,
                       text='Registrar',
                       bg = 'green',
                       fg = 'white',
                       font = 'Arial',
                       width = 10).grid(row = 5,
                                        column =1,
                                         sticky = 'e',
                                         padx = 5,
                                         pady = 5 )
btnSalir = Button(frameForm,
                   text='Salir',
                   bg = 'red',
                   fg = 'white',
                   font = 'Arial',
                   width = 10).grid(row = 5,
                                    column = 1,
                                    
                   
                   
                   
                   )  

root.mainloop()
              