.. sip:method-description::
    :status: todo
    :pysig: d41d8cd98f00b204e9800998ecf8427e
    :realsig: ()
    :digest: 79b02516c1af8eab46c24c3d1be9f162

Disables the event sink implementation for this ActiveX container. If you don't intend to listen to the ActiveX control's events use this function to speed up the meta object generation.

Some ActiveX controls might be unstable when connected to an event sink. To get OLE events you must use standard COM methods to register your own event sink. Use queryInterface() to get access to the raw COM object.

Note that this function should be called immediately after construction of the object.
