init python:
    gallery = Gallery()

    gallery.button("Ending1") 
    gallery.unlock_image("ed1ver1")
    gallery.unlock_image("ed1ver2") 

    gallery.button("Ending2") 
    gallery.unlock_image("ed2ver1")
    gallery.unlock_image("ed2ver2") 

    gallery.button("Ending3") 
    gallery.unlock_image("ed3ver1")
    gallery.unlock_image("ed3ver2") 

    gallery.button("Ending4") 
    gallery.unlock_image("ed4ver1")
    gallery.unlock_image("ed4ver2") 

    gallery.button("Ending5") 
    gallery.unlock_image("ed5ver1")
    gallery.unlock_image("ed5ver2") 

    gallery.button("Ending6") 
    gallery.unlock_image("ed6ver1")
    gallery.unlock_image("ed6ver2") 
    

screen album:
    tag menu
    add "images/CustomUI/bg gallery.png"
    
    hbox:
        xalign 0.5
        yalign 0.5
        spacing 20
        grid 3 2:
            add gallery.make_button(name="Ending1",unlocked="CGs/small/ed1ver1small.png",locked="CGs/small/locked.png") 
            add gallery.make_button(name="Ending2",unlocked="CGs/small/ed2ver1small.png",locked="CGs/small/locked.png") 
            add gallery.make_button(name="Ending3",unlocked="CGs/small/ed3ver1small.png",locked="CGs/small/locked.png") 
            add gallery.make_button(name="Ending4",unlocked="CGs/small/ed4ver1small.png",locked="CGs/small/locked.png") 
            add gallery.make_button(name="Ending5",unlocked="CGs/small/ed5ver1small.png",locked="CGs/small/locked.png") 
            add gallery.make_button(name="Ending6",unlocked="CGs/small/ed6ver1small.png",locked="CGs/small/locked.png")  
            spacing 30
        textbutton "Return" action Return()