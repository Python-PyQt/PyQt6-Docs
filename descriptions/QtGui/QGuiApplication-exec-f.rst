.. sip:method-description::
    :status: todo
    :pysig: 5cd04cdbb9ebf068a865ec63c9099761
    :realsig: ()
    :digest: c2e76f2c719808d1cef49f8f1befbfb6

Enters the main event loop and waits until exit() is called, and then returns the value that was set to exit() (which is 0 if exit() is called via quit()).

It is necessary to call this function to start event handling. The main event loop receives events from the window system and dispatches these to the application widgets.

Generally, no user interaction can take place before calling exec().

To make your application perform idle processing, e.g., executing a special function whenever there are no pending events, use a QChronoTimer with 0ns timeout. More advanced idle processing schemes can be achieved using processEvents().

We recommend that you connect clean-up code to the :sip:ref:`~PyQt6.QtCore.QCoreApplication.aboutToQuit` signal, instead of putting it in your application's ``main()`` function. This is because, on some platforms, the :sip:ref:`~PyQt6.QtWidgets.QApplication.exec` call may not return.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QGuiApplication.quitOnLastWindowClosed`, quit(), exit(), processEvents(), :sip:ref:`~PyQt6.QtCore.QCoreApplication.exec`.
