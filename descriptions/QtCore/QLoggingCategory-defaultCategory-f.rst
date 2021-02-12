.. sip:method-description::
    :status: todo
    :pysig: b40bd04ab3d6257db81e414ee8cf2370
    :realsig: ()
    :digest: c2cee9e26f4830279b031c10ba56ac7f

Returns a pointer to the global category ``"default"`` that is used, for example, by :sip:ref:`~PyQt6.QtCore.qDebug`, :sip:ref:`~PyQt6.QtCore.qInfo`, :sip:ref:`~PyQt6.QtCore.qWarning`, :sip:ref:`~PyQt6.QtCore.qCritical`, or :sip:ref:`~PyQt6.QtCore.qFatal`.

**Note:** The pointer returned may be null during destruction of static objects. Also, don't ``delete`` this pointer, as ownership of the category isn't transferred.
