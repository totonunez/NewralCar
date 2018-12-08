"""
CREATE TABLE GPS
            (PATENTE varchar(6) references AUTOS(PATENTE),
            fecha int  --> que la sacaremos de los sensores,
            hora int,  --> que la sacaremos de los sensores
            longitud int   -->,
            latitud int;   -->
"""

c=2
if c is 1:
    iniciolatitud=-70.599644
    iniciolongitud=-33.490855
    for i in range(2000):
        print("{0:.5f}".format(iniciolongitud-i*0.000001),',',"{0:.5f}".format(iniciolatitud-i*0.00001) )
if c is 2:
    iniciolatitud=-70.539405
    iniciolongitud=-33.428637
    #-33.431673, -70.584380
    for i in range(4000):
        print("{0:.6f}".format(iniciolongitud-i*0.0000001),',',"{0:.6f}".format(iniciolatitud-i*0.00001) )
