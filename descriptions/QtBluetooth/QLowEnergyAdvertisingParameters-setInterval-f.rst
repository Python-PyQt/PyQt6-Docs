.. sip:method-description::
    :status: todo
    :pysig: 61569f2965b7a369eb10b6d75d410d11
    :realsig: (quint16,quint16)
    :digest: d6053695d78d7095638d1e56ebdf6825

Sets the advertising interval. This is a range that gives the controller an upper and a lower bound for how often to send the advertising data. Both *minimum* and *maximum* are given in milliseconds. If *maximum* is smaller than *minimum*, it will be set to the value of *minimum*.

**Note:** There are limits for the minimum and maximum interval; the exact values depend on the mode. If they are exceeded, the lowest or highest possible value will be used, respectively.

Setting the advertising interval is supported on BlueZ DBus backend if its experimental status is changed in later versions of BlueZ (or run in experimental mode).
