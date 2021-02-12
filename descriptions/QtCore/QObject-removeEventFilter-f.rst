.. sip:method-description::
    :status: todo
    :pysig: 2b9057d9b4a06375acf76e6922f506e2
    :realsig: (QObject*)
    :digest: 4ef90f604d26dba355b2e9fa17c9d6ef

Removes an event filter object *obj* from this object. The request is ignored if such an event filter has not been installed.

All event filters for this object are automatically removed when this object is destroyed.

It is always safe to remove an event filter, even during event filter activation (i.e. from the :sip:ref:`~PyQt6.QtCore.QObject.eventFilter` function).

.. seealso:: :sip:ref:`~PyQt6.QtCore.QObject.installEventFilter`, :sip:ref:`~PyQt6.QtCore.QObject.eventFilter`, :sip:ref:`~PyQt6.QtCore.QObject.event`.
