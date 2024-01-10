import random

file = open("./svg_bg_p6g.svg", "w")

file.write("""<svg xmlns='http://www.w3.org/2000/svg'  width='300' height='300' viewBox='0 0 300 300'>
    <defs>
        <radialGradient id="background">
            <stop offset='0' stop-color='yellow' />
            <stop offset='1' stop-color='#ff5100'/>
        </radialGradient>

        <pattern id="background_block" x="0" y="0" width="100" height="100" patternUnits="userSpaceOnUse">
                <rect x="50" y="0" width="50" height="50" fill='#ffd500'/>
                <rect x="0" y="50" width="50" height="50" fill='#ffd500'/>

        </pattern>

        <linearGradient id="a" gradientUnits="objectBoundingBox" gradientTransform="rotate(90)">
            <stop offset='0.25' stop-color='#000' stop-opacity='0.8'/>
            <stop offset='0.7' stop-color='#000' stop-opacity='0'/>
        </linearGradient>
        <linearGradient id="b" gradientUnits="objectBoundingBox">
            <stop offset='0.25' stop-color='#000' stop-opacity='0.8'/>
            <stop offset='0.7' stop-color='#000' stop-opacity='0'/>
        </linearGradient>
        <linearGradient id="e" gradientUnits="objectBoundingBox">x
            <stop offset='0.1' stop-color='#000' stop-opacity='0'/>
            <stop offset='0.9' stop-color='#000' stop-opacity='0.4'/>
        </linearGradient>
    </defs>

    <filter id="canvas">
        <feTurbulence
            type="turbulence"
            baseFrequency="0.1 0.66"
            numOctaves="3"
            Seed = "20"
            result="n" />
        <feBlend in="n" result="noise" mode="multiply" />
        <feDiffuseLighting in="n" result="light" lighting-color='#ff8000'>
            <feDistantLight azimuth="45" elevation="60" filtername="feDistantLight"/>
        </feDiffuseLighting>
    </filter>


    <rect fill='#ff8000' width='300' height='300' filter="url(#canvas)"/>
    <circle cx="300" cy="300" r="341" fill="url(#background)" fill-opacity='0.4'/>
    <rect x="0" y="0" width="300" height="300" fill="url(#background_block)" fill-opacity='0.4'/>\n""")

#for the shadow effect
file.write("\t<g fill-opacity='0.6'>")

#for the fuzzy white space effect
# file.write("\t<g fill-opacity='0.8'>")

tSide = "M "
lSide = "M "
rSide = "M "

tSideOut = "M "
lSideOut = "M "
rSideOut = "M "

