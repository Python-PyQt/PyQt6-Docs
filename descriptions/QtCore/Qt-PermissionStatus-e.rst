.. sip:enum-description::
    :status: todo
    :digest: 904f859799d3acdf89d559a298108c6c

This enum describes the possible statuses of a permissions.

**Note:** On Android, there is no ``Undetermined`` status by the platform's APIs. Thus, if a permission is denied for an app, :sip:ref:`~PyQt6.QtCore.QCoreApplication.checkPermission` returns ``Undetermined`` by default until :sip:ref:`~PyQt6.QtCore.QCoreApplication.requestPermission` is called. After that :sip:ref:`~PyQt6.QtCore.QCoreApplication.checkPermission` reports a non ``Undetermined`` status.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QCoreApplication.requestPermission`, :sip:ref:`~PyQt6.QtCore.QCoreApplication.checkPermission`, `Application Permissions <https://doc.qt.io/qt-6/permissions.html>`_.
