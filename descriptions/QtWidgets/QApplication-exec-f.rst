.. sip:method-description::
    :status: todo
    :pysig: 5cd04cdbb9ebf068a865ec63c9099761
    :realsig: ()
    :digest: 77190f49b54600fc1d9aecc6c44af791

Enters the main event loop and waits until exit() is called, then returns the value that was set to exit() (which is 0 if exit() is called via quit()).

It is necessary to call this function to start event handling. The main event loop receives events from the window system and dispatches these to the application widgets.

Generally, no user interaction can take place before calling . As a special case, modal widgets like :sip:ref:`~PyQt6.QtWidgets.QMessageBox` can be used before calling , because modal widgets call  to start a local event loop.

To make your application perform idle processing, i.e., executing a special function whenever there are no pending events, use a :sip:ref:`~PyQt6.QtCore.QTimer` with 0 timeout. More advanced idle processing schemes can be achieved using processEvents().

We recommend that you connect clean-up code to the :sip:ref:`~PyQt6.QtCore.QCoreApplication.aboutToQuit` signal, instead of putting it in your application's ``main()`` function. This is because, on some platforms the  call may not return. For example, on the Windows platform, when the user logs off, the system terminates the process after Qt closes all top-level windows. Hence, there is *no guarantee* that the application will have time to exit its event loop and execute code at the end of the ``main()`` function, after the  call.

.. seealso:: quitOnLastWindowClosed, :sip:ref:`~PyQt6.QtCore.QCoreApplication.quit`, :sip:ref:`~PyQt6.QtCore.QCoreApplication.exit`, :sip:ref:`~PyQt6.QtCore.QCoreApplication.processEvents`, :sip:ref:`~PyQt6.QtCore.QCoreApplication.exec`.
