.. sip:method-description::
    :status: todo
    :pysig: 8c461a127e318381f87d6109ff70e0d8
    :realsig: (QAbstractNativeEventFilter*)
    :digest: de6d6b4d02b60c96e1a0636d1c501032

Installs an event filter *filterObj* for all native events received by the application in the main thread.

The event filter *filterObj* receives events via its :sip:ref:`~PyQt6.QtCore.QAbstractNativeEventFilter.nativeEventFilter` function, which is called for all native events received in the main thread.

The :sip:ref:`~PyQt6.QtCore.QAbstractNativeEventFilter.nativeEventFilter` function should return true if the event should be filtered, i.e. stopped. It should return false to allow normal Qt processing to continue: the native event can then be translated into a :sip:ref:`~PyQt6.QtCore.QEvent` and handled by the standard Qt :sip:ref:`~PyQt6.QtCore.QEvent` filtering, e.g. :sip:ref:`~PyQt6.QtCore.QObject.installEventFilter`.

If multiple event filters are installed, the filter that was installed last is activated first.

**Note:** The filter function set here receives native messages, i.e. MSG or XCB event structs.

**Note:** Native event filters will be disabled in the application when the :sip:ref:`~PyQt6.QtCore.Qt.ApplicationAttribute.AA_PluginApplication` attribute is set.

For maximum portability, you should always try to use :sip:ref:`~PyQt6.QtCore.QEvent` and :sip:ref:`~PyQt6.QtCore.QObject.installEventFilter` whenever possible.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QObject.installEventFilter`.
