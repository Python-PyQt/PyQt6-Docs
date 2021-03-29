.. sip:method-description::
    :status: todo
    :pysig: 2c3a85170feb55541a292cc0c7316b09
    :realsig: ()
    :digest: 53f894c824f4ec46ef691682ad720a7f

Returns a `QDBusConnection <https://doc.qt.io/qt-6/dbus-changes-qt6.html#qdbusconnection>`_ object opened with the system bus. The object reference returned by this function is valid until the :sip:ref:`~PyQt6.QtCore.QCoreApplication`'s destructor is run, when the connection will be closed and the object, deleted.
