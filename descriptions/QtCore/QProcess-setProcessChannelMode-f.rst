.. sip:method-description::
    :status: todo
    :pysig: 00201edf44348c0108286d30a3664cc5
    :realsig: (QProcess::ProcessChannelMode)
    :digest: 8a43567153b85583f2b098ca5c2b1853

Sets the channel mode of the `QProcess <https://doc.qt.io/qt-6/qtcore-changes-qt6.html#qprocess>`_ standard output and standard error channels to the *mode* specified. This mode will be used the next time :sip:ref:`~PyQt6.QtCore.QProcess.start` is called. For example:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_io_qprocess.py
    :lines: 58-65

.. seealso:: :sip:ref:`~PyQt6.QtCore.QProcess.processChannelMode`, :sip:ref:`~PyQt6.QtCore.QProcess.ProcessChannelMode.ProcessChannelMode`, :sip:ref:`~PyQt6.QtCore.QProcess.setReadChannel`.
