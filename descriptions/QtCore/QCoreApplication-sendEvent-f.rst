.. sip:method-description::
    :status: todo
    :pysig: 76d817410820b1644ff5672159e15ab5
    :realsig: (QObject*,QEvent*)
    :digest: d466a136dffcd8f3d268d0e766e6cef9

Sends event *event* directly to receiver *receiver*, using the :sip:ref:`~PyQt6.QtCore.QCoreApplication.notify` function. Returns the value that was returned from the event handler.

The event is *not* deleted when the event has been sent. The normal approach is to create the event on the stack, for example:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_kernel_qcoreapplication.py
    :lines: 54-55

.. seealso:: :sip:ref:`~PyQt6.QtCore.QCoreApplication.postEvent`, :sip:ref:`~PyQt6.QtCore.QCoreApplication.notify`.
