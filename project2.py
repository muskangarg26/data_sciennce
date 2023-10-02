from numpy import loadtxt
filename='pima-indians-diabetes-data.csv'
raw_data=open(filename,'rb')
data=loadtxt(raw_data,delimiter="'")
data
type(data)
data.shape
data[0]
data[-1]
                                                   

                            
                        
        

      
