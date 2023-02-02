:orphan:

.. sip:class:: PyQt6.QtQml.QJSEngine
    :inherits: :sip:ref:`~PyQt6.QtCore.QObject`
    :description: QtQml/QJSEngine-c.rst

    .. sip:enum:: PyQt6.QtQml.QJSEngine.Extension
        :description: QtQml/QJSEngine-Extension-e.rst

        .. sip:enum-member:: PyQt6.QtQml.QJSEngine.Extension.AllExtensions
            :description: QtQml/QJSEngine-Extension-AllExtensions-v.rst

        .. sip:enum-member:: PyQt6.QtQml.QJSEngine.Extension.ConsoleExtension
            :description: QtQml/QJSEngine-Extension-ConsoleExtension-v.rst

        .. sip:enum-member:: PyQt6.QtQml.QJSEngine.Extension.GarbageCollectionExtension
            :description: QtQml/QJSEngine-Extension-GarbageCollectionExtension-v.rst

        .. sip:enum-member:: PyQt6.QtQml.QJSEngine.Extension.TranslationExtension
            :description: QtQml/QJSEngine-Extension-TranslationExtension-v.rst

    .. sip:enum:: PyQt6.QtQml.QJSEngine.ObjectOwnership
        :description: QtQml/QJSEngine-ObjectOwnership-e.rst

        .. sip:enum-member:: PyQt6.QtQml.QJSEngine.ObjectOwnership.CppOwnership
            :description: QtQml/QJSEngine-ObjectOwnership-CppOwnership-v.rst

        .. sip:enum-member:: PyQt6.QtQml.QJSEngine.ObjectOwnership.JavaScriptOwnership
            :description: QtQml/QJSEngine-ObjectOwnership-JavaScriptOwnership-v.rst

    .. sip:method:: PyQt6.QtQml.QJSEngine.__init__
        :description: QtQml/QJSEngine-__init__-f.rst

    .. sip:method:: PyQt6.QtQml.QJSEngine.__init__
        :args:
            :sip:ref:`~PyQt6.QtCore.QObject`
        :description: QtQml/QJSEngine-__init__-f-1.rst

    .. sip:method:: PyQt6.QtQml.QJSEngine.catchError
        :returns:
            :sip:ref:`~PyQt6.QtQml.QJSValue`
        :description: QtQml/QJSEngine-catchError-f.rst

    .. sip:method:: PyQt6.QtQml.QJSEngine.collectGarbage
        :description: QtQml/QJSEngine-collectGarbage-f.rst

    .. sip:method:: PyQt6.QtQml.QJSEngine.evaluate
        :args:
            str
            fileName: str = ''
            lineNumber: int = 1
            exceptionStackTrace: List[str] = None
        :returns:
            :sip:ref:`~PyQt6.QtQml.QJSValue`
        :description: QtQml/QJSEngine-evaluate-f-1.rst

    .. sip:method:: PyQt6.QtQml.QJSEngine.globalObject
        :returns:
            :sip:ref:`~PyQt6.QtQml.QJSValue`
        :description: QtQml/QJSEngine-globalObject-f.rst

    .. sip:method:: PyQt6.QtQml.QJSEngine.hasError
        :returns:
            bool
        :description: QtQml/QJSEngine-hasError-f.rst

    .. sip:method:: PyQt6.QtQml.QJSEngine.importModule
        :args:
            str
        :returns:
            :sip:ref:`~PyQt6.QtQml.QJSValue`
        :description: QtQml/QJSEngine-importModule-f.rst

    .. sip:method:: PyQt6.QtQml.QJSEngine.installExtensions
        :args:
            :sip:ref:`~PyQt6.QtQml.QJSEngine.Extension`
            object: Union[:sip:ref:`~PyQt6.QtQml.QJSValue`, :sip:ref:`~PyQt6.QtQml.QJSValue.SpecialValue`, bool, int, float, str] = QJSValue()
        :description: QtQml/QJSEngine-installExtensions-f-1.rst

    .. sip:method:: PyQt6.QtQml.QJSEngine.isInterrupted
        :returns:
            bool
        :description: QtQml/QJSEngine-isInterrupted-f.rst

    .. sip:method:: PyQt6.QtQml.QJSEngine.newArray
        :args:
            length: int = 0
        :returns:
            :sip:ref:`~PyQt6.QtQml.QJSValue`
        :description: QtQml/QJSEngine-newArray-f.rst

    .. sip:method:: PyQt6.QtQml.QJSEngine.newErrorObject
        :args:
            :sip:ref:`~PyQt6.QtQml.QJSValue.ErrorType`
            message: str = ''
        :returns:
            :sip:ref:`~PyQt6.QtQml.QJSValue`
        :description: QtQml/QJSEngine-newErrorObject-f.rst

    .. sip:method:: PyQt6.QtQml.QJSEngine.newObject
        :returns:
            :sip:ref:`~PyQt6.QtQml.QJSValue`
        :description: QtQml/QJSEngine-newObject-f.rst

    .. sip:method:: PyQt6.QtQml.QJSEngine.newQMetaObject
        :args:
            :sip:ref:`~PyQt6.QtCore.QMetaObject`
        :returns:
            :sip:ref:`~PyQt6.QtQml.QJSValue`
        :description: QtQml/QJSEngine-newQMetaObject-f.rst

    .. sip:method:: PyQt6.QtQml.QJSEngine.newQObject
        :args:
            :sip:ref:`~PyQt6.QtCore.QObject`
        :returns:
            :sip:ref:`~PyQt6.QtQml.QJSValue`
        :description: QtQml/QJSEngine-newQObject-f.rst

    .. sip:method:: PyQt6.QtQml.QJSEngine.newSymbol
        :args:
            str
        :returns:
            :sip:ref:`~PyQt6.QtQml.QJSValue`
        :description: QtQml/QJSEngine-newSymbol-f.rst

    .. sip:method:: PyQt6.QtQml.QJSEngine.objectOwnership
        :args:
            :sip:ref:`~PyQt6.QtCore.QObject`
        :returns:
            :sip:ref:`~PyQt6.QtQml.QJSEngine.ObjectOwnership`
        :static:
        :description: QtQml/QJSEngine-objectOwnership-f.rst

    .. sip:method:: PyQt6.QtQml.QJSEngine.registerModule
        :args:
            str
            Union[:sip:ref:`~PyQt6.QtQml.QJSValue`, :sip:ref:`~PyQt6.QtQml.QJSValue.SpecialValue`, bool, int, float, str]
        :returns:
            bool
        :description: QtQml/QJSEngine-registerModule-f.rst

    .. sip:method:: PyQt6.QtQml.QJSEngine.setInterrupted
        :args:
            bool
        :description: QtQml/QJSEngine-setInterrupted-f.rst

    .. sip:method:: PyQt6.QtQml.QJSEngine.setObjectOwnership
        :args:
            :sip:ref:`~PyQt6.QtCore.QObject`
            :sip:ref:`~PyQt6.QtQml.QJSEngine.ObjectOwnership`
        :static:
        :description: QtQml/QJSEngine-setObjectOwnership-f.rst

    .. sip:method:: PyQt6.QtQml.QJSEngine.setUiLanguage
        :args:
            str
        :description: QtQml/QJSEngine-setUiLanguage-f.rst

    .. sip:method:: PyQt6.QtQml.QJSEngine.throwError
        :args:
            str
        :description: QtQml/QJSEngine-throwError-f.rst

    .. sip:method:: PyQt6.QtQml.QJSEngine.throwError
        :args:
            Union[:sip:ref:`~PyQt6.QtQml.QJSValue`, :sip:ref:`~PyQt6.QtQml.QJSValue.SpecialValue`, bool, int, float, str]
        :description: QtQml/QJSEngine-throwError-f-2.rst

    .. sip:method:: PyQt6.QtQml.QJSEngine.throwError
        :args:
            :sip:ref:`~PyQt6.QtQml.QJSValue.ErrorType`
            message: str = ''
        :description: QtQml/QJSEngine-throwError-f-1.rst

    .. sip:method:: PyQt6.QtQml.QJSEngine.uiLanguage
        :returns:
            str
        :description: QtQml/QJSEngine-uiLanguage-f.rst

    .. sip:signal:: PyQt6.QtQml.QJSEngine.uiLanguageChanged
        :description: QtQml/QJSEngine-uiLanguageChanged-s.rst
