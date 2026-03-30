.. sip:signal-description::
    :status: todo
    :pysig: b130f021e23bcdbb3df5f92815c8803f
    :realsig: (int, const QString&, const QString&, const QString&)
    :digest: 09c0b911d8096b4835441d582f6306ff

This signal is emitted when the COM object throws an exception while called using the OLE automation interface IDispatch. *code*, *source*, *desc* and *help* provide information about the exception as provided by the COM server and can be used to provide useful feedback to the end user. *help* includes the help file, and the help context ID in brackets, e.g. "filename [id]".

.. seealso:: :sip:ref:`~PyQt6.QAxContainer.QAxBaseObject.exception`.
