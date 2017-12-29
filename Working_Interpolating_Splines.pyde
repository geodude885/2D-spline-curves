def setup():
    size(800, 800)
    background(230)
    
    global xPoints
    xPoints = []
    global yPoints
    yPoints = []

def draw():
    if keyPressed:
        if key in ("r", "R"):
            global xPoints
            xPoints = []
            global yPoints
            yPoints = []
            mouseReleased()
    
def mouseReleased():
    clear()
    background(230)
    
    global xPoints, yPoints
    xPoints.append(mouseX)
    yPoints.append(mouseY)
    
    nPoints = len(xPoints)
        
    if nPoints > 1:
        
        xTangents = getTangents(xPoints)
        yTangents = getTangents(yPoints)
        
        xCubics = getCubics(xPoints, xTangents)
        yCubics = getCubics(yPoints, yTangents)
            
        xCurvePoints = getCurveCoords(xCubics)
        yCurvePoints = getCurveCoords(yCubics)
            
        strokeWeight(1)
        for t in range(0, nPoints-1):
            strokeWeight(1)
            stroke(200)
            line(xPoints[t], yPoints[t], xPoints[t+1], yPoints[t+1])
            stroke(200, 255, 200)
            line(xPoints[t], t*height/(nPoints-1), xPoints[t+1], (t+1)*height/(nPoints-1))
            line(xPoints[t], t*height/(nPoints-1), xPoints[t] + xTangents[t], (t+1)*height/(nPoints-1))
            stroke(200, 200, 255)
            line(t*width/(nPoints-1), yPoints[t], (t+1)*width/(nPoints-1), yPoints[t+1])
            line(t*width/(nPoints-1), yPoints[t], (t+1)*width/(nPoints-1), yPoints[t] + yTangents[t])
        
        for i in range(len(xCurvePoints)-1):
            stroke(200, 255, 200)
            y1 = float(width)/len(xCurvePoints) * i
            y2 = y1 + float(width)/len(xCurvePoints)
            line(xCurvePoints[i], y1, xCurvePoints[i+1], y2)
            stroke(200, 200, 255)
            line(y1, yCurvePoints[i], y2, yCurvePoints[i+1])
            
        stroke(0)
        [line(xCurvePoints[i], yCurvePoints[i], xCurvePoints[i+1], yCurvePoints[i+1]) for i in range(len(xCurvePoints)-1)]
        
        strokeWeight(10) 
        for t in range(nPoints):
            stroke(200, 255, 200)
            point(xPoints[t], t*height/(nPoints-1))
            stroke(200, 200, 255)
            point(t*width/(nPoints-1), yPoints[t]) 
            
        stroke(255, 0, 0)
        [point(xPoints[t], yPoints[t]) for t in range(nPoints)]
            
        #for i in range(nPoints):
        #    i-=1
        #    print("x(t) = " + str(xCubics[i][0]) + "t^3 + " + str(xCubics[i][1]) + "t^2 + " + str(xCubics[i][2]) + "t + " + str(xCubics[i][3]))
        #    print("y(t) = " + str(yCubics[i][0]) + "t^3 + " + str(yCubics[i][1]) + "t^2 + " + str(yCubics[i][2]) + "t + " + str(yCubics[i][3]))
        
    else:
        strokeWeight(10) 
        stroke(255, 0, 0)
        point(xPoints[0], yPoints[0])
    
def getTangents(a):
    exPoints = [a[1]]
    [exPoints.append(p) for p in a]
    exPoints.append(a[-2])
    tangents = []
    for i in range(1, len(a) + 1):
        tangents.append((exPoints[i+1]-exPoints[i-1])/2)
    return tangents

def getCubics(points, tangents):
    cubics = []
    for t in range(len(points)-1):
            d = points[t]
            c = tangents[t]
            a = tangents[t+1] + c + 2 * (d - points[t+1])
            b = points[t+1] - c - d - a
            cubics.append([a, b, c, d])
    return cubics

def getCurveCoords(cubics):
    curvePoints = []
    for t in range(0, len(cubics)):
        for tPart in range(width/(len(cubics)+1)):
            curvePoints.append(int(cubicVal(float(tPart)/(width/(len(cubics)+1)), cubics[t])))
    return curvePoints
            
def cubicVal(val, a):
    return a[0] * val**3 + a[1] * val**2 + a[2] * val + a[3]
        
    