.. sip:class-description::
    :status: todo
    :brief: Enables introspection of signal emission
    :digest: c3aeff486a0c18b98415569d67eb21f0

The :sip:ref:`~PyQt6.QtTest.QSignalSpy` class enables introspection of signal emission.

:sip:ref:`~PyQt6.QtTest.QSignalSpy` can connect to any signal of any object and records its emission. :sip:ref:`~PyQt6.QtTest.QSignalSpy` itself is a list of `QVariant <https://doc.qt.io/qt-6/qtcore-changes-qt6.html#qvariant>`_ lists. Each emission of the signal will append one item to the list, containing the arguments of the signal.

The following example records all signal emissions for the ``clicked()`` signal of a :sip:ref:`~PyQt6.QtWidgets.QCheckBox`:

.. literalinclude:: ../../../snippets/qtbase-src-testlib-doc-snippets-code-doc_src_qsignalspy.py
    :lines: 54-63

``spy.takeFirst()`` returns the arguments for the first emitted signal, as a list of `QVariant <https://doc.qt.io/qt-6/qtcore-changes-qt6.html#qvariant>`_ objects. The ``clicked()`` signal has a single bool argument, which is stored as the first entry in the list of arguments.

The example below catches a signal from a custom object:

.. literalinclude:: ../../../snippets/qtbase-src-testlib-doc-snippets-code-doc_src_qsignalspy.py
    :lines: 68-75

**Note:** Non-standard data types need to be registered, using the qRegisterMetaType() function, before you can create a :sip:ref:`~PyQt6.QtTest.QSignalSpy`. For example:

.. literalinclude:: ../../../snippets/qtbase-src-testlib-doc-snippets-code-doc_src_qsignalspy.py
    :lines: 80-81

To retrieve the instance, you can use qvariant_cast:

.. literalinclude:: ../../../snippets/qtbase-src-testlib-doc-snippets-code-doc_src_qsignalspy.py
    :lines: 86-87

.. _qsignalspy-verifying-signal-emissions:

Verifying Signal Emissions
--------------------------

The :sip:ref:`~PyQt6.QtTest.QSignalSpy` class provides an elegant mechanism for capturing the list of signals emitted by an object. However, you should verify its validity after construction. The constructor does a number of sanity checks, such as verifying that the signal to be spied upon actually exists. To make the diagnosis of test failures easier, the results of these checks should be checked by calling ``QVERIFY(spy.isValid())`` before proceeding further with a test.

.. seealso:: QVERIFY().
