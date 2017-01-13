# file DeviceDriverSnd.py
DeviceDriverSnd(port,data):
    """ this driver is a stump function that writes to the database """
    import TCVRClass
    db1 = TCVRClass.TCVR()
    db1.TCVRWrite(T='PORT',C='Byte',V=data,R=port)
#end DeviceDriverSnd
