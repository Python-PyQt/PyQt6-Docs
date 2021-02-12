.. sip:method-description::
    :status: todo
    :pysig: c506ff134babdd6e68ab3e6350e95305
    :realsig: () const
    :digest: ee2ebe29d07e1dce5356c8377cf4ebcb

Returns ``true`` is auto-deletion is enabled; false otherwise.

If auto-deletion is enabled, :sip:ref:`~PyQt6.QtCore.QThreadPool` will automatically delete this runnable after calling :sip:ref:`~PyQt6.QtCore.QRunnable.run`; otherwise, ownership remains with the application programmer.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QRunnable.setAutoDelete`, :sip:ref:`~PyQt6.QtCore.QThreadPool`.
