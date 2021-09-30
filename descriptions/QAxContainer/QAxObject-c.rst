.. sip:class-description::
    :status: todo
    :brief: QObject that wraps a COM object
    :digest: 1cf0328447d8f777e141f032b6189703

The :sip:ref:`~PyQt6.QAxContainer.QAxObject` class provides a :sip:ref:`~PyQt6.QtCore.QObject` that wraps a COM object.

A :sip:ref:`~PyQt6.QAxContainer.QAxObject` can be instantiated as an empty object, with the name of the COM object it should wrap, or with a pointer to the IUnknown that represents an existing COM object. If the COM object implements the ``IDispatch`` interface, the properties, methods and events of that object become available as Qt properties, slots and signals. The base class, :sip:ref:`~PyQt6.QAxContainer.QAxBase`, provides an API to access the COM object directly through the IUnknown pointer.

:sip:ref:`~PyQt6.QAxContainer.QAxObject` is a :sip:ref:`~PyQt6.QtCore.QObject` and can be used as such, e.g. it can be organized in an object hierarchy, receive events and connect to signals and slots.

:sip:ref:`~PyQt6.QAxContainer.QAxObject` also inherits most of its ActiveX-related functionality from :sip:ref:`~PyQt6.QAxContainer.QAxBase`, notably dynamicCall() and querySubObject().

**Warning:** You can subclass :sip:ref:`~PyQt6.QAxContainer.QAxObject`, but you cannot use the Q_OBJECT macro in the subclass (the generated moc-file will not compile), so you cannot add further signals, slots or properties. This limitation is due to the metaobject information generated in runtime. To work around this problem, aggregate the :sip:ref:`~PyQt6.QAxContainer.QAxObject` as a member of the :sip:ref:`~PyQt6.QtCore.QObject` subclass.

.. seealso:: :sip:ref:`~PyQt6.QAxContainer.QAxBase`, :sip:ref:`~PyQt6.QAxContainer.QAxWidget`, QAxScript, `ActiveQt Framework <https://doc.qt.io/qt-6/activeqt-index.html>`_.
