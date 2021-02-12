.. sip:method-description::
    :status: todo
    :pysig: 2b9057d9b4a06375acf76e6922f506e2
    :realsig: (QObject*)
    :digest: 863ab2ca5c08b1d8774cbfc7ca034a05

Installs an event filter *filterObj* on this object. For example:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_kernel_qobject.py
    :lines: 209-209

An event filter is an object that receives all events that are sent to this object. The filter can either stop the event or forward it to this object. The event filter *filterObj* receives events via its :sip:ref:`~PyQt6.QtCore.QObject.eventFilter` function. The :sip:ref:`~PyQt6.QtCore.QObject.eventFilter` function must return true if the event should be filtered, (i.e. stopped); otherwise it must return false.

If multiple event filters are installed on a single object, the filter that was installed last is activated first.

Here's a ``KeyPressEater`` class that eats the key presses of its monitored objects:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_kernel_qobject.py
    :lines: 214-233

And here's how to install it on two widgets:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_kernel_qobject.py
    :lines: 238-243

The QShortcut class, for example, uses this technique to intercept shortcut key presses.

**Warning:** If you delete the receiver object in your :sip:ref:`~PyQt6.QtCore.QObject.eventFilter` function, be sure to return true. If you return false, Qt sends the event to the deleted object and the program will crash.

Note that the filtering object must be in the same thread as this object. If *filterObj* is in a different thread, this function does nothing. If either *filterObj* or this object are moved to a different thread after calling this function, the event filter will not be called until both objects have the same thread affinity again (it is *not* removed).

.. seealso:: :sip:ref:`~PyQt6.QtCore.QObject.removeEventFilter`, :sip:ref:`~PyQt6.QtCore.QObject.eventFilter`, :sip:ref:`~PyQt6.QtCore.QObject.event`.
