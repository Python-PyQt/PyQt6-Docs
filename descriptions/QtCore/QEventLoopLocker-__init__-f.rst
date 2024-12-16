.. sip:method-description::
    :status: todo
    :pysig: d41d8cd98f00b204e9800998ecf8427e
    :realsig: ()
    :digest: 325fb1504973a559141ced82d627f16f

Creates an event locker operating on the :sip:ref:`~PyQt6.QtCore.QCoreApplication`.

The application will attempt to quit when there are no more QEventLoopLockers operating on it, as long as :sip:ref:`~PyQt6.QtCore.QCoreApplication.isQuitLockEnabled` is ``true``.

Note that attempting a quit may not necessarily result in the application quitting, if there for example are open windows, or the :sip:ref:`~PyQt6.QtCore.QEvent.Type.Quit` event is ignored.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QCoreApplication.quit`, :sip:ref:`~PyQt6.QtCore.QCoreApplication.isQuitLockEnabled`.
