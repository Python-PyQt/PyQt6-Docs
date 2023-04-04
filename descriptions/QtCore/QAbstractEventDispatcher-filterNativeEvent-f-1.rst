.. sip:method-description::
    :status: todo
    :pysig: 33b0db7fbb72cd3be749c3d8e5e1a1e2
    :realsig: (const QByteArray&,void*,qintptr*)
    :digest: 7be98863f95f2bca2b9444a3a9608c2c

Sends *message* through the event filters that were set by :sip:ref:`~PyQt6.QtCore.QAbstractEventDispatcher.installNativeEventFilter`. This function returns ``true`` as soon as an event filter returns ``true``, and false otherwise to indicate that the processing of the event should continue.

Subclasses of :sip:ref:`~PyQt6.QtCore.QAbstractEventDispatcher` *must* call this function for *all* messages received from the system to ensure compatibility with any extensions that may be used in the application. The type of event *eventType* is specific to the platform plugin chosen at run-time, and can be used to cast message to the right type. The *result* pointer is only used on Windows, and corresponds to the LRESULT pointer.

Note that the type of *message* is platform dependent. See :sip:ref:`~PyQt6.QtCore.QAbstractNativeEventFilter` for details.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QAbstractEventDispatcher.installNativeEventFilter`, :sip:ref:`~PyQt6.QtCore.QAbstractNativeEventFilter.nativeEventFilter`.
