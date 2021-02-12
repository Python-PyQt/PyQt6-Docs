.. sip:method-description::
    :status: todo
    :pysig: c506ff134babdd6e68ab3e6350e95305
    :realsig: (bool)
    :digest: 8e921c98070b0c842c4904f7783ef1e2

Enables auto-deletion if *autoDelete* is true; otherwise auto-deletion is disabled.

If auto-deletion is enabled, :sip:ref:`~PyQt6.QtCore.QThreadPool` will automatically delete this runnable after calling :sip:ref:`~PyQt6.QtCore.QRunnable.run`; otherwise, ownership remains with the application programmer.

Note that this flag must be set before calling :sip:ref:`~PyQt6.QtCore.QThreadPool.start`. Calling this function after :sip:ref:`~PyQt6.QtCore.QThreadPool.start` results in undefined behavior.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QRunnable.autoDelete`, :sip:ref:`~PyQt6.QtCore.QThreadPool`.
