.. sip:method-description::
    :status: todo
    :pysig: 341be97d9aff90c9978347f66f945b77
    :realsig: () const
    :digest: 92824d262bb08a5db1eb8c618eac2760

If `QProcess <https://doc.qt.io/qt-6/qtcore-changes-qt6.html#qprocess>`_ has been assigned a working directory, this function returns the working directory that the `QProcess <https://doc.qt.io/qt-6/qtcore-changes-qt6.html#qprocess>`_ will enter before the program has started. Otherwise, (i.e., no directory has been assigned,) an empty string is returned, and `QProcess <https://doc.qt.io/qt-6/qtcore-changes-qt6.html#qprocess>`_ will use the application's current working directory instead.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QProcess.setWorkingDirectory`.
