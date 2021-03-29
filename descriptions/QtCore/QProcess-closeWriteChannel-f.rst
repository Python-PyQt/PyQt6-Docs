.. sip:method-description::
    :status: todo
    :pysig: d41d8cd98f00b204e9800998ecf8427e
    :realsig: ()
    :digest: cc98c2a4c39dbd5680db27c8c577e036

Schedules the write channel of `QProcess <https://doc.qt.io/qt-6/qtcore-changes-qt6.html#qprocess>`_ to be closed. The channel will close once all data has been written to the process. After calling this function, any attempts to write to the process will fail.

Closing the write channel is necessary for programs that read input data until the channel has been closed. For example, the program "more" is used to display text data in a console on both Unix and Windows. But it will not display the text data until `QProcess <https://doc.qt.io/qt-6/qtcore-changes-qt6.html#qprocess>`_'s write channel has been closed. Example:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_io_qprocess.py
    :lines: 70-74

The write channel is implicitly opened when :sip:ref:`~PyQt6.QtCore.QProcess.start` is called.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QProcess.closeReadChannel`.
