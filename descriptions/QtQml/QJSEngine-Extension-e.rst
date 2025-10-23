.. sip:enum-description::
    :status: todo
    :digest: 0735ab7a885ba761fefb01718c262b9c

This enum is used to specify extensions to be installed via :sip:ref:`~PyQt6.QtQml.QJSEngine.installExtensions`.

**TranslationExtension**

The relation between script translation functions and C++ translation functions is described in the following table:

+--------------------------------------------+-----------------------------------------------------+
| Script Function                            | Corresponding C++ Function                          |
+============================================+=====================================================+
| qsTr()                                     | :sip:ref:`~PyQt6.QtCore.QObject.tr`                 |
+--------------------------------------------+-----------------------------------------------------+
| :sip:ref:`~PyQt6.QtCore.QT_TR_NOOP`        | :sip:ref:`~PyQt6.QtCore.QT_TR_NOOP`                 |
+--------------------------------------------+-----------------------------------------------------+
| qsTranslate()                              | :sip:ref:`~PyQt6.QtCore.QCoreApplication.translate` |
+--------------------------------------------+-----------------------------------------------------+
| :sip:ref:`~PyQt6.QtCore.QT_TRANSLATE_NOOP` | :sip:ref:`~PyQt6.QtCore.QT_TRANSLATE_NOOP`          |
+--------------------------------------------+-----------------------------------------------------+
| qsTrId()                                   | qtTrId()                                            |
+--------------------------------------------+-----------------------------------------------------+
| QT_TRID_NOOP()                             | QT_TRID_NOOP()                                      |
+--------------------------------------------+-----------------------------------------------------+

This flag also adds an ``arg()`` function to the string prototype.

For more information, see the Internationalization with Qt documentation.

**ConsoleExtension**

The `console <https://doc.qt.io/qt-6/qtquick-debugging.html#console-api>`_ object implements a subset of the `Console API <https://developer.mozilla.org/en-US/docs/Web/API/Console>`_, which provides familiar logging functions, such as ``console.log()``.

The list of functions added is as follows:

* ``console.assert()``

* ``console.debug()``

* ``console.exception()``

* ``console.info()``

* ``console.log()`` (equivalent to ``console.debug()``)

* ``console.error()``

* ``console.time()``

* ``console.timeEnd()``

* ``console.trace()``

* ``console.count()``

* ``console.warn()``

* ``print()`` (equivalent to ``console.debug()``)

For more information, see the `Console API <https://doc.qt.io/qt-6/qtquick-debugging.html#console-api>`_ documentation.

**GarbageCollectionExtension**

The ``gc()`` function is equivalent to calling :sip:ref:`~PyQt6.QtQml.QJSEngine.collectGarbage`.
