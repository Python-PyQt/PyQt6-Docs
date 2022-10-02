.. sip:enum-description::
    :status: todo
    :digest: 777ea439676b23c7dad5cc7863be4b33

This enum describes the process output channel modes of :sip:ref:`~PyQt6.QtCore.QProcess`. Pass one of these values to :sip:ref:`~PyQt6.QtCore.QProcess.setProcessChannelMode` to set the current read channel mode.

**Note:** Windows intentionally suppresses output from GUI-only applications to inherited consoles. This does *not* apply to output redirected to files or pipes. To forward the output of GUI-only applications on the console nonetheless, you must use SeparateChannels and do the forwarding yourself by reading the output and writing it to the appropriate output channels.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QProcess.setProcessChannelMode`.
