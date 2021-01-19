:orphan:

.. sip:module:: PyQt6.QtQml
    :description: QtQml/QtQml-m.rst

    .. sip:method:: PyQt6.QtQml.qjsEngine
        :args:
            :sip:ref:`~PyQt6.QtCore.QObject`
        :returns:
            :sip:ref:`~PyQt6.QtQml.QJSEngine`
        :description: QtQml/qjsEngine-f.rst

    .. sip:method:: PyQt6.QtQml.qmlAttachedPropertiesObject
        :args:
            type
            :sip:ref:`~PyQt6.QtCore.QObject`
            create: bool = True
        :returns:
            :sip:ref:`~PyQt6.QtCore.QObject`
        :description: QtQml/qmlAttachedPropertiesObject-f.rst

    .. sip:method:: PyQt6.QtQml.qmlClearTypeRegistrations
        :description: QtQml/qmlClearTypeRegistrations-f.rst

    .. sip:method:: PyQt6.QtQml.qmlContext
        :args:
            :sip:ref:`~PyQt6.QtCore.QObject`
        :returns:
            :sip:ref:`~PyQt6.QtQml.QQmlContext`
        :description: QtQml/qmlContext-f.rst

    .. sip:method:: PyQt6.QtQml.qmlEngine
        :args:
            :sip:ref:`~PyQt6.QtCore.QObject`
        :returns:
            :sip:ref:`~PyQt6.QtQml.QQmlEngine`
        :description: QtQml/qmlEngine-f.rst

    .. sip:method:: PyQt6.QtQml.qmlProtectModule
        :args:
            str
            int
        :returns:
            bool
        :description: QtQml/qmlProtectModule-f.rst

    .. sip:method:: PyQt6.QtQml.qmlRegisterAnonymousType
        :args:
            type
            str
            int
        :returns:
            int
        :description: QtQml/qmlRegisterAnonymousType-f.rst

    .. sip:method:: PyQt6.QtQml.qmlRegisterModule
        :args:
            str
            int
            int
        :description: QtQml/qmlRegisterModule-f.rst

    .. sip:method:: PyQt6.QtQml.qmlRegisterRevision
        :args:
            type
            str
            int
            int
            attachedProperties: type = 0
        :returns:
            int
        :description: QtQml/qmlRegisterRevision-f.rst

    .. sip:method:: PyQt6.QtQml.qmlRegisterSingletonInstance
        :args:
            str
            int
            int
            str
            :sip:ref:`~PyQt6.QtCore.QObject`
        :returns:
            int
        :description: QtQml/qmlRegisterSingletonInstance-f.rst

    .. sip:method:: PyQt6.QtQml.qmlRegisterSingletonType
        :args:
            :sip:ref:`~PyQt6.QtCore.QUrl`
            str
            int
            int
            str
        :returns:
            int
        :description: QtQml/qmlRegisterSingletonType-f.rst

    .. sip:method:: PyQt6.QtQml.qmlRegisterSingletonType
        :args:
            type
            str
            int
            int
            Callable[[:sip:ref:`~PyQt6.QtQml.QQmlEngine`, :sip:ref:`~PyQt6.QtQml.QJSEngine`], Any]
            name: str = None
        :returns:
            int
        :description: QtQml/qmlRegisterSingletonType-f-1.rst

    .. sip:method:: PyQt6.QtQml.qmlRegisterType
        :args:
            :sip:ref:`~PyQt6.QtCore.QUrl`
            str
            int
            int
            str
        :returns:
            int
        :description: QtQml/qmlRegisterType-f.rst

    .. sip:method:: PyQt6.QtQml.qmlRegisterType
        :args:
            type
            str
            int
            int
            name: str = None
            attachedProperties: type = 0
        :returns:
            int
        :description: QtQml/qmlRegisterType-f-1.rst

    .. sip:method:: PyQt6.QtQml.qmlRegisterTypeNotAvailable
        :args:
            str
            int
            int
            str
            str
        :returns:
            int
        :description: QtQml/qmlRegisterTypeNotAvailable-f.rst

    .. sip:method:: PyQt6.QtQml.qmlRegisterUncreatableMetaObject
        :args:
            :sip:ref:`~PyQt6.QtCore.QMetaObject`
            str
            int
            int
            str
            str
        :returns:
            int
        :description: QtQml/qmlRegisterUncreatableMetaObject-f.rst

    .. sip:method:: PyQt6.QtQml.qmlRegisterUncreatableType
        :args:
            type
            str
            int
            int
            str
            qmlName: str = None
        :returns:
            int
        :description: QtQml/qmlRegisterUncreatableType-f.rst

    .. sip:method:: PyQt6.QtQml.qmlTypeId
        :args:
            str
            int
            int
            str
        :returns:
            int
        :description: QtQml/qmlTypeId-f.rst
