.. sip:method-description::
    :status: todo
    :pysig: 06b6748bc0d5f7fc977b4321a5de7d3a
    :realsig: (QObject*,QEvent*)
    :digest: 565ed5937799a0a3b241bff98e9b70d0

Filters events if this object has been installed as an event filter for the *watched* object.

In your reimplementation of this function, if you want to filter the *event* out, i.e. stop it being handled further, return true; otherwise return false.

Example:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_kernel_qobject.py
    :lines: 100-134

Notice in the example above that unhandled events are passed to the base class's  function, since the base class might have reimplemented  for its own internal purposes.

Some events, such as :sip:ref:`~PyQt6.QtCore.QEvent.Type.ShortcutOverride` must be explicitly accepted (by calling :sip:ref:`~PyQt6.QtCore.QEvent.accept` on them) in order to prevent propagation.

**Warning:** If you delete the receiver object in this function, be sure to return true. Otherwise, Qt will forward the event to the deleted object and the program might crash.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QObject.installEventFilter`.
