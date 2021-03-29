.. sip:method-description::
    :status: todo
    :pysig: 341be97d9aff90c9978347f66f945b77
    :realsig: (const QString&)
    :digest: a30e7c434143d99e3ea58bfdee36d06f

Sets the working directory to *dir*. `QProcess <https://doc.qt.io/qt-6/qtcore-changes-qt6.html#qprocess>`_ will start the process in this directory. The default behavior is to start the process in the working directory of the calling process.

**Note:** On QNX, this may cause all application threads to temporarily freeze.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QProcess.workingDirectory`, :sip:ref:`~PyQt6.QtCore.QProcess.start`.
