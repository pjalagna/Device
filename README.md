# Device
device agent
getpos() -- lon,lat and depth
getZULU() -- time in zulu
getValue() -- environmental monitor
sendDev(id,val,pos,zulu on hubCH )
sleep and repeat

repeater agent
poll device list by channel till eol
-- at eol sleep and repeat
per device
-- if msg null skip
-- else
---- sendPACK(getHUBch,package)
repeat per device


hub agent
poll repeater list by ch
per poll
-- if msg null skip
-- else
---- writeDB(package)
repeat per poll
