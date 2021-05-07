.. sip:method-description::
    :status: todo
    :pysig: 8adf6519edc601294efee9ee2694c93a
    :realsig: (QWindow*,char,Qt::KeyboardModifiers,int)
    :digest: 0f5118488d136b7f372a3c2d642211f2

This is an overloaded function.

Simulates clicking of *key* with an optional *modifier* on a *window*. If *delay* is larger than 0, the test will wait for *delay* milliseconds before clicking the key.

Example:

.. literalinclude:: ../../../snippets/qtbase-src-testlib-doc-snippets-code-src_qtestlib_qtestcase_snippet.py
    :lines: 124-125

The example above simulates clicking ``a`` on ``myWindow`` without any keyboard modifiers and without delay of the test.

.. seealso:: :sip:ref:`~PyQt6.QtTest.QTest.keyClicks`.
