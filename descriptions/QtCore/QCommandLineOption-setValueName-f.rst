.. sip:method-description::
    :status: todo
    :pysig: 341be97d9aff90c9978347f66f945b77
    :realsig: (const QString&)
    :digest: ab2fc1f08dbff932a27c71b5041469f7

Sets the name of the expected value, for the documentation, to *valueName*.

Options without a value assigned have a boolean-like behavior: either the user specifies –option or they don't.

Options with a value assigned need to set a name for the expected value, for the documentation of the option in the help output. An option with names ``o`` and ``output``, and a value name of ``file`` will appear as ``-o, --output <file>``.

Call :sip:ref:`~PyQt6.QtCore.QCommandLineParser.value` if you expect the option to be present only once, and :sip:ref:`~PyQt6.QtCore.QCommandLineParser.values` if you expect that option to be present multiple times.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QCommandLineOption.valueName`.
