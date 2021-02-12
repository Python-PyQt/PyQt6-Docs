.. sip:method-description::
    :status: todo
    :pysig: 8c461a127e318381f87d6109ff70e0d8
    :realsig: (QAbstractNativeEventFilter*)
    :digest: 347332b6d44faa5b336c978af926ed39

Removes the event filter *filter* from this object. The request is ignored if such an event filter has not been installed.

All event filters for this object are automatically removed when this object is destroyed.

It is always safe to remove an event filter, even during event filter filter activation (that is, even from within the :sip:ref:`~PyQt6.QtCore.QAbstractNativeEventFilter.nativeEventFilter` function).

.. seealso:: :sip:ref:`~PyQt6.QtCore.QAbstractEventDispatcher.installNativeEventFilter`, :sip:ref:`~PyQt6.QtCore.QAbstractNativeEventFilter`.
