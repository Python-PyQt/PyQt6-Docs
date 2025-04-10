.. sip:method-description::
    :status: todo
    :pysig: 0dcf7cec6b01c020082ff1e065c7b33f
    :realsig: (QCommandLineParser::MessageType, const QString&, int)
    :digest: ceb154ed4b451bcf841820275a2e3a34

Displays a *message*, and exits the application with the given *exitCode*.

The *message* will usually be printed directly to ``stdout`` or ``stderr`` according to the given *type*, or the message may be shown in a message box under Windows when necessary, with an information icon or error icon according to the given *type* (set the ``QT_COMMAND_LINE_PARSER_NO_GUI_MESSAGE_BOXES`` environment variable if you don't want the message box).

It's the same message display method used by :sip:ref:`~PyQt6.QtCore.QCommandLineParser.showHelp`, :sip:ref:`~PyQt6.QtCore.QCommandLineParser.showVersion` and the builtin options (``--version`` if :sip:ref:`~PyQt6.QtCore.QCommandLineParser.addVersionOption` was called and ``--help`` / ``--help-all`` if :sip:ref:`~PyQt6.QtCore.QCommandLineParser.addHelpOption` was called).

.. seealso:: :sip:ref:`~PyQt6.QtCore.QCommandLineParser.addVersionOption`, :sip:ref:`~PyQt6.QtCore.QCommandLineParser.showHelp`, :sip:ref:`~PyQt6.QtCore.QCommandLineParser.showVersion`, :sip:ref:`~PyQt6.QtCore.QCommandLineParser.MessageType`.
