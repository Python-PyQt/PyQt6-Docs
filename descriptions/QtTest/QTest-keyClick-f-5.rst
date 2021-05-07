.. sip:method-description::
    :status: todo
    :pysig: f87a8f7e8ce2932757048a1316eab485
    :realsig: (QWidget*,char,Qt::KeyboardModifiers,int)
    :digest: 308663bd08d634d66d7c737fe7f3ae77

This is an overloaded function.

Simulates clicking of *key* with an optional *modifier* on a *widget*. If *delay* is larger than 0, the test will wait for *delay* milliseconds before clicking the key.

Example:

.. literalinclude:: ../../../snippets/qtbase-src-testlib-doc-snippets-code-src_qtestlib_qtestcase_snippet.py
    :lines: 57-57

The example above simulates clicking ``a`` on ``myWidget`` without any keyboard modifiers and without delay of the test.

.. seealso:: :sip:ref:`~PyQt6.QtTest.QTest.keyClicks`.
