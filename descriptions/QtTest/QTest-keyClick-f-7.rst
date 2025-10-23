.. sip:method-description::
    :status: todo
    :pysig: 8adf6519edc601294efee9ee2694c93a
    :realsig: (QWindow*,char,Qt::KeyboardModifiers,int)
    :digest: 78af3f0862fb49b7267a564ee60320c3

Simulates clicking of *key* with an optional *modifier* on a *window*. If *delay* is larger than 0, the test will wait for *delay* milliseconds before clicking the key.

Example:

.. literalinclude:: ../../../snippets/qtbase-src-testlib-doc-snippets-code-src_qtestlib_qtestcase_snippet.py
    :lines: 124-125

The example above simulates clicking ``a`` on ``myWindow`` without any keyboard modifiers and without delay of the test.

.. seealso:: :sip:ref:`~PyQt6.QtTest.QTest.keyClicks`.
