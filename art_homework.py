def setup():
    size(400, 600) # sizing your canvas
    background("#c3471b")

def draw():
    fill("#c4ae96")
    no_stroke()
    rect(25, 25, 350, 250)
    
    fill("#d59583")
    no_stroke()
    square(100, 50, 200)
    
    fill("#d59583")
    no_stroke()
    rect(25, 275, 350, 25)
    
    fill("#de6046")
    no_stroke()
    rect(25, 300, 350, 15)
    
    fill("#5d7b93")
    no_stroke()
    rect(25, 315, 350, 30)
    
    fill("#ce4737")
    no_stroke()
    rect(25, 345, 350, 30)
    
    fill("#d59583")
    no_stroke()
    rect(50, 345, 325, 30)
    
    fill("#5d7b93")
    no_stroke()
    rect(25, 375, 350, 30)
    
    fill("#d93224")
    no_stroke()
    rect(25, 405, 350, 30)
    
    fill("#d28372")
    no_stroke()
    rect(25, 435, 350, 45)
    
    fill("#819699")
    no_stroke()
    rect(25, 480, 350, 55)
    
    fill("#d7b9a1")
    no_stroke()
    rect(25, 535, 350, 55)
    
    stroke("#bd5353")
    stroke_weight(3)
    line(25, 537, 374, 537)
    
    stroke("#d60014")
    stroke_weight(5)
    line(26, 544, 373, 544)
    
    stroke("#bd5353")
    stroke_weight(3)
    line(25, 558, 374, 558)
    
    stroke("#bd5353")
    stroke_weight(3)
    line(25, 565, 374, 565)
    
def key_pressed(e):
   # print(e)
    key_value = e.get_key()
    if key_value.lower() == 's':
        save('art_homework.jpg')