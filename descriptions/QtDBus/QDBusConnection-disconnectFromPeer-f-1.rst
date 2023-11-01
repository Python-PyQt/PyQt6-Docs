.. sip:method-description::
    :status: todo
    :pysig: c5283bf81cad04335531dd6931c2734d
    :realsig: (const QString&)
    :digest: e060389f6f4df4b0ec1733ab0cbd5b83

Closes the peer connection of name *name*.

Note that if there are still :sip:ref:`~PyQt6.QtDBus.QDBusConnection` objects associated with the same connection, the connection will not be closed until all references are dropped. However, no further references can be created using the :sip:ref:`~PyQt6.QtDBus.QDBusConnection` constructor.
