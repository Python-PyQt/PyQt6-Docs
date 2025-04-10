.. sip:method-description::
    :status: todo
    :pysig: 84403139209dcd0d8c2c57a139ba22bd
    :realsig: (const QList<QVariant>&)
    :digest: 9037fdc0568df46016eb78bdea0e6edb

Sets the arguments that are going to be sent over D-Bus to *arguments*. Those will be the arguments to a method call or the parameters in the signal.

Note that QVariantMap with invalid :sip:ref:`~PyQt6.QtCore.QVariant` as value is not allowed in *arguments*.

.. seealso:: :sip:ref:`~PyQt6.QtDBus.QDBusMessage.arguments`.
