.. sip:method-description::
    :status: todo
    :pysig: 5cd04cdbb9ebf068a865ec63c9099761
    :realsig: (int)
    :digest: 4b8f80fe7dca3b0f9909ce46f6854c43

Waits for *msecs*. Equivalent to calling:

::

    QTest::qWait(std::chrono::milliseconds{msecs});
