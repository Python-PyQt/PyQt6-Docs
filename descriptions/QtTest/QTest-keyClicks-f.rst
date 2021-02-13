.. sip:method-description::
    :status: todo
    :pysig: ab43e1ec5e249b661f37b326a7107294
    :realsig: (QWidget*,const QString&,Qt::KeyboardModifiers,int)
    :digest: 5e4e5e3609e3a870bb96ca15ad4b59cc

Simulates clicking a *sequence* of keys on a *widget*. Optionally, a keyboard *modifier* can be specified as well as a *delay* (in milliseconds) of the test before each key click.

Example:

.. literalinclude:: ../../../snippets/qtbase-src-testlib-doc-snippets-code-src_qtestlib_qtestcase_snippet.py
    :lines: 67-67

The example above simulates clicking the sequence of keys representing "hello world" on ``myWidget`` without any keyboard modifiers and without delay of the test.

.. seealso:: :sip:ref:`~PyQt6.QtTest.QTest.keyClick`.
