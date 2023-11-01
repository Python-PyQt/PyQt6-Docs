.. sip:method-description::
    :status: todo
    :pysig: 6fc6e9c01571cdc6b89b4a4db9aea1ac
    :realsig: (const QPermission&)
    :digest: 8792de0c90daf95661fe9bcd21593f8d

Checks the status of the given *permission*

If the result is :sip:ref:`~PyQt6.QtCore.Qt.PermissionStatus.Undetermined` then permission should be requested via :sip:ref:`~PyQt6.QtCore.QCoreApplication.requestPermission` to determine the user's intent.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QCoreApplication.requestPermission`, `Application Permissions <https://doc.qt.io/qt-6/permissions.html>`_.
