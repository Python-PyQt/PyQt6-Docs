.. sip:enum-description::
    :status: todo
    :digest: 77b1e94dc99ec03941881f48c0aa7f59

ObjectOwnership controls whether or not the JavaScript memory manager automatically destroys the :sip:ref:`~PyQt6.QtCore.QObject` when the corresponding JavaScript object is garbage collected by the engine. The two ownership options are:

Generally an application doesn't need to set an object's ownership explicitly. The JavaScript memory manager uses a heuristic to set the default ownership. By default, an object that is created by the JavaScript memory manager has JavaScriptOwnership. The exception to this are the root objects created by calling :sip:ref:`~PyQt6.QtQml.QQmlComponent.create` or :sip:ref:`~PyQt6.QtQml.QQmlComponent.beginCreate`, which have CppOwnership by default. The ownership of these root-level objects is considered to have been transferred to the C++ caller.

Objects not-created by the JavaScript memory manager have CppOwnership by default. The exception to this are objects returned from C++ method calls; their ownership will be set to JavaScriptOwnership. This applies only to explicit invocations of Q_INVOKABLE methods or slots, but not to property getter invocations.

Calling :sip:ref:`~PyQt6.QtQml.QJSEngine.setObjectOwnership` overrides the default ownership.

.. seealso:: `Data Ownership <https://doc.qt.io/qt-6/qtqml-cppintegration-data.html#data-ownership>`_.