# for all boxes white style
for i in range(0,8):
    for j in range(0,8):
        #decide if is shadow or white space
        boo = random.randint(0,1)

        #decide how small the square will shrink
        size = random.random()+1
        
        #generate paths for shadow/white space
        tSide += str(i*50) + ","
        tSide += str(j*50) + " "
        tSide += str(i*50) + ","
        tSide += str(j*50+12.5*size) + " "
        tSide += str(i*50+50) + ","
        tSide += str(j*50+12.5*size) + " "
        tSide += str(i*50+50) + ","
        tSide += str(j*50) + " "

        tSideOut += str(i*50) + ","
        tSideOut += str(j*50) + " "
        tSideOut += str(i*50) + ","
        tSideOut += str(j*50) + " "
        tSideOut += str(i*50+50) + ","
        tSideOut += str(j*50) + " "
        tSideOut += str(i*50+50) + ","
        tSideOut += str(j*50) + " "

        lSide += str(i*50) + ","
        lSide += str(j*50) + " "
        lSide += str(i*50) + ","
        lSide += str(j*50+50) + " "
        lSide += str(i*50+12.5*size) + ","
        lSide += str(j*50+50) + " "
        lSide += str(i*50+12.5*size) + ","
        lSide += str(j*50) + " "

        lSideOut += str(i*50) + ","
        lSideOut += str(j*50) + " "
        lSideOut += str(i*50) + ","
        lSideOut += str(j*50+50) + " "
        lSideOut += str(i*50) + ","
        lSideOut += str(j*50+50) + " "
        lSideOut += str(i*50) + ","
        lSideOut += str(j*50) + " "
    
        rSide += str(i*50+50-5*size) + ","  #right side has been decided to get not that big so to not interefere the next square's left side
        rSide += str(j*50) + " "
        rSide += str(i*50+50) + ","
        rSide += str(j*50) + " "
        rSide += str(i*50+50) + ","
        rSide += str(j*50+50) + " "
        rSide += str(i*50+50-5*size) + ","
        rSide += str(j*50+50) + " "

        rSideOut += str(i*50+50) + ","
        rSideOut += str(j*50) + " "
        rSideOut += str(i*50+50) + ","
        rSideOut += str(j*50) + " "
        rSideOut += str(i*50+50) + ","
        rSideOut += str(j*50+50) + " "
        rSideOut += str(i*50+50) + ","
        rSideOut += str(j*50+50) + " "

        #random animation duration time
        time = random.randint(5,15)

        file.write('\t<path fill="white" d="{}">\n'.format(tSide))
        file.write('\t\t<animate attributeName="d" repeatDur="indefinite" dur="{}s" keyTimes="0;0.5;1"\n values="{}; {}; {}"/>\n'.format(str(time),tSide,tSideOut,tSide))
        file.write('\t</path>\n')

        file.write('\t<path fill="white" d="{}">\n'.format(lSide))
        file.write('\t\t<animate attributeName="d" repeatDur="indefinite" dur="{}s" keyTimes="0;0.5;1"\n values="{}; {}; {}"/>\n'.format(str(time),lSide,lSideOut,lSide))
        file.write('\t</path>\n')

        file.write('\t<path fill="white" d="{}">\n'.format(rSide))
        file.write('\t\t<animate attributeName="d" repeatDur="indefinite" dur="{}s" keyTimes="0;0.5;1"\n values="{}; {}; {}"/>\n'.format(str(time),rSide,rSideOut,rSide))
        file.write('\t</path>\n')

        #reset the sides for next path
        tSide = "M "
        lSide = "M "
        rSide = "M "

        tSideOut = "M "
        lSideOut = "M "
        rSideOut = "M "



#for all boxes shadow style
# for i in range(0,8):
#     for j in range(0,8):
#         #decide if is shadow or white space
#         boo = random.randint(0,1)

#         #decide how small the square will shrink
#         size = random.random()+1
        
#         if boo == 1:
#             tSide += str(i*50) + ","
#             tSide += str(j*50) + " "
#             tSide += str(i*50) + ","
#             tSide += str(j*50+12.5*size) + " "
#             tSide += str(i*50+50) + ","
#             tSide += str(j*50+12.5*size) + " "
#             tSide += str(i*50+50) + ","
#             tSide += str(j*50) + " "

#             tSideOut += str(i*50) + ","
#             tSideOut += str(j*50) + " "
#             tSideOut += str(i*50) + ","
#             tSideOut += str(j*50) + " "
#             tSideOut += str(i*50+50) + ","
#             tSideOut += str(j*50) + " "
#             tSideOut += str(i*50+50) + ","
#             tSideOut += str(j*50) + " "

#             lSide += str(i*50) + ","
#             lSide += str(j*50) + " "
#             lSide += str(i*50) + ","
#             lSide += str(j*50+50) + " "
#             lSide += str(i*50+12.5*size) + ","
#             lSide += str(j*50+50) + " "
#             lSide += str(i*50+12.5*size) + ","
#             lSide += str(j*50) + " "

#             lSideOut += str(i*50) + ","
#             lSideOut += str(j*50) + " "
#             lSideOut += str(i*50) + ","
#             lSideOut += str(j*50+50) + " "
#             lSideOut += str(i*50) + ","
#             lSideOut += str(j*50+50) + " "
#             lSideOut += str(i*50) + ","
#             lSideOut += str(j*50) + " "
        
#             rSide += str(i*50+50-5*size) + ","  #right side has been decided to get not that big so to not interefere the next square's left side
#             rSide += str(j*50) + " "
#             rSide += str(i*50+50) + ","
#             rSide += str(j*50) + " "
#             rSide += str(i*50+50) + ","
#             rSide += str(j*50+50) + " "
#             rSide += str(i*50+50-5*size) + ","
#             rSide += str(j*50+50) + " "

#             rSideOut += str(i*50+50) + ","
#             rSideOut += str(j*50) + " "
#             rSideOut += str(i*50+50) + ","
#             rSideOut += str(j*50) + " "
#             rSideOut += str(i*50+50) + ","
#             rSideOut += str(j*50+50) + " "
#             rSideOut += str(i*50+50) + ","
#             rSideOut += str(j*50+50) + " "

