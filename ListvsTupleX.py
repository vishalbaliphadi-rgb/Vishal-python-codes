#------------------------------------------------------
#                   List       Tuple
#-------------------------------------------------------
# Ordered           Yes         Yes           
# Indexed           Yes         Yes   
# Mutable           Yes         No
#     
def main():
    Data1 = [10,3.14,True,"Pune"]  #List
    data2 = (10,3.14,True,"Pune")  # Tuple

    print (Data1)
    print (data2)

    print(Data1[0])
    print(data2[0])

if __name__ == "__main__":
    main()