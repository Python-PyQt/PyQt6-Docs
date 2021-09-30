.. sip:method-description::
    :status: todo
    :pysig: d41d8cd98f00b204e9800998ecf8427e
    :realsig: ()
    :digest: d5765925fde447adbf14917283ae83d8

Disables the meta object generation for this ActiveX container. This also disables the event sink and class info generation. If you don't intend to use the Qt meta object implementation call this function to speed up instantiation of the control. You will still be able to call the object through :sip:ref:`~PyQt6.QAxContainer.QAxBase.dynamicCall`, but signals, slots and properties will not be available with :sip:ref:`~PyQt6.QtCore.QObject` APIs.

Some ActiveX controls might be unstable when used with OLE automation. Use standard COM methods to use those controls through the COM interfaces provided by queryInterface().

Note that this function must be called immediately after construction of the object.
