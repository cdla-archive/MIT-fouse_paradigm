import numpy as np
from psychopy import visual
from graph_base import GraphBase, scale
import time

class ThermBase(GraphBase):
    def __init__(self,win,size=[1,1],pos=[0,0],scale=range(-3,4)):
        """
        Inputs
        ------
        win : visual.Window object
        size : size of graph
        pos : position of graph
        """

        self._pos = pos
        self._size = size
        self._win = win
        self.objects = []

        self._draw_axis()
        
        _, ay,by = self._scaleY(scale)
        _, ax,bx = self._scaleX()
        self._draw_axis_labels(scale,by)
        self.affine = np.array([[ax,0.,bx],[0.,ay,by+self._pos[1]],[0.,0.,1.]])
        self.T = lambda x,y : tuple(np.dot(self.affine,[x,y,1.])[:2].tolist())
    
    def plotFB(self, fb, max, zero_val,fillColor=None,thresh=None):
        FB = visual.ShapeStim(self._win,
                                  closeShape=True,
                                  vertices= (self.T(0,0),
                                                    self.T(0,fb),
                                                    self.T(1,fb),
                                                    self.T(1,0)),
                                                    fillColor = fillColor,
                                                    depth=-1,
                                                    opacity=1)
                                                        
        self.objects.append(FB)
    
    def plotThr(self,max):
        TH =  visual.ShapeStim(self._win,
                                      closeShape=False,
                                      vertices= (self.T(0,max),
                                                 self.T(1,max)),
                                      lineColor='black')
                                      
        self.objects.append(TH)
        
        thTxt = visual.TextStim(self._win,'*',pos=[self._pos[0]+self._size[0]+0.1,self.T(0,max)[1]])
        self.objects.append(thTxt)
        
    def plot(self,fb,zero_val,arrow='up',frame=20,maxframe=10):
        frac = float(frame)/float(maxframe)
        color = 'black'
    
        if frac >= 1:
            frac = 1.0
        
        if (fb < zero_val):
                fillColor = 'red'
            
        elif (fb >= zero_val):
                fillColor = 'green'
        
        #self.plotFB((fb-zero_val)*frac+zero_val,color,zero_val)
        self.plotFB((fb-zero_val)*1+zero_val,fillColor,zero_val)
        self.plotThr(zero_val)
    
        
    def _scaleY(self,X):
        y,a,b = scale(X)
        f = lambda pt: pt*a+b+self._pos[1]
        return f, a, b
        
    def _scaleX(self):
        a,b = self._size[0], self._pos[0]
        f = lambda pt: pt*self._size[0]+self._pos[0]
        return f, a, b
    
    
if __name__== "__main__":
    win = visual.Window([800,600])
    
    t = ThermBase(win, [0.25,1],[-0.125,-0.5])
    
    for i in range(0,21):
        t.plot(0.5,1.0,'up',i,20)
        t.draw()
        win.flip()
