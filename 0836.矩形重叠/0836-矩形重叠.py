class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        x0,y0,x1,y1 = rec1
        X0,Y0,X1,Y1 = rec2
        
        rec_x = [x0,x1,X0,X1]
        rec_y = [y0,y1,Y0,Y1]
        
        rec_x0 = min(rec_x)
        rec_y0 = min(rec_y)
        
        rec_x1 = max(rec_x)
        rec_y1 = max(rec_y)
        
        
        if (rec_y1-rec_y0 >= (y1-y0+Y1-Y0)) or (rec_x1-rec_x0 >= (x1-x0+X1-X0)):
            return False
        else:
            return True
        
    
        