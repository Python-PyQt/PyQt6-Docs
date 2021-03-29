.. sip:class-description::
    :status: todo
    :brief: Convenient way for waiting for asynchronous replies
    :digest: 7c00c9ce799b2d4398a4398654bc0445

The :sip:ref:`~PyQt6.QtDBus.QDBusPendingCallWatcher` class provides a convenient way for waiting for asynchronous replies.

The :sip:ref:`~PyQt6.QtDBus.QDBusPendingCallWatcher` provides the :sip:ref:`~PyQt6.QtDBus.QDBusPendingCallWatcher.finished` signal that will be emitted when a reply arrives.

It is usually used like the following example:

.. literalinclude:: ../../../snippets/qtbase-src-dbus-doc-snippets-code-src_qdbus_qdbuspendingcall.py
    :lines: 82-86

Note that it is not necessary to keep the original :sip:ref:`~PyQt6.QtDBus.QDBusPendingCall` object around since :sip:ref:`~PyQt6.QtDBus.QDBusPendingCallWatcher` inherits from that class too.

The slot connected to by the above code could be something similar to the following:

.. literalinclude:: ../../../snippets/qtbase-src-dbus-doc-snippets-code-src_qdbus_qdbuspendingcall.py
    :lines: 92-103

Note the use of `QDBusPendingReply <https://doc.qt.io/qt-6/dbus-changes-qt6.html#qdbuspendingreply>`_ to validate the argument types in the reply. If the reply did not contain exactly two arguments (one string and one :sip:ref:`~PyQt6.QtCore.QByteArray`), QDBusPendingReply::isError() will return true.

.. seealso:: `QDBusPendingReply <https://doc.qt.io/qt-6/dbus-changes-qt6.html#qdbuspendingreply>`_.
