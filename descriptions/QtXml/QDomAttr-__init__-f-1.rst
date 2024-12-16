.. sip:method-description::
    :status: todo
    :pysig: c0b1f26748a8a22542f8256ed7a18944
    :realsig: (const QDomAttr&)
    :digest: 48d8814920718f2eec158887fd44ec57

Constructs a copy of *attr*.

The data of the copy is shared (shallow copy): modifying one node will also change the other. If you want to make a deep copy, use cloneNode().
