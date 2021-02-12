.. sip:method-description::
    :status: todo
    :pysig: 9ed0de7ecb17b6432f6443fa97d3d34d
    :realsig: (const QCommandLineOption&) const
    :digest: e80715255fdbf7d72ad9225bba09c5d7

This is an overloaded function.

Checks whether the *option* was passed to the application.

Returns ``true`` if the *option* was set, false otherwise.

This is the recommended way to check for options with no values.

Example:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_tools_qcommandlineparser.py
    :lines: 67-72
