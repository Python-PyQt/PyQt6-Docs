.. sip:method-description::
    :status: todo
    :pysig: 5cd04cdbb9ebf068a865ec63c9099761
    :realsig: (int)
    :digest: 5bd1ba6cebd69666150a6019e435d0bf

Waits for *ms* milliseconds. While waiting, events will be processed and your test will stay responsive to user interface events or network communication.

Example:

.. literalinclude:: ../../../snippets/qtbase-src-testlib-doc-snippets-code-src_corelib_kernel_qtestsupport_core.py
    :lines: 70-72

The code above will wait until the network server is responding for a maximum of about 12.5 seconds.

.. seealso:: QTest::qSleep(), :sip:ref:`~PyQt6.QtTest.QSignalSpy.wait`.
