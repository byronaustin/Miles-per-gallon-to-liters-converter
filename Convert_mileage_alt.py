def convert_mileage2(m):
    return ((3.78/((m*1.6)/100)))

if __name__ == '__main__' :
    print ("20 MPG = ",convert_mileage2(20)," Liters per 100 kilometers") 
