.. sip:signal-description::
    :status: todo
    :pysig: 43d61033588da017976faab5a1a69e7b
    :realsig: (QQuickCloseEvent*)
    :digest: a219188fc724f11d6f7513242c54655b

This signal is emitted when the window receives the event *close* from the windowing system.

On macOs, Qt will create a menu item ``Quit`` if there is no menu item whose text is "quit" or "exit". This menu item calls the ``QCoreApplication::quit`` signal, not the ``QQuickWindow::closing()`` signal.

.. seealso:: QMenuBar as a Global Menu Bar.
