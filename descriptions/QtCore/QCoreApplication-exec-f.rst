.. sip:method-description::
    :status: todo
    :pysig: 5cd04cdbb9ebf068a865ec63c9099761
    :realsig: ()
    :digest: 325df7dba13967b85a9c69cc645d4baa

Enters the main event loop and waits until :sip:ref:`~PyQt6.QtCore.QCoreApplication.exit` is called. Returns the value that was passed to :sip:ref:`~PyQt6.QtCore.QCoreApplication.exit` (which is 0 if :sip:ref:`~PyQt6.QtCore.QCoreApplication.exit` is called via :sip:ref:`~PyQt6.QtCore.QCoreApplication.quit`).

It is necessary to call this function to start event handling. The main event loop receives events from the window system and dispatches these to the application widgets.

To make your application perform idle processing (by executing a special function whenever there are no pending events), use a :sip:ref:`~PyQt6.QtCore.QTimer` with 0 timeout. More advanced idle processing schemes can be achieved using :sip:ref:`~PyQt6.QtCore.QCoreApplication.processEvents`.

We recommend that you connect clean-up code to the :sip:ref:`~PyQt6.QtCore.QCoreApplication.aboutToQuit` signal, instead of putting it in your application's ``main()`` function because on some platforms the  call may not return. For example, on Windows when the user logs off, the system terminates the process after Qt closes all top-level windows. Hence, there is no guarantee that the application will have time to exit its event loop and execute code at the end of the ``main()`` function after the  call.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QCoreApplication.quit`, :sip:ref:`~PyQt6.QtCore.QCoreApplication.exit`, :sip:ref:`~PyQt6.QtCore.QCoreApplication.processEvents`.
