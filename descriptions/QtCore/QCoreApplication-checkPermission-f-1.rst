.. sip:method-description::
    :status: todo
    :pysig: 30666f99f745b0b97b7f211ea1ce041d
    :realsig: (const QPermission&)
    :digest: 8792de0c90daf95661fe9bcd21593f8d

Checks the status of the given *permission*

If the result is :sip:ref:`~PyQt6.QtCore.Qt.PermissionStatus.Undetermined` then permission should be requested via :sip:ref:`~PyQt6.QtCore.QCoreApplication.requestPermission` to determine the user's intent.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QCoreApplication.requestPermission`, `Application Permissions <https://doc.qt.io/qt-6/permissions.html>`_.