#             #random animation duration time
#             time = random.randint(5,15)

#             file.write('\t<path fill="url(#a)" d="{}">\n'.format(tSide))
#             file.write('\t\t<animate attributeName="d" repeatDur="indefinite" dur="{}s" keyTimes="0;0.5;1"\n values="{}; {}; {}"/>\n'.format(str(time),tSide,tSideOut,tSide))
#             file.write('\t</path>\n')

#             file.write('\t<path fill="url(#b)" d="{}">\n'.format(lSide))
#             file.write('\t\t<animate attributeName="d" repeatDur="indefinite" dur="{}s" keyTimes="0;0.5;1"\n values="{}; {}; {}"/>\n'.format(str(time),lSide,lSideOut,lSide))
#             file.write('\t</path>\n')

#             file.write('\t<path fill="url(#e)" d="{}">\n'.format(rSide))
#             file.write('\t\t<animate attributeName="d" repeatDur="indefinite" dur="{}s" keyTimes="0;0.5;1"\n values="{}; {}; {}"/>\n'.format(str(time),rSide,rSideOut,rSide))
#             file.write('\t</path>\n')

#             #reset the sides for next path
#             tSide = "M "
#             lSide = "M "
#             rSide = "M "

#             tSideOut = "M "
#             lSideOut = "M "
#             rSideOut = "M "


#for only orange boxes
# for i in range(1,8,2):
#     for j in range(1,8,2):
#         boo = random.randint(0,1)
#         if boo==1:
#             tSide += str(i*100) + ","
#             tSide += str(j*100) + " "
#             tSide += str(i*100) + ","
#             tSide += str(j*100+25) + " "
#             tSide += str(i*100+100) + ","
#             tSide += str(j*100+25) + " "
#             tSide += str(i*100+100) + ","
#             tSide += str(j*100) + " "

#             tSideOut += str(i*100) + ","
#             tSideOut += str(j*100) + " "
#             tSideOut += str(i*100) + ","
#             tSideOut += str(j*100) + " "
#             tSideOut += str(i*100+100) + ","
#             tSideOut += str(j*100) + " "
#             tSideOut += str(i*100+100) + ","
#             tSideOut += str(j*100) + " "

#             lSide += str(i*100) + ","
#             lSide += str(j*100) + " "
#             lSide += str(i*100) + ","
#             lSide += str(j*100+100) + " "
#             lSide += str(i*100+25) + ","
#             lSide += str(j*100+100) + " "
#             lSide += str(i*100+25) + ","
#             lSide += str(j*100) + " "

#             lSideOut += str(i*100) + ","
#             lSideOut += str(j*100) + " "
#             lSideOut += str(i*100) + ","
#             lSideOut += str(j*100+100) + " "
#             lSideOut += str(i*100) + ","
#             lSideOut += str(j*100+100) + " "
#             lSideOut += str(i*100) + ","
#             lSideOut += str(j*100) + " "
        
#             rSide += str(i*100+90) + ","
#             rSide += str(j*100) + " "
#             rSide += str(i*100+100) + ","
#             rSide += str(j*100) + " "
#             rSide += str(i*100+100) + ","
#             rSide += str(j*100+100) + " "
#             rSide += str(i*100+90) + ","
#             rSide += str(j*100+100) + " "

#             rSideOut += str(i*100+100) + ","
#             rSideOut += str(j*100) + " "
#             rSideOut += str(i*100+100) + ","
#             rSideOut += str(j*100) + " "
#             rSideOut += str(i*100+100) + ","
#             rSideOut += str(j*100+100) + " "
#             rSideOut += str(i*100+100) + ","
#             rSideOut += str(j*100+100) + " "

#             time = random.randint(5,15)
#             file.write('\t<path fill="url(#a)" d="{}">\n'.format(tSide))
#             file.write('\t\t<animate attributeName="d" repeatDur="indefinite" dur="{}s" keyTimes="0;0.5;1"\n values="{}; {}; {}"/>\n'.format(str(time),tSide,tSideOut,tSide))
#             file.write('\t</path>\n')

#             time = random.randint(5,15)
#             file.write('\t<path fill="url(#b)" d="{}">\n'.format(lSide))
#             file.write('\t\t<animate attributeName="d" repeatDur="indefinite" dur="{}s" keyTimes="0;0.5;1"\n values="{}; {}; {}"/>\n'.format(str(time),lSide,lSideOut,lSide))
#             file.write('\t</path>\n')

