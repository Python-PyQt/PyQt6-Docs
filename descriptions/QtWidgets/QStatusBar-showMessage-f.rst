.. sip:method-description::
    :status: todo
    :pysig: 91f65314a3df41fe525bb3b1c11d6d37
    :realsig: (const QString&, int)
    :digest: 8726c04efb4eed7b32855a31cce3d2f2

Hides the normal status indications and displays the given *message* for the specified number of milli-seconds (\ *timeout*). If *timeout* is 0 (default), the *message* remains displayed until the :sip:ref:`~PyQt6.QtWidgets.QStatusBar.clearMessage` slot is called or until the showMessage() slot is called again to change the message.

Note that showMessage() is called to show temporary explanations of tool tip texts, so passing a *timeout* of 0 is not sufficient to display a :ref:`permanent message<qstatusbar-permanent-message>`.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QStatusBar.messageChanged`, :sip:ref:`~PyQt6.QtWidgets.QStatusBar.currentMessage`, :sip:ref:`~PyQt6.QtWidgets.QStatusBar.clearMessage`.
