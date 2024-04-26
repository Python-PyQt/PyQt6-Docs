.. sip:method-description::
    :status: todo
    :pysig: 5cd04cdbb9ebf068a865ec63c9099761
    :realsig: (int)
    :digest: 26904e5c4fc4129c6ebab9089c71e8a1

This is an overloaded function.

Waits for *msecs*. Equivalent to calling:

::

    QTest::qWait(std::chrono::milliseconds{msecs});