#             time = random.randint(5,15)
#             file.write('\t<path fill="url(#e)" d="{}">\n'.format(rSide))
#             file.write('\t\t<animate attributeName="d" repeatDur="indefinite" dur="{}s" keyTimes="0;0.5;1"\n values="{}; {}; {}"/>\n'.format(str(time),rSide,rSideOut,rSide))
#             file.write('\t</path>\n')

#             tSide = "M "
#             lSide = "M "
#             rSide = "M "

#             tSideOut = "M "
#             lSideOut = "M "
#             rSideOut = "M "


# for i in range(0,8,2):
#     for j in range(0,8,2):
#         #decide to have shadow or not
#         boo = random.randint(0,1)

#         if boo==1:
#             tSide += str(i*100) + ","
#             tSide += str(j*100) + " "
#             tSide += str(i*100) + ","
#             tSide += str(j*100+25*size) + " "
#             tSide += str(i*100+100) + ","
#             tSide += str(j*100+25*size) + " "
#             tSide += str(i*100+100) + ","
#             tSide += str(j*100) + " "

#             tSideOut += str(i*100) + ","
#             tSideOut += str(j*100) + " "
#             tSideOut += str(i*100) + ","
#             tSideOut += str(j*100) + " "
#             tSideOut += str(i*100+100) + ","
#             tSideOut += str(j*100) + " "
#             tSideOut += str(i*100+100) + ","
#             tSideOut += str(j*100) + " "

#             lSide += str(i*100) + ","
#             lSide += str(j*100) + " "
#             lSide += str(i*100) + ","
#             lSide += str(j*100+100) + " "
#             lSide += str(i*100+25*size) + ","
#             lSide += str(j*100+100) + " "
#             lSide += str(i*100+25*size) + ","
#             lSide += str(j*100) + " "

#             lSideOut += str(i*100) + ","
#             lSideOut += str(j*100) + " "
#             lSideOut += str(i*100) + ","
#             lSideOut += str(j*100+100) + " "
#             lSideOut += str(i*100) + ","
#             lSideOut += str(j*100+100) + " "
#             lSideOut += str(i*100) + ","
#             lSideOut += str(j*100) + " "
        
#             rSide += str(i*100+100-10*size) + ","
#             rSide += str(j*100) + " "
#             rSide += str(i*100+100) + ","
#             rSide += str(j*100) + " "
#             rSide += str(i*100+100) + ","
#             rSide += str(j*100+100) + " "
#             rSide += str(i*100+100-10*size) + ","
#             rSide += str(j*100+100) + " "

#             rSideOut += str(i*100+100) + ","
#             rSideOut += str(j*100) + " "
#             rSideOut += str(i*100+100) + ","
#             rSideOut += str(j*100) + " "
#             rSideOut += str(i*100+100) + ","
#             rSideOut += str(j*100+100) + " "
#             rSideOut += str(i*100+100) + ","
#             rSideOut += str(j*100+100) + " "

#             time = random.randint(5,15)
#             file.write('\t<path fill="url(#a)" d="{}">\n'.format(tSide))
#             file.write('\t\t<animate attributeName="d" repeatDur="indefinite" dur="{}s" keyTimes="0;0.5;1"\n values="{}; {}; {}"/>\n'.format(str(time),tSide,tSideOut,tSide))
#             file.write('\t</path>\n')

#             time = random.randint(5,15)
#             file.write('\t<path fill="url(#b)" d="{}">\n'.format(lSide))
#             file.write('\t\t<animate attributeName="d" repeatDur="indefinite" dur="{}s" keyTimes="0;0.5;1"\n values="{}; {}; {}"/>\n'.format(str(time),lSide,lSideOut,lSide))
#             file.write('\t</path>\n')

#             time = random.randint(5,15)
#             file.write('\t<path fill="url(#e)" d="{}">\n'.format(rSide))
#             file.write('\t\t<animate attributeName="d" repeatDur="indefinite" dur="{}s" keyTimes="0;0.5;1"\n values="{}; {}; {}"/>\n'.format(str(time),rSide,rSideOut,rSide))
#             file.write('\t</path>\n')

#             tSide = "M "
#             lSide = "M "
#             rSide = "M "

#             tSideOut = "M "
#             lSideOut = "M "
#             rSideOut = "M "



file.write("\t</g>\n</svg>")
