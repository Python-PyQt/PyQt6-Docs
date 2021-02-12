.. sip:signal-description::
    :status: todo
    :pysig: 6eb633aab87edefb54c3c04bd6c329f3
    :realsig: (QObject*)
    :digest: 6414d120087e147b78b89e6d40b6053f

This signal is emitted immediately before the object *obj* is destroyed, after any instances of QPointer have been notified, and cannot be blocked.

All the objects's children are destroyed immediately after this signal is emitted.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QObject.deleteLater`, QPointer.
