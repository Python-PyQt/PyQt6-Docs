:orphan:

.. sip:class:: PyQt6.QtQml.QQmlComponent
    :inherits: :sip:ref:`~PyQt6.QtCore.QObject`
    :description: QtQml/QQmlComponent-c.rst

    .. sip:enum:: PyQt6.QtQml.QQmlComponent.CompilationMode
        :description: QtQml/QQmlComponent-CompilationMode-e.rst

        .. sip:enum-member:: PyQt6.QtQml.QQmlComponent.CompilationMode.Asynchronous
            :description: QtQml/QQmlComponent-CompilationMode-Asynchronous-v.rst

        .. sip:enum-member:: PyQt6.QtQml.QQmlComponent.CompilationMode.PreferSynchronous
            :description: QtQml/QQmlComponent-CompilationMode-PreferSynchronous-v.rst

    .. sip:enum:: PyQt6.QtQml.QQmlComponent.Status
        :description: QtQml/QQmlComponent-Status-e.rst

        .. sip:enum-member:: PyQt6.QtQml.QQmlComponent.Status.Error
            :description: QtQml/QQmlComponent-Status-Error-v.rst

        .. sip:enum-member:: PyQt6.QtQml.QQmlComponent.Status.Loading
            :description: QtQml/QQmlComponent-Status-Loading-v.rst

        .. sip:enum-member:: PyQt6.QtQml.QQmlComponent.Status.Null
            :description: QtQml/QQmlComponent-Status-Null-v.rst

        .. sip:enum-member:: PyQt6.QtQml.QQmlComponent.Status.Ready
            :description: QtQml/QQmlComponent-Status-Ready-v.rst

    .. sip:method:: PyQt6.QtQml.QQmlComponent.__init__
        :args:
            parent: :sip:ref:`~PyQt6.QtCore.QObject` = None
        :description: QtQml/QQmlComponent-__init__-f.rst

    .. sip:method:: PyQt6.QtQml.QQmlComponent.__init__
        :args:
            :sip:ref:`~PyQt6.QtQml.QQmlEngine`
            parent: :sip:ref:`~PyQt6.QtCore.QObject` = None
        :description: QtQml/QQmlComponent-__init__-f-1.rst

    .. sip:method:: PyQt6.QtQml.QQmlComponent.__init__
        :args:
            :sip:ref:`~PyQt6.QtQml.QQmlEngine`
            Optional[str]
            parent: :sip:ref:`~PyQt6.QtCore.QObject` = None
        :description: QtQml/QQmlComponent-__init__-f-8.rst

    .. sip:method:: PyQt6.QtQml.QQmlComponent.__init__
        :args:
            :sip:ref:`~PyQt6.QtQml.QQmlEngine`
            :sip:ref:`~PyQt6.QtCore.QUrl`
            parent: :sip:ref:`~PyQt6.QtCore.QObject` = None
        :description: QtQml/QQmlComponent-__init__-f-3.rst

    .. sip:method:: PyQt6.QtQml.QQmlComponent.__init__
        :args:
            :sip:ref:`~PyQt6.QtQml.QQmlEngine`
            Optional[str]
            :sip:ref:`~PyQt6.QtQml.QQmlComponent.CompilationMode`
            parent: :sip:ref:`~PyQt6.QtCore.QObject` = None
        :description: QtQml/QQmlComponent-__init__-f-9.rst

    .. sip:method:: PyQt6.QtQml.QQmlComponent.__init__
        :args:
            :sip:ref:`~PyQt6.QtQml.QQmlEngine`
            :sip:ref:`~PyQt6.QtCore.QUrl`
            :sip:ref:`~PyQt6.QtQml.QQmlComponent.CompilationMode`
            parent: :sip:ref:`~PyQt6.QtCore.QObject` = None
        :description: QtQml/QQmlComponent-__init__-f-5.rst

    .. sip:method:: PyQt6.QtQml.QQmlComponent.__init__
        :args:
            :sip:ref:`~PyQt6.QtQml.QQmlEngine`
            Union[Union[:sip:ref:`~PyQt6.QtCore.QByteArray`, bytes, bytearray, memoryview], Optional[str]]
            Union[Union[:sip:ref:`~PyQt6.QtCore.QByteArray`, bytes, bytearray, memoryview], Optional[str]]
            parent: :sip:ref:`~PyQt6.QtCore.QObject` = None
        :description: QtQml/QQmlComponent-__init__-f-10.rst

    .. sip:method:: PyQt6.QtQml.QQmlComponent.__init__
        :args:
            :sip:ref:`~PyQt6.QtQml.QQmlEngine`
            Union[Union[:sip:ref:`~PyQt6.QtCore.QByteArray`, bytes, bytearray, memoryview], Optional[str]]
            Union[Union[:sip:ref:`~PyQt6.QtCore.QByteArray`, bytes, bytearray, memoryview], Optional[str]]
            :sip:ref:`~PyQt6.QtQml.QQmlComponent.CompilationMode`
            parent: :sip:ref:`~PyQt6.QtCore.QObject` = None
        :description: QtQml/QQmlComponent-__init__-f-11.rst

    .. sip:method:: PyQt6.QtQml.QQmlComponent.beginCreate
        :args:
            :sip:ref:`~PyQt6.QtQml.QQmlContext`
        :returns:
            :sip:ref:`~PyQt6.QtCore.QObject`
        :description: QtQml/QQmlComponent-beginCreate-f.rst

    .. sip:method:: PyQt6.QtQml.QQmlComponent.completeCreate
        :description: QtQml/QQmlComponent-completeCreate-f.rst

    .. sip:method:: PyQt6.QtQml.QQmlComponent.create
        :args:
            context: :sip:ref:`~PyQt6.QtQml.QQmlContext` = None
        :returns:
            :sip:ref:`~PyQt6.QtCore.QObject`
        :description: QtQml/QQmlComponent-create-f.rst

    .. sip:method:: PyQt6.QtQml.QQmlComponent.create
        :args:
            :sip:ref:`~PyQt6.QtQml.QQmlIncubator`
            context: :sip:ref:`~PyQt6.QtQml.QQmlContext` = None
            forContext: :sip:ref:`~PyQt6.QtQml.QQmlContext` = None
        :description: QtQml/QQmlComponent-create-f-1.rst

    .. sip:method:: PyQt6.QtQml.QQmlComponent.createWithInitialProperties
        :args:
            dict[Optional[str], Any]
            context: :sip:ref:`~PyQt6.QtQml.QQmlContext` = None
        :returns:
            :sip:ref:`~PyQt6.QtCore.QObject`
        :description: QtQml/QQmlComponent-createWithInitialProperties-f.rst

    .. sip:method:: PyQt6.QtQml.QQmlComponent.creationContext
        :returns:
            :sip:ref:`~PyQt6.QtQml.QQmlContext`
        :description: QtQml/QQmlComponent-creationContext-f.rst

    .. sip:method:: PyQt6.QtQml.QQmlComponent.engine
        :returns:
            :sip:ref:`~PyQt6.QtQml.QQmlEngine`
        :description: QtQml/QQmlComponent-engine-f.rst

    .. sip:method:: PyQt6.QtQml.QQmlComponent.errors
        :returns:
            list[:sip:ref:`~PyQt6.QtQml.QQmlError`]
        :description: QtQml/QQmlComponent-errors-f-1.rst

    .. sip:method:: PyQt6.QtQml.QQmlComponent.isBound
        :returns:
            bool
        :description: QtQml/QQmlComponent-isBound-f.rst

    .. sip:method:: PyQt6.QtQml.QQmlComponent.isError
        :returns:
            bool
        :description: QtQml/QQmlComponent-isError-f.rst

    .. sip:method:: PyQt6.QtQml.QQmlComponent.isLoading
        :returns:
            bool
        :description: QtQml/QQmlComponent-isLoading-f.rst

    .. sip:method:: PyQt6.QtQml.QQmlComponent.isNull
        :returns:
            bool
        :description: QtQml/QQmlComponent-isNull-f.rst

    .. sip:method:: PyQt6.QtQml.QQmlComponent.isReady
        :returns:
            bool
        :description: QtQml/QQmlComponent-isReady-f.rst

    .. sip:method:: PyQt6.QtQml.QQmlComponent.loadFromModule
        :args:
            Union[Union[:sip:ref:`~PyQt6.QtCore.QByteArray`, bytes, bytearray, memoryview], Optional[str]]
            Union[Union[:sip:ref:`~PyQt6.QtCore.QByteArray`, bytes, bytearray, memoryview], Optional[str]]
            mode: :sip:ref:`~PyQt6.QtQml.QQmlComponent.CompilationMode` = :sip:ref:`~PyQt6.QtQml.QQmlComponent.CompilationMode.PreferSynchronous`
        :description: QtQml/QQmlComponent-loadFromModule-f-1.rst

    .. sip:method:: PyQt6.QtQml.QQmlComponent.loadUrl
        :args:
            :sip:ref:`~PyQt6.QtCore.QUrl`
        :description: QtQml/QQmlComponent-loadUrl-f.rst

    .. sip:method:: PyQt6.QtQml.QQmlComponent.loadUrl
        :args:
            :sip:ref:`~PyQt6.QtCore.QUrl`
            :sip:ref:`~PyQt6.QtQml.QQmlComponent.CompilationMode`
        :description: QtQml/QQmlComponent-loadUrl-f-1.rst

    .. sip:method:: PyQt6.QtQml.QQmlComponent.progress
        :returns:
            float
        :description: QtQml/QQmlComponent-progress-f.rst

    .. sip:method:: PyQt6.QtQml.QQmlComponent.setData
        :args:
            Union[:sip:ref:`~PyQt6.QtCore.QByteArray`, bytes, bytearray, memoryview]
            :sip:ref:`~PyQt6.QtCore.QUrl`
        :description: QtQml/QQmlComponent-setData-f-1.rst

    .. sip:method:: PyQt6.QtQml.QQmlComponent.setInitialProperties
        :args:
            :sip:ref:`~PyQt6.QtCore.QObject`
            dict[Optional[str], Any]
        :description: QtQml/QQmlComponent-setInitialProperties-f.rst

    .. sip:method:: PyQt6.QtQml.QQmlComponent.status
        :returns:
            :sip:ref:`~PyQt6.QtQml.QQmlComponent.Status`
        :description: QtQml/QQmlComponent-status-f.rst

    .. sip:method:: PyQt6.QtQml.QQmlComponent.url
        :returns:
            :sip:ref:`~PyQt6.QtCore.QUrl`
        :description: QtQml/QQmlComponent-url-f.rst

    .. sip:signal:: PyQt6.QtQml.QQmlComponent.progressChanged
        :args:
            float
        :description: QtQml/QQmlComponent-progressChanged-s.rst

    .. sip:signal:: PyQt6.QtQml.QQmlComponent.statusChanged
        :args:
            :sip:ref:`~PyQt6.QtQml.QQmlComponent.Status`
        :description: QtQml/QQmlComponent-statusChanged-s.rst
