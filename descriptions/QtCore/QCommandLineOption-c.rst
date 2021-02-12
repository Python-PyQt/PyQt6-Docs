.. sip:class-description::
    :status: todo
    :brief: Defines a possible command-line option
    :digest: 5db6dbe582bbbc2657983cc6fc43d864

The :sip:ref:`~PyQt6.QtCore.QCommandLineOption` class defines a possible command-line option.

This class is used to describe an option on the command line. It allows different ways of defining the same option with multiple aliases possible. It is also used to describe how the option is used - it may be a flag (e.g. ``-v``) or take a value (e.g. ``-o file``).

Examples:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_tools_qcommandlineoption.py
    :lines: 60-61

.. seealso:: :sip:ref:`~PyQt6.QtCore.QCommandLineParser`.
