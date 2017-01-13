# file DeviceDriver.py
DeviceDriver(port):
    """ receives a byte from a port
        this driver is a stump function that returns the database store
    """
    import TCVRClass
    x = TCVRRead(T='PORT',C='Byte','',R=port)
    return(x)
#end DeviceDriver
