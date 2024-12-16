.. sip:method-description::
    :status: todo
    :pysig: 5cd04cdbb9ebf068a865ec63c9099761
    :realsig: ()
    :digest: fc5d2bea044884f1d658c740d662b89b

Enters the main event loop and waits until :sip:ref:`~PyQt6.QtCore.QCoreApplication.exit` is called. Returns the value that was passed to :sip:ref:`~PyQt6.QtCore.QCoreApplication.exit` (which is 0 if :sip:ref:`~PyQt6.QtCore.QCoreApplication.exit` is called via :sip:ref:`~PyQt6.QtCore.QCoreApplication.quit`).

It is necessary to call this function to start event handling. The main event loop receives events from the window system and dispatches these to the application widgets.

To make your application perform idle processing (by executing a special function whenever there are no pending events), use a QChronoTimer with 0ns timeout. More advanced idle processing schemes can be achieved using :sip:ref:`~PyQt6.QtCore.QCoreApplication.processEvents`.

We recommend that you connect clean-up code to the :sip:ref:`~PyQt6.QtCore.QCoreApplication.aboutToQuit` signal, instead of putting it in your application's ``main()`` function because on some platforms the exec() call may not return. For example, on Windows when the user logs off, the system terminates the process after Qt closes all top-level windows. Hence, there is no guarantee that the application will have time to exit its event loop and execute code at the end of the ``main()`` function after the exec() call.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QCoreApplication.quit`, :sip:ref:`~PyQt6.QtCore.QCoreApplication.exit`, :sip:ref:`~PyQt6.QtCore.QCoreApplication.processEvents`, :sip:ref:`~PyQt6.QtWidgets.QApplication.exec`.
