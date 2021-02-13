.. sip:method-description::
    :status: todo
    :pysig: 8e8f4b88dfd741d3d1fbf96a2f3c379c
    :realsig: (const QString&,int)
    :digest: d6608450f38d8d82e24d3a7bc77f8be0

Hides the normal status indications and displays the given *message* for the specified number of milli-seconds (\ *timeout*). If *timeout* is 0 (default), the *message* remains displayed until the :sip:ref:`~PyQt6.QtWidgets.QStatusBar.clearMessage` slot is called or until the  slot is called again to change the message.

Note that  is called to show temporary explanations of tool tip texts, so passing a *timeout* of 0 is not sufficient to display a :ref:`permanent message<qstatusbar-permanent-message>`.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QStatusBar.messageChanged`, :sip:ref:`~PyQt6.QtWidgets.QStatusBar.currentMessage`, :sip:ref:`~PyQt6.QtWidgets.QStatusBar.clearMessage`.
