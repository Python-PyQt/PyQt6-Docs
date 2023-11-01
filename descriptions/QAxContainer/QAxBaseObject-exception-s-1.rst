.. sip:signal-description::
    :status: todo
    :pysig: d995e10e17643812384d25fd617c0920
    :realsig: (int, const QString&, const QString&, const QString&)
    :digest: 40feb1499314389f11b15b6ea9533b67

This signal is emitted when the COM object throws an exception while called using the OLE automation interface IDispatch. *code*, *source*, *desc* and *help* provide information about the exception as provided by the COM server and can be used to provide useful feedback to the end user. *help* includes the help file, and the help context ID in brackets, e.g. "filename [id]".

.. seealso:: :sip:ref:`~PyQt6.QAxContainer.QAxBaseWidget.exception`.
