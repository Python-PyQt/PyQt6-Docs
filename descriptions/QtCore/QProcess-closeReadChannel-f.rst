.. sip:method-description::
    :status: todo
    :pysig: f6adb039a52d5725aa12103e458543cc
    :realsig: (QProcess::ProcessChannel)
    :digest: 9d8e60e723ddd368e625c68f7bbd9afc

Closes the read channel *channel*. After calling this function, `QProcess <https://doc.qt.io/qt-6/qtcore-changes-qt6.html#qprocess>`_ will no longer receive data on the channel. Any data that has already been received is still available for reading.

Call this function to save memory, if you are not interested in the output of the process.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QProcess.closeWriteChannel`, :sip:ref:`~PyQt6.QtCore.QProcess.setReadChannel`.
