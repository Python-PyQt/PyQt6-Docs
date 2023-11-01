.. sip:method-description::
    :status: todo
    :pysig: 6068d7d0a63a3b6c588f27ad432df320
    :realsig: (const QByteArray&, const QUrl&)
    :digest: abf3bd67e12bf81779f907363683566d

Loads the QML given in *data*. The object tree defined by *data* is instantiated immediately.

If a *url* is specified it is used as the base url of the component. This affects relative paths within the data and error messages.

If an error occurs, error messages are printed with :sip:ref:`~PyQt6.QtCore.qWarning`.
