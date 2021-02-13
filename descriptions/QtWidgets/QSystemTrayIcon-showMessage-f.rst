.. sip:method-description::
    :status: todo
    :pysig: 2ee88c758da2925462d56cc434805bb6
    :realsig: (const QString&,const QString&,QSystemTrayIcon::MessageIcon,int)
    :digest: 9fe634442dde54d0c64c43d95d72fafe

Shows a balloon message for the entry with the given *title*, *message* and *icon* for the time specified in *millisecondsTimeoutHint*. *title* and *message* must be plain text strings.

Message can be clicked by the user; the :sip:ref:`~PyQt6.QtWidgets.QSystemTrayIcon.messageClicked` signal will emitted when this occurs.

Note that display of messages are dependent on the system configuration and user preferences, and that messages may not appear at all. Hence, it should not be relied upon as the sole means for providing critical information.

On Windows, the *millisecondsTimeoutHint* is usually ignored by the system when the application has focus.

Has been turned into a slot in Qt 5.2.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QSystemTrayIcon.show`, :sip:ref:`~PyQt6.QtWidgets.QSystemTrayIcon.supportsMessages`.
