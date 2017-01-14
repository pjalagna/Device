# file DeviceDriverSnd.py
DeviceDriverSnd(port,data):
    """ this driver is a stump function that writes to the database """
    import TCVRClass
    db1 = TCVRClass.TCVR('hubdb')
    j = db1.newRec()
    j[db._TABLE] = 'PORT'
    j[db._COLUMN] = 'Byte'
    j[db._ROW] = port
    j[db._VALUE] = data
    try:
        db1.update(j)
    except:
        db1.insert(j)
    finaly:
        nop = -1
    #end try
#end DeviceDriverSnd
