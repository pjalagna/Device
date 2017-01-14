# file DeviceDriver.py
DeviceDriver(port):
    """ receives a byte from a port
        this driver is a stump function that returns the database store
    """
    import TCVRClass
    db = TCVRClass.TCVR('hubdb')
    m = db.newRec()
    m[db._TABLE] = 'PORT'
    m[db._COLUMN] = 'Byte'
    m[db._ROW]=port
    x = db.fetch(m)
    return(x[0][db._VALUE])
#end DeviceDriver
