import cv2
import numpy as np
cap = cv2.VideoCapture(0)

n=0
while(True):
    text = "conveyor"
    n=n+1
    ret,frame = cap.read()
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray,(5,5),0)
    ret ,thresh = cv2.threshold(gray,150,255,cv2.THRESH_BINARY)
    contours,hierachy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
    font = cv2.FONT_HERSHEY_SIMPLEX
    x=[]
    y=[]
    
    
    cv2.imshow("normal",frame)
    cv2.imshow("threshold",thresh)
    if len(contours)>0:
        for i in range(0,len(contours)):
            for j in range(0,len(contours[i])):
                x.append(contours[i][j][0][0])
                y.append(contours[i][j][0][1])
        frame = cv2.drawContours(frame,contours,-1,(0,255,0),3)
        error ="incorrectly placed"
        distance = 0
        correct = "correctly placed"
        for i in range(1,len(x)+1):
            if len(x)>1:
                distance=(((x[i]-x[i-1])**2)+ ((y[i]-y[i-1])**2))**0.5+distance
            if i+1==len(x):
                break
        X=(max(y)+min(y))/2
        Y=(max(x)+min(x))/2
        jj=str(int(X))+","+str(int(Y))
        
        lines=cv2.HoughLinesP(thresh,1,np.pi/180,350)
        if abs(int(X)-240)>10 or abs(int(Y)-320)>10 :
            cv2.putText(frame,error,(100,400),font,1,(0,0,255),2,cv2.LINE_AA)
            cv2.rectangle(frame,(240,160),(400,320),(0,0,255),3)
        else:
            cv2.rectangle(frame,(240,160),(400,320),(0,255,0),3)
            cv2.putText(frame,correct,(100,400),font,1,(0,255,0),2,cv2.LINE_AA)
            
        if n%2==0:
            cv2.putText(frame,text,(int(Y),int(X-100)),font,1,(0,255,0),2,cv2.LINE_AA)
            
        cv2.circle(frame,(int(Y),int(X)),2,(0,0,255),3)
        z=0.05*(max(x)-min(x))
        a=0.05*(max(y)-min(y))
        shapes=["circle","square","rectangle"]
        square= abs(abs(max(y)-min(y))-abs(max(x)-min(x)))
        circle = abs(distance-(3.14*abs(max(y)-min(y))))
        rectangle= abs(2*abs(abs(max(y)-min(y))+abs(max(x)-min(x)))-distance)
        shapes = [square,circle,rectangle]
        shapes_2 = ["square","circle","rectangle"]
        for i in range(0,len(shapes)):
            if shapes[i]<0:
                shapes[i]=-1*shapes[i]
        xxx=[]
        for i in shapes:
            xxx.append(i)
        xxx.sort()
        if shapes.index(xxx[0])==0:
            if shapes.index(xxx[1])==1:
                j=shapes_2[1]
            else:
                j=shapes_2[0]
        else:
            j=shapes_2[2]
                
        if j==shapes_2[1]:
            cv2.putText(frame,j,(100,100),font,1,(0,255,0),2,cv2.LINE_AA)
            z="diameter is "+ str(z)
            cv2.putText(frame,z,(100,200),font,1,(0,255,0),2,cv2.LINE_AA)
        elif j==shapes_2[2]:
            cv2.putText(frame,j,(100,100),font,1,(0,255,0),2,cv2.LINE_AA)
            z= "length is " + str(z)
            a= "breadth is" + str(a)
            cv2.putText(frame,z,(100,200),font,1,(0,255,0),2,cv2.LINE_AA)
            cv2.putText(frame,a,(100,300),font,1,(0,255,0),2,cv2.LINE_AA)
        elif j==shapes_2[0]:
            cv2.putText(frame,j,(100,100),font,1,(0,255,0),2,cv2.LINE_AA)
            z = "side is "+str(z)
            cv2.putText(frame,z,(100,200),font,1,(0,255,0),2,cv2.LINE_AA)
            
            
            
        cv2.imshow("frame",frame)
        contours = np.array(contours)
        if cv2.waitKey(1)==ord("q"):
            break
cv2.destroyAllWindows()
