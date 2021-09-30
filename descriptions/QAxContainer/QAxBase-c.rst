.. sip:class-description::
    :status: todo
    :brief: Abstract class that provides an API to initialize and access a COM object
    :digest: 9c7fcb7ca489332226198a6847ed6309

The :sip:ref:`~PyQt6.QAxContainer.QAxBase` class is an abstract class that provides an API to initialize and access a COM object.

:sip:ref:`~PyQt6.QAxContainer.QAxBase` is an abstract class that cannot be used directly, and is instantiated through the subclasses :sip:ref:`~PyQt6.QAxContainer.QAxObject` and :sip:ref:`~PyQt6.QAxContainer.QAxWidget`. This class provides the API to access the COM object directly through its IUnknown implementation. If the COM object implements the IDispatch interface, the properties and methods of that object become available as Qt properties and slots.

.. literalinclude:: ../../../snippets/qtactiveqt-src-activeqt-doc-snippets-src_activeqt_container_qaxbase.py
    :lines: 54-54

Properties exposed by the object's IDispatch implementation can be read and written through the property system provided by the Qt Object Model (both subclasses are :sip:ref:`~PyQt6.QtCore.QObject`\ s, so you can use :sip:ref:`~PyQt6.QtCore.QObject.setProperty` and :sip:ref:`~PyQt6.QtCore.QObject.property`). Properties with multiple parameters are not supported.

.. literalinclude:: ../../../snippets/qtactiveqt-src-activeqt-doc-snippets-src_activeqt_container_qaxbase.py
    :lines: 59-60

Write-functions for properties and other methods exposed by the object's IDispatch implementation can be called directly using :sip:ref:`~PyQt6.QAxContainer.QAxBase.dynamicCall`, or indirectly as slots connected to a signal.

.. literalinclude:: ../../../snippets/qtactiveqt-src-activeqt-doc-snippets-src_activeqt_container_qaxbase.py
    :lines: 65-65

Outgoing events supported by the COM object are emitted as standard Qt signals.

.. literalinclude:: ../../../snippets/qtactiveqt-src-activeqt-doc-snippets-src_activeqt_container_qaxbase.py
    :lines: 70-71

:sip:ref:`~PyQt6.QAxContainer.QAxBase` transparently converts between COM data types and the equivalent Qt data types. Some COM types have no equivalent Qt data structure.

Supported COM datatypes are listed in the first column of following table. The second column is the Qt type that can be used with the :sip:ref:`~PyQt6.QtCore.QObject` property functions. The third column is the Qt type that is used in the prototype of generated signals and slots for in-parameters, and the last column is the Qt type that is used in the prototype of signals and slots for out-parameters.

