.. sip:method-description::
    :status: todo
    :pysig: 8aa4db8179170d37e11ad02ad96f4d34
    :realsig: (const QStringList&)
    :digest: 54e71322691c47b123655b8e17be04fe

Processes the command line *arguments*.

In addition to parsing the options (like :sip:ref:`~PyQt6.QtCore.QCommandLineParser.parse`), this function also handles the builtin options and handles errors.

The builtin options are ``--version`` if :sip:ref:`~PyQt6.QtCore.QCommandLineParser.addVersionOption` was called and ``--help`` / ``--help-all`` if :sip:ref:`~PyQt6.QtCore.QCommandLineParser.addHelpOption` was called.

When invoking one of these options, or when an error happens (for instance an unknown option was passed), the current process will then stop, using the exit() function.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QCoreApplication.arguments`, :sip:ref:`~PyQt6.QtCore.QCommandLineParser.parse`.
