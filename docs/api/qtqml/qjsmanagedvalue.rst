:orphan:

.. sip:class:: PyQt6.QtQml.QJSManagedValue
    :description: QtQml/QJSManagedValue-c.rst

    .. sip:enum:: PyQt6.QtQml.QJSManagedValue.Type
        :description: QtQml/QJSManagedValue-Type-e.rst

        .. sip:enum-member:: PyQt6.QtQml.QJSManagedValue.Type.Boolean
            :description: QtQml/QJSManagedValue-Type-Boolean-v.rst

        .. sip:enum-member:: PyQt6.QtQml.QJSManagedValue.Type.Function
            :description: QtQml/QJSManagedValue-Type-Function-v.rst

        .. sip:enum-member:: PyQt6.QtQml.QJSManagedValue.Type.Number
            :description: QtQml/QJSManagedValue-Type-Number-v.rst

        .. sip:enum-member:: PyQt6.QtQml.QJSManagedValue.Type.Object
            :description: QtQml/QJSManagedValue-Type-Object-v.rst

        .. sip:enum-member:: PyQt6.QtQml.QJSManagedValue.Type.String
            :description: QtQml/QJSManagedValue-Type-String-v.rst

        .. sip:enum-member:: PyQt6.QtQml.QJSManagedValue.Type.Symbol
            :description: QtQml/QJSManagedValue-Type-Symbol-v.rst

        .. sip:enum-member:: PyQt6.QtQml.QJSManagedValue.Type.Undefined
            :description: QtQml/QJSManagedValue-Type-Undefined-v.rst

    .. sip:method:: PyQt6.QtQml.QJSManagedValue.__init__
        :description: QtQml/QJSManagedValue-__init__-f.rst

    .. sip:method:: PyQt6.QtQml.QJSManagedValue.__init__
        :args:
            Union[:sip:ref:`~PyQt6.QtQml.QJSValue`, :sip:ref:`~PyQt6.QtQml.QJSValue.SpecialValue`, bool, int, float, str]
            :sip:ref:`~PyQt6.QtQml.QJSEngine`
        :description: QtQml/QJSManagedValue-__init__-f-1.rst

    .. sip:method:: PyQt6.QtQml.QJSManagedValue.__init__
        :args:
            :sip:ref:`~PyQt6.QtQml.QJSPrimitiveValue`
            :sip:ref:`~PyQt6.QtQml.QJSEngine`
        :description: QtQml/QJSManagedValue-__init__-f-2.rst

    .. sip:method:: PyQt6.QtQml.QJSManagedValue.__init__
        :args:
            str
            :sip:ref:`~PyQt6.QtQml.QJSEngine`
        :description: QtQml/QJSManagedValue-__init__-f-3.rst

    .. sip:method:: PyQt6.QtQml.QJSManagedValue.__init__
        :args:
            Any
            :sip:ref:`~PyQt6.QtQml.QJSEngine`
        :description: QtQml/QJSManagedValue-__init__-f-4.rst

    .. sip:method:: PyQt6.QtQml.QJSManagedValue.call
        :args:
            arguments: Iterable[Union[:sip:ref:`~PyQt6.QtQml.QJSValue`, :sip:ref:`~PyQt6.QtQml.QJSValue.SpecialValue`, bool, int, float, str]] = []
        :returns:
            :sip:ref:`~PyQt6.QtQml.QJSValue`
        :description: QtQml/QJSManagedValue-call-f.rst

    .. sip:method:: PyQt6.QtQml.QJSManagedValue.callAsConstructor
        :args:
            arguments: Iterable[Union[:sip:ref:`~PyQt6.QtQml.QJSValue`, :sip:ref:`~PyQt6.QtQml.QJSValue.SpecialValue`, bool, int, float, str]] = []
        :returns:
            :sip:ref:`~PyQt6.QtQml.QJSValue`
        :description: QtQml/QJSManagedValue-callAsConstructor-f.rst

    .. sip:method:: PyQt6.QtQml.QJSManagedValue.callWithInstance
        :args:
            Union[:sip:ref:`~PyQt6.QtQml.QJSValue`, :sip:ref:`~PyQt6.QtQml.QJSValue.SpecialValue`, bool, int, float, str]
            arguments: Iterable[Union[:sip:ref:`~PyQt6.QtQml.QJSValue`, :sip:ref:`~PyQt6.QtQml.QJSValue.SpecialValue`, bool, int, float, str]] = []
        :returns:
            :sip:ref:`~PyQt6.QtQml.QJSValue`
        :description: QtQml/QJSManagedValue-callWithInstance-f.rst

    .. sip:method:: PyQt6.QtQml.QJSManagedValue.deleteProperty
        :args:
            str
        :returns:
            bool
        :description: QtQml/QJSManagedValue-deleteProperty-f.rst

    .. sip:method:: PyQt6.QtQml.QJSManagedValue.deleteProperty
        :args:
            int
        :returns:
            bool
        :description: QtQml/QJSManagedValue-deleteProperty-f-1.rst

    .. sip:method:: PyQt6.QtQml.QJSManagedValue.engine
        :returns:
            :sip:ref:`~PyQt6.QtQml.QJSEngine`
        :description: QtQml/QJSManagedValue-engine-f.rst

    .. sip:method:: PyQt6.QtQml.QJSManagedValue.equals
        :args:
            :sip:ref:`~PyQt6.QtQml.QJSManagedValue`
        :returns:
            bool
        :description: QtQml/QJSManagedValue-equals-f.rst

    .. sip:method:: PyQt6.QtQml.QJSManagedValue.hasOwnProperty
        :args:
            str
        :returns:
            bool
        :description: QtQml/QJSManagedValue-hasOwnProperty-f.rst

    .. sip:method:: PyQt6.QtQml.QJSManagedValue.hasOwnProperty
        :args:
            int
        :returns:
            bool
        :description: QtQml/QJSManagedValue-hasOwnProperty-f-1.rst

    .. sip:method:: PyQt6.QtQml.QJSManagedValue.hasProperty
        :args:
            str
        :returns:
            bool
        :description: QtQml/QJSManagedValue-hasProperty-f.rst

    .. sip:method:: PyQt6.QtQml.QJSManagedValue.hasProperty
        :args:
            int
        :returns:
            bool
        :description: QtQml/QJSManagedValue-hasProperty-f-1.rst

    .. sip:method:: PyQt6.QtQml.QJSManagedValue.isArray
        :returns:
            bool
        :description: QtQml/QJSManagedValue-isArray-f.rst

    .. sip:method:: PyQt6.QtQml.QJSManagedValue.isBoolean
        :returns:
            bool
        :description: QtQml/QJSManagedValue-isBoolean-f.rst

    .. sip:method:: PyQt6.QtQml.QJSManagedValue.isDate
        :returns:
            bool
        :description: QtQml/QJSManagedValue-isDate-f.rst

    .. sip:method:: PyQt6.QtQml.QJSManagedValue.isError
        :returns:
            bool
        :description: QtQml/QJSManagedValue-isError-f.rst

    .. sip:method:: PyQt6.QtQml.QJSManagedValue.isFunction
        :returns:
            bool
        :description: QtQml/QJSManagedValue-isFunction-f.rst

    .. sip:method:: PyQt6.QtQml.QJSManagedValue.isInteger
        :returns:
            bool
        :description: QtQml/QJSManagedValue-isInteger-f.rst

    .. sip:method:: PyQt6.QtQml.QJSManagedValue.isNull
        :returns:
            bool
        :description: QtQml/QJSManagedValue-isNull-f.rst

    .. sip:method:: PyQt6.QtQml.QJSManagedValue.isNumber
        :returns:
            bool
        :description: QtQml/QJSManagedValue-isNumber-f.rst

    .. sip:method:: PyQt6.QtQml.QJSManagedValue.isObject
        :returns:
            bool
        :description: QtQml/QJSManagedValue-isObject-f.rst

    .. sip:method:: PyQt6.QtQml.QJSManagedValue.isQMetaObject
        :returns:
            bool
        :description: QtQml/QJSManagedValue-isQMetaObject-f.rst

    .. sip:method:: PyQt6.QtQml.QJSManagedValue.isQObject
        :returns:
            bool
        :description: QtQml/QJSManagedValue-isQObject-f.rst

    .. sip:method:: PyQt6.QtQml.QJSManagedValue.isRegularExpression
        :returns:
            bool
        :description: QtQml/QJSManagedValue-isRegularExpression-f.rst

    .. sip:method:: PyQt6.QtQml.QJSManagedValue.isString
        :returns:
            bool
        :description: QtQml/QJSManagedValue-isString-f.rst

    .. sip:method:: PyQt6.QtQml.QJSManagedValue.isSymbol
        :returns:
            bool
        :description: QtQml/QJSManagedValue-isSymbol-f.rst

    .. sip:method:: PyQt6.QtQml.QJSManagedValue.isUndefined
        :returns:
            bool
        :description: QtQml/QJSManagedValue-isUndefined-f.rst

    .. sip:method:: PyQt6.QtQml.QJSManagedValue.isUrl
        :returns:
            bool
        :description: QtQml/QJSManagedValue-isUrl-f.rst

    .. sip:method:: PyQt6.QtQml.QJSManagedValue.isVariant
        :returns:
            bool
        :description: QtQml/QJSManagedValue-isVariant-f.rst

    .. sip:method:: PyQt6.QtQml.QJSManagedValue.property
        :args:
            str
        :returns:
            :sip:ref:`~PyQt6.QtQml.QJSValue`
        :description: QtQml/QJSManagedValue-property-f.rst

    .. sip:method:: PyQt6.QtQml.QJSManagedValue.property
        :args:
            int
        :returns:
            :sip:ref:`~PyQt6.QtQml.QJSValue`
        :description: QtQml/QJSManagedValue-property-f-1.rst

    .. sip:method:: PyQt6.QtQml.QJSManagedValue.prototype
        :returns:
            :sip:ref:`~PyQt6.QtQml.QJSManagedValue`
        :description: QtQml/QJSManagedValue-prototype-f.rst

    .. sip:method:: PyQt6.QtQml.QJSManagedValue.setProperty
        :args:
            str
            Union[:sip:ref:`~PyQt6.QtQml.QJSValue`, :sip:ref:`~PyQt6.QtQml.QJSValue.SpecialValue`, bool, int, float, str]
        :description: QtQml/QJSManagedValue-setProperty-f.rst

    .. sip:method:: PyQt6.QtQml.QJSManagedValue.setProperty
        :args:
            int
            Union[:sip:ref:`~PyQt6.QtQml.QJSValue`, :sip:ref:`~PyQt6.QtQml.QJSValue.SpecialValue`, bool, int, float, str]
        :description: QtQml/QJSManagedValue-setProperty-f-1.rst

    .. sip:method:: PyQt6.QtQml.QJSManagedValue.setPrototype
        :args:
            :sip:ref:`~PyQt6.QtQml.QJSManagedValue`
        :description: QtQml/QJSManagedValue-setPrototype-f.rst

    .. sip:method:: PyQt6.QtQml.QJSManagedValue.strictlyEquals
        :args:
            :sip:ref:`~PyQt6.QtQml.QJSManagedValue`
        :returns:
            bool
        :description: QtQml/QJSManagedValue-strictlyEquals-f.rst

    .. sip:method:: PyQt6.QtQml.QJSManagedValue.toBoolean
        :returns:
            bool
        :description: QtQml/QJSManagedValue-toBoolean-f.rst

    .. sip:method:: PyQt6.QtQml.QJSManagedValue.toDateTime
        :returns:
            :sip:ref:`~PyQt6.QtCore.QDateTime`
        :description: QtQml/QJSManagedValue-toDateTime-f.rst

    .. sip:method:: PyQt6.QtQml.QJSManagedValue.toInteger
        :returns:
            int
        :description: QtQml/QJSManagedValue-toInteger-f.rst

    .. sip:method:: PyQt6.QtQml.QJSManagedValue.toJSValue
        :returns:
            :sip:ref:`~PyQt6.QtQml.QJSValue`
        :description: QtQml/QJSManagedValue-toJSValue-f.rst

    .. sip:method:: PyQt6.QtQml.QJSManagedValue.toNumber
        :returns:
            float
        :description: QtQml/QJSManagedValue-toNumber-f.rst

    .. sip:method:: PyQt6.QtQml.QJSManagedValue.toPrimitive
        :returns:
            :sip:ref:`~PyQt6.QtQml.QJSPrimitiveValue`
        :description: QtQml/QJSManagedValue-toPrimitive-f.rst

    .. sip:method:: PyQt6.QtQml.QJSManagedValue.toQMetaObject
        :returns:
            :sip:ref:`~PyQt6.QtCore.QMetaObject`
        :description: QtQml/QJSManagedValue-toQMetaObject-f.rst

    .. sip:method:: PyQt6.QtQml.QJSManagedValue.toQObject
        :returns:
            :sip:ref:`~PyQt6.QtCore.QObject`
        :description: QtQml/QJSManagedValue-toQObject-f.rst

    .. sip:method:: PyQt6.QtQml.QJSManagedValue.toRegularExpression
        :returns:
            :sip:ref:`~PyQt6.QtCore.QRegularExpression`
        :description: QtQml/QJSManagedValue-toRegularExpression-f.rst

    .. sip:method:: PyQt6.QtQml.QJSManagedValue.toString
        :returns:
            str
        :description: QtQml/QJSManagedValue-toString-f.rst

    .. sip:method:: PyQt6.QtQml.QJSManagedValue.toUrl
        :returns:
            :sip:ref:`~PyQt6.QtCore.QUrl`
        :description: QtQml/QJSManagedValue-toUrl-f.rst

    .. sip:method:: PyQt6.QtQml.QJSManagedValue.toVariant
        :returns:
            Any
        :description: QtQml/QJSManagedValue-toVariant-f.rst

    .. sip:method:: PyQt6.QtQml.QJSManagedValue.type
        :returns:
            :sip:ref:`~PyQt6.QtQml.QJSManagedValue.Type`
        :description: QtQml/QJSManagedValue-type-f.rst
