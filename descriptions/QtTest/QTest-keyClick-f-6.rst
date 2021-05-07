.. sip:method-description::
    :status: todo
    :pysig: c9c635901822e19896153e6ca8ccfeb4
    :realsig: (QWindow*,Qt::Key,Qt::KeyboardModifiers,int)
    :digest: 1879038169f4738da297ed5c0036a607

This is an overloaded function.

Simulates clicking of *key* with an optional *modifier* on a *window*. If *delay* is larger than 0, the test will wait for *delay* milliseconds before clicking the key.

Examples:

.. literalinclude:: ../../../snippets/qtbase-src-testlib-doc-snippets-code-src_qtestlib_qtestcase_snippet.py
    :lines: 129-130

The first example above simulates clicking the ``escape`` key on ``myWindow`` without any keyboard modifiers and without delay. The second example simulates clicking ``shift-escape`` on ``myWindow`` following a 200 ms delay of the test.

.. seealso:: :sip:ref:`~PyQt6.QtTest.QTest.keyClicks`.
