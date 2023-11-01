.. sip:method-description::
    :status: todo
    :pysig: 2baa7d4269799dd663f70fa7d375a372
    :realsig: (bool, const QByteArray&)
    :digest: 3397cc3359dedd424b73579ebc0a1542

Creates the client site for the ActiveX control, and returns true if the control could be embedded successfully, otherwise returns false. If *initialized* is false the control will be initialized using the *data*. The control will be initialized through either IPersistStreamInit or IPersistStorage interface.

If the control needs to be initialized using custom data, call this function in your reimplementation of initialize(). This function is not called by the default implementation of initialize().
