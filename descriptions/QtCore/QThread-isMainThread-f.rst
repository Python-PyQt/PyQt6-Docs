.. sip:method-description::
    :status: todo
    :pysig: 01111d32dddd979ac6254452ab6fef9b
    :realsig: ()
    :digest: a973c735b28e40abe35995e1c9f77b62

Returns whether the currently executing thread is the main thread.

The main thread is the thread in which :sip:ref:`~PyQt6.QtCore.QCoreApplication` was created. This is usually the thread that called the ``main()`` function, but not necessarily so. It is the thread that is processing the GUI events and in which graphical objects (\ :sip:ref:`~PyQt6.QtGui.QWindow`, :sip:ref:`~PyQt6.QtWidgets.QWidget`) can be created.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QThread.currentThread`, :sip:ref:`~PyQt6.QtCore.QCoreApplication.instance`.
