.. sip:method-description::
    :status: todo
    :pysig: 8c461a127e318381f87d6109ff70e0d8
    :realsig: (QAbstractNativeEventFilter*)
    :digest: 43befb45ff0a5a03718c3aed4756b0d6

Removes an event *filterObject* from this object. The request is ignored if such an event filter has not been installed.

All event filters for this object are automatically removed when this object is destroyed.

It is always safe to remove an event filter, even during event filter activation (i.e. from the nativeEventFilter() function).

.. seealso:: :sip:ref:`~PyQt6.QtCore.QCoreApplication.installNativeEventFilter`.
