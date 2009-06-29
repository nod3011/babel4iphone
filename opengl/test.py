import pygegl

if __name__=="__main__":
    print "Hit ESC key to quit."
    
    pygegl.display.init(800, 600)
    pygegl.display.set_caption("Prova")
    
    sc = pygegl.scene.create()
    
    img0 = pygegl.surface.load("prova.png", [-1.0, 0.0, 1.0])
    img0.color = [1.0, 1.0, 1.0, 0.5]
    
    img1 = pygegl.surface.load("NeHe.bmp", [1.0, 0.0, 0.0])
    
    img2 = pygegl.surface.load("prova.jpg", [0.0, 1.0, 0.0])
    img2.scalar = 0.6
    
    sc.addObject(img0)
    sc.addObject(img1)
    sc.addObject(img2)
    
    # Start Event Processing Engine
    pygegl.display.mainLoop()