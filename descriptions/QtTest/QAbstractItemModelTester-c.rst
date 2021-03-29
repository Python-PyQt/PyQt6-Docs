.. sip:class-description::
    :status: todo
    :brief: Helps testing QAbstractItemModel subclasses
    :digest: 5d15e8ad2e54ecb888536d261ff0308c

The :sip:ref:`~PyQt6.QtTest.QAbstractItemModelTester` class helps testing :sip:ref:`~PyQt6.QtCore.QAbstractItemModel` subclasses.

The :sip:ref:`~PyQt6.QtTest.QAbstractItemModelTester` class is a utility class to test item models.

When implementing an item model (that is, a concrete :sip:ref:`~PyQt6.QtCore.QAbstractItemModel` subclass) one must abide to a very strict set of rules that ensure consistency for users of the model (views, proxy models, and so on).

For instance, for a given index, a model's reimplementation of :sip:ref:`~PyQt6.QtCore.QAbstractItemModel.hasChildren` must be consistent with the values returned by :sip:ref:`~PyQt6.QtCore.QAbstractItemModel.rowCount` and :sip:ref:`~PyQt6.QtCore.QAbstractItemModel.columnCount`.

:sip:ref:`~PyQt6.QtTest.QAbstractItemModelTester` helps catching the most common errors in custom item model classes. By performing a series of tests, it will try to check that the model status is consistent at all times. The tests will be repeated automatically every time the model is modified.

:sip:ref:`~PyQt6.QtTest.QAbstractItemModelTester` employs non-destructive tests, which typically consist in reading data and metadata out of a given item model. :sip:ref:`~PyQt6.QtTest.QAbstractItemModelTester` will also attempt illegal modifications of the model. In models which are properly implemented, such attempts should be rejected, and no data should be changed as a consequence.

.. _qabstractitemmodeltester-usage:

Usage
-----

Using :sip:ref:`~PyQt6.QtTest.QAbstractItemModelTester` is straightforward. In a `test case <https://doc.qt.io/qt-6/qtest-overview.html>`_ it is sufficient to create an instance, passing the model that needs to be tested to the constructor:

::

    MyModel *modelToBeTested = ...;
    auto tester = new QAbstractItemModelTester(modelToBeTested);

:sip:ref:`~PyQt6.QtTest.QAbstractItemModelTester` will report testing failures through the Qt Test logging mechanisms.

It is also possible to use :sip:ref:`~PyQt6.QtTest.QAbstractItemModelTester` outside of a test case. For instance, it may be useful to test an item model used by an application without the need of building an explicit unit test for such a model (which might be challenging). In order to use :sip:ref:`~PyQt6.QtTest.QAbstractItemModelTester` outside of a test case, pass one of the ``QAbstractItemModelTester::FailureReportingMode`` enumerators to its constructor, therefore specifying how failures should be logged.

:sip:ref:`~PyQt6.QtTest.QAbstractItemModelTester` may also report additional debugging information as logging messages under the ``qt.modeltest`` logging category. Such debug logging is disabled by default; refer to the :sip:ref:`~PyQt6.QtCore.QLoggingCategory` documentation to learn how to enable it.

**Note:** While :sip:ref:`~PyQt6.QtTest.QAbstractItemModelTester` is a valid help for development and testing of custom item models, it does not (and cannot) catch all possible problems in :sip:ref:`~PyQt6.QtCore.QAbstractItemModel` subclasses. Notably, it will never perform meaningful destructive testing of a model, which must be therefore tested separately.

.. seealso:: `Model/View Programming <https://doc.qt.io/qt-6/model-view-programming.html>`_, :sip:ref:`~PyQt6.QtCore.QAbstractItemModel`.