+----------------------------------------------------+--------------------------------------------+---------------------------------------------------+-----------------------------------------------------------+
| COM type                                           | Qt property                                | in-parameter                                      | out-parameter                                             |
+====================================================+============================================+===================================================+===========================================================+
| VARIANT_BOOL                                       | bool                                       | bool                                              | bool&                                                     |
+----------------------------------------------------+--------------------------------------------+---------------------------------------------------+-----------------------------------------------------------+
| BSTR                                               | QString                                    | const QString&                                    | QString&                                                  |
+----------------------------------------------------+--------------------------------------------+---------------------------------------------------+-----------------------------------------------------------+
| char, short, int, long                             | int                                        | int                                               | int&                                                      |
+----------------------------------------------------+--------------------------------------------+---------------------------------------------------+-----------------------------------------------------------+
| uchar, ushort, uint, ulong                         | uint                                       | uint                                              | uint&                                                     |
+----------------------------------------------------+--------------------------------------------+---------------------------------------------------+-----------------------------------------------------------+
| float, double                                      | double                                     | double                                            | double&                                                   |
+----------------------------------------------------+--------------------------------------------+---------------------------------------------------+-----------------------------------------------------------+
| DATE                                               | :sip:ref:`~PyQt6.QtCore.QDateTime`         | const :sip:ref:`~PyQt6.QtCore.QDateTime`&         | :sip:ref:`~PyQt6.QtCore.QDateTime`&                       |
+----------------------------------------------------+--------------------------------------------+---------------------------------------------------+-----------------------------------------------------------+
| CY                                                 | qlonglong                                  | qlonglong                                         | qlonglong&                                                |
+----------------------------------------------------+--------------------------------------------+---------------------------------------------------+-----------------------------------------------------------+
| OLE_COLOR                                          | :sip:ref:`~PyQt6.QtGui.QColor`             | const :sip:ref:`~PyQt6.QtGui.QColor`&             | :sip:ref:`~PyQt6.QtGui.QColor`&                           |
+----------------------------------------------------+--------------------------------------------+---------------------------------------------------+-----------------------------------------------------------+
| SAFEARRAY(VARIANT)                                 | QList<\ :sip:ref:`~PyQt6.QtCore.QVariant`> | const QList<\ :sip:ref:`~PyQt6.QtCore.QVariant`>& | QList<\ :sip:ref:`~PyQt6.QtCore.QVariant`>&               |
+----------------------------------------------------+--------------------------------------------+---------------------------------------------------+-----------------------------------------------------------+
| SAFEARRAY(int), SAFEARRAY(double), SAFEARRAY(Date) | QList<\ :sip:ref:`~PyQt6.QtCore.QVariant`> | const QList<\ :sip:ref:`~PyQt6.QtCore.QVariant`>& | QList<\ :sip:ref:`~PyQt6.QtCore.QVariant`>&               |
+----------------------------------------------------+--------------------------------------------+---------------------------------------------------+-----------------------------------------------------------+
| SAFEARRAY(BYTE)                                    | :sip:ref:`~PyQt6.QtCore.QByteArray`        | const :sip:ref:`~PyQt6.QtCore.QByteArray`&        | :sip:ref:`~PyQt6.QtCore.QByteArray`&                      |
+----------------------------------------------------+--------------------------------------------+---------------------------------------------------+-----------------------------------------------------------+
| SAFEARRAY(BSTR)                                    | QStringList                                | const QStringList&                                | QStringList&                                              |
+----------------------------------------------------+--------------------------------------------+---------------------------------------------------+-----------------------------------------------------------+
| VARIANT                                            | type-dependent                             | const :sip:ref:`~PyQt6.QtCore.QVariant`&          | :sip:ref:`~PyQt6.QtCore.QVariant`&                        |
+----------------------------------------------------+--------------------------------------------+---------------------------------------------------+-----------------------------------------------------------+
| IFontDisp\*                                        | :sip:ref:`~PyQt6.QtGui.QFont`              | const :sip:ref:`~PyQt6.QtGui.QFont`&              | :sip:ref:`~PyQt6.QtGui.QFont`&                            |
+----------------------------------------------------+--------------------------------------------+---------------------------------------------------+-----------------------------------------------------------+
| IPictureDisp\*                                     | :sip:ref:`~PyQt6.QtGui.QPixmap`            | const :sip:ref:`~PyQt6.QtGui.QPixmap`&            | :sip:ref:`~PyQt6.QtGui.QPixmap`&                          |
+----------------------------------------------------+--------------------------------------------+---------------------------------------------------+-----------------------------------------------------------+
| IDispatch\*                                        | :sip:ref:`~PyQt6.QAxContainer.QAxObject`\* | ``QAxBase::asVariant()``                          | :sip:ref:`~PyQt6.QAxContainer.QAxObject`\* (return value) |
+----------------------------------------------------+--------------------------------------------+---------------------------------------------------+-----------------------------------------------------------+
| IUnknown\*                                         | :sip:ref:`~PyQt6.QAxContainer.QAxObject`\* | ``QAxBase::asVariant()``                          | :sip:ref:`~PyQt6.QAxContainer.QAxObject`\* (return value) |
+----------------------------------------------------+--------------------------------------------+---------------------------------------------------+-----------------------------------------------------------+
| SCODE, DECIMAL                                     | *unsupported*                              | *unsupported*                                     | *unsupported*                                             |
+----------------------------------------------------+--------------------------------------------+---------------------------------------------------+-----------------------------------------------------------+
| VARIANT\* (Since Qt 4.5)                           | *unsupported*                              | *QVariant&*                                       | *QVariant&*                                               |
+----------------------------------------------------+--------------------------------------------+---------------------------------------------------+-----------------------------------------------------------+

Supported are also enumerations, and typedefs to supported types.

To call the methods of a COM interface described by the following IDL

.. literalinclude:: ../../../snippets/qtactiveqt-src-activeqt-doc-snippets-src_activeqt_container_qaxbase.py
    :lines: 76-87

use the :sip:ref:`~PyQt6.QAxContainer.QAxBase` API like this:

.. literalinclude:: ../../../snippets/qtactiveqt-src-activeqt-doc-snippets-src_activeqt_container_qaxbase.py
    :lines: 92-105

Note that the QList the object should fill has to be provided as an element in the parameter list of :sip:ref:`~PyQt6.QtCore.QVariant`\ s.

If you need to access properties or pass parameters of unsupported datatypes you must access the COM object directly through its ``IDispatch`` implementation or other interfaces. Those interfaces can be retrieved through queryInterface().

.. literalinclude:: ../../../snippets/qtactiveqt-src-activeqt-doc-snippets-src_activeqt_container_qaxbase.py
    :lines: 110-115

To get the definition of the COM interfaces you will have to use the header files provided with the component you want to use. Some compilers can also import type libraries using the #import compiler directive. See the component documentation to find out which type libraries you have to import, and how to use them.

If you need to react to events that pass parameters of unsupported datatypes you can use the generic signal that delivers the event data as provided by the COM event.

.. seealso:: :sip:ref:`~PyQt6.QAxContainer.QAxObject`, :sip:ref:`~PyQt6.QAxContainer.QAxWidget`, QAxScript, `ActiveQt Framework <https://doc.qt.io/qt-6/activeqt-index.html>`_.
