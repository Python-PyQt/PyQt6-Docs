.. sip:method-description::
    :status: todo
    :pysig: 14cfca2ae20c9a1cdd63b7e4750587c1
    :realsig: () const
    :digest: 93184c446bec79db1e512e21e2d945a3

Returns the environment that `QProcess <https://doc.qt.io/qt-6/qtcore-changes-qt6.html#qprocess>`_ will pass to its child process, or an empty object if no environment has been set using setEnvironment() or :sip:ref:`~PyQt6.QtCore.QProcess.setProcessEnvironment`. If no environment has been set, the environment of the calling process will be used.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QProcess.setProcessEnvironment`, setEnvironment(), :sip:ref:`~PyQt6.QtCore.QProcessEnvironment.isEmpty`.
