.. sip:method-description::
    :status: todo
    :pysig: 6a478baa52f796fd984a858dba37cac2
    :realsig: (QProcess*)
    :digest: a928662b165058a6997086f593404210

Pipes the standard output stream of this process to the *destination* process' standard input.

The following shell command:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_io_qprocess.py
    :lines: 79-79

Can be accomplished with `QProcess <https://doc.qt.io/qt-6/qtcore-changes-qt6.html#qprocess>`_ with the following code:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_io_qprocess.py
    :lines: 84-90
