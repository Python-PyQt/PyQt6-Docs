.. sip:method-description::
    :status: todo
    :pysig: 32587605d4256bf5329850b2da8476d9
    :realsig: (QWidget*,Qt::Key,Qt::KeyboardModifiers,int)
    :digest: b5889017b4c9925563acd79612650efa

Simulates clicking of *key* with an optional *modifier* on a *widget*. If *delay* is larger than 0, the test will wait for *delay* milliseconds before clicking the key.

Examples:

.. literalinclude:: ../../../snippets/qtbase-src-testlib-doc-snippets-code-src_qtestlib_qtestcase_snippet.py
    :lines: 61-63

The first example above simulates clicking the ``escape`` key on ``myWidget`` without any keyboard modifiers and without delay. The second example simulates clicking ``shift-escape`` on ``myWidget`` following a 200 ms delay of the test.

.. seealso:: :sip:ref:`~PyQt6.QtTest.QTest.keyClicks`.
