#Draw sketches


from sketchpy import library as lib
# Function to draw sketches
def sketches():
    name = input('''
    
    
    Please choose any onne sketch:
    [1] Apj
    [2] Rdj
    [3] Vijay
    [4] Tom holland
    [5] Flag
    [6] Bts
    [7] Gojo
    ''')
    name=int(name)
    if name==1:
        sketch=lib.apj()
    elif name==2:
        sketch=lib.rdj()
    elif name==3:
        sketch=lib.vijay()
    elif name==4:
        sketch=lib.tom_holland()
    elif name==5:
        sketch=lib.flag()
    elif name==6:
        sketch=lib.bts()
    elif name==7:
        sketch=lib.gojo()
    else:
        print('Please enter a valid input')
    sketch.draw()
sketches()
