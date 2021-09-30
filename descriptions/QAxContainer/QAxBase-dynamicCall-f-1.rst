.. sip:method-description::
    :status: todo
    :pysig: 6101dd994fbfd9fcdb0c24d8cb1f3516
    :realsig: (const char*,const QVariant&,const QVariant&,const QVariant&,const QVariant&,const QVariant&,const QVariant&,const QVariant&,const QVariant&)
    :digest: bea225ad2ca59bc3bebe3e92674659ae

Calls the COM object's method *function*, passing the parameters *var1*, *var1*, *var2*, *var3*, *var4*, *var5*, *var6*, *var7* and *var8*, and returns the value returned by the method, or an invalid :sip:ref:`~PyQt6.QtCore.QVariant` if the method does not return a value or when the function call failed.

If *function* is a method of the object the string must be provided as the full prototype, for example as it would be written in a QObject::connect() call.

.. literalinclude:: ../../../snippets/qtactiveqt-src-activeqt-doc-snippets-src_activeqt_container_qaxbase.py
    :lines: 160-160

Alternatively a function can be called passing the parameters embedded in the string, e.g. above function can also be invoked using

.. literalinclude:: ../../../snippets/qtactiveqt-src-activeqt-doc-snippets-src_activeqt_container_qaxbase.py
    :lines: 165-165

All parameters are passed as strings; it depends on the control whether they are interpreted correctly, and is slower than using the prototype with correctly typed parameters.

If *function* is a property the string has to be the name of the property. The property setter is called when *var1* is a valid :sip:ref:`~PyQt6.QtCore.QVariant`, otherwise the getter is called.

.. literalinclude:: ../../../snippets/qtactiveqt-src-activeqt-doc-snippets-src_activeqt_container_qaxbase.py
    :lines: 170-171

Note that it is faster to get and set properties using :sip:ref:`~PyQt6.QtCore.QObject.property` and :sip:ref:`~PyQt6.QtCore.QObject.setProperty`.

can also be used to call objects with a :sip:ref:`~PyQt6.QAxContainer.QAxBase.disableMetaObject` wrapper, which can improve performance significantely, esp. when calling many different objects of different types during an automation process. ActiveQt will then however not validate parameters.

It is only possible to call functions through  that have parameters or return values of datatypes supported by :sip:ref:`~PyQt6.QtCore.QVariant`. See the :sip:ref:`~PyQt6.QAxContainer.QAxBase` class documentation for a list of supported and unsupported datatypes. If you want to call functions that have unsupported datatypes in the parameter list, use queryInterface() to retrieve the appropriate COM interface, and use the function directly.

.. literalinclude:: ../../../snippets/qtactiveqt-src-activeqt-doc-snippets-src_activeqt_container_qaxbase.py
    :lines: 176-181

This is also more efficient.
