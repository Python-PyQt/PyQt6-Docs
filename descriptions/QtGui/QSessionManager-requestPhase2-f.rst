.. sip:method-description::
    :status: todo
    :pysig: d41d8cd98f00b204e9800998ecf8427e
    :realsig: ()
    :digest: f4a13c85f867505cd91649d2fc7a0917

Requests a second session management phase for the application. The application may then return immediately from the :sip:ref:`~PyQt6.QtGui.QGuiApplication.commitDataRequest` or QApplication::saveStateRequest() function, and they will be called again once most or all other applications have finished their session management.

The two phases are useful for applications such as the X11 window manager that need to store information about another application's windows and therefore have to wait until these applications have completed their respective session management tasks.

**Note:** If another application has requested a second phase it may get called before, simultaneously with, or after your application's second phase.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QSessionManager.isPhase2`.
