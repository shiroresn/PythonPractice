#     * 
#    * * 
#   * * * 
#  * * * * 
# * * * * * 


count = 5
xx = 1
for j in range(0,5):
    for i in range(0,count):
        print "",
    for k in range(0,xx):
        print "*",
        
    xx=xx+1   
    print ""
    count = count-1
