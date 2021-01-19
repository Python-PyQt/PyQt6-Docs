:orphan:

.. sip:class:: PyQt6.QtQml.QJSValue
    :description: QtQml/QJSValue-c.rst

    .. sip:enum:: PyQt6.QtQml.QJSValue.ErrorType
        :description: QtQml/QJSValue-ErrorType-e.rst

        .. sip:enum-member:: PyQt6.QtQml.QJSValue.ErrorType.EvalError
            :description: QtQml/QJSValue-ErrorType-EvalError-v.rst

        .. sip:enum-member:: PyQt6.QtQml.QJSValue.ErrorType.GenericError
            :description: QtQml/QJSValue-ErrorType-GenericError-v.rst

        .. sip:enum-member:: PyQt6.QtQml.QJSValue.ErrorType.RangeError
            :description: QtQml/QJSValue-ErrorType-RangeError-v.rst

        .. sip:enum-member:: PyQt6.QtQml.QJSValue.ErrorType.ReferenceError
            :description: QtQml/QJSValue-ErrorType-ReferenceError-v.rst

        .. sip:enum-member:: PyQt6.QtQml.QJSValue.ErrorType.SyntaxError
            :description: QtQml/QJSValue-ErrorType-SyntaxError-v.rst

        .. sip:enum-member:: PyQt6.QtQml.QJSValue.ErrorType.TypeError
            :description: QtQml/QJSValue-ErrorType-TypeError-v.rst

        .. sip:enum-member:: PyQt6.QtQml.QJSValue.ErrorType.URIError
            :description: QtQml/QJSValue-ErrorType-URIError-v.rst

    .. sip:enum:: PyQt6.QtQml.QJSValue.SpecialValue
        :description: QtQml/QJSValue-SpecialValue-e.rst

        .. sip:enum-member:: PyQt6.QtQml.QJSValue.SpecialValue.NullValue
            :description: QtQml/QJSValue-SpecialValue-NullValue-v.rst

        .. sip:enum-member:: PyQt6.QtQml.QJSValue.SpecialValue.UndefinedValue
            :description: QtQml/QJSValue-SpecialValue-UndefinedValue-v.rst

    .. sip:method:: PyQt6.QtQml.QJSValue.__init__
        :args:
            value: :sip:ref:`~PyQt6.QtQml.QJSValue.SpecialValue` = :sip:ref:`~PyQt6.QtQml.QJSValue.SpecialValue.UndefinedValue`
        :description: QtQml/QJSValue-__init__-f.rst

    .. sip:method:: PyQt6.QtQml.QJSValue.__init__
        :args:
            Union[:sip:ref:`~PyQt6.QtQml.QJSValue`, :sip:ref:`~PyQt6.QtQml.QJSValue.SpecialValue`, bool, int, float, str]
        :description: QtQml/QJSValue-__init__-f-1.rst

    .. sip:method:: PyQt6.QtQml.QJSValue.call
        :args:
            args: Iterable[Union[:sip:ref:`~PyQt6.QtQml.QJSValue`, :sip:ref:`~PyQt6.QtQml.QJSValue.SpecialValue`, bool, int, float, str]] = []
        :returns:
            :sip:ref:`~PyQt6.QtQml.QJSValue`
        :description: QtQml/QJSValue-call-f.rst

    .. sip:method:: PyQt6.QtQml.QJSValue.callAsConstructor
        :args:
            args: Iterable[Union[:sip:ref:`~PyQt6.QtQml.QJSValue`, :sip:ref:`~PyQt6.QtQml.QJSValue.SpecialValue`, bool, int, float, str]] = []
        :returns:
            :sip:ref:`~PyQt6.QtQml.QJSValue`
        :description: QtQml/QJSValue-callAsConstructor-f.rst

    .. sip:method:: PyQt6.QtQml.QJSValue.callWithInstance
        :args:
            Union[:sip:ref:`~PyQt6.QtQml.QJSValue`, :sip:ref:`~PyQt6.QtQml.QJSValue.SpecialValue`, bool, int, float, str]
            args: Iterable[Union[:sip:ref:`~PyQt6.QtQml.QJSValue`, :sip:ref:`~PyQt6.QtQml.QJSValue.SpecialValue`, bool, int, float, str]] = []
        :returns:
            :sip:ref:`~PyQt6.QtQml.QJSValue`
        :description: QtQml/QJSValue-callWithInstance-f.rst

    .. sip:method:: PyQt6.QtQml.QJSValue.deleteProperty
        :args:
            str
        :returns:
            bool
        :description: QtQml/QJSValue-deleteProperty-f.rst

    .. sip:method:: PyQt6.QtQml.QJSValue.equals
        :args:
            Union[:sip:ref:`~PyQt6.QtQml.QJSValue`, :sip:ref:`~PyQt6.QtQml.QJSValue.SpecialValue`, bool, int, float, str]
        :returns:
            bool
        :description: QtQml/QJSValue-equals-f.rst

    .. sip:method:: PyQt6.QtQml.QJSValue.errorType
        :returns:
            :sip:ref:`~PyQt6.QtQml.QJSValue.ErrorType`
        :description: QtQml/QJSValue-errorType-f.rst

    .. sip:method:: PyQt6.QtQml.QJSValue.hasOwnProperty
        :args:
            str
        :returns:
            bool
        :description: QtQml/QJSValue-hasOwnProperty-f.rst

    .. sip:method:: PyQt6.QtQml.QJSValue.hasProperty
        :args:
            str
        :returns:
            bool
        :description: QtQml/QJSValue-hasProperty-f.rst

    .. sip:method:: PyQt6.QtQml.QJSValue.isArray
        :returns:
            bool
        :description: QtQml/QJSValue-isArray-f.rst

    .. sip:method:: PyQt6.QtQml.QJSValue.isBool
        :returns:
            bool
        :description: QtQml/QJSValue-isBool-f.rst

    .. sip:method:: PyQt6.QtQml.QJSValue.isCallable
        :returns:
            bool
        :description: QtQml/QJSValue-isCallable-f.rst

    .. sip:method:: PyQt6.QtQml.QJSValue.isDate
        :returns:
            bool
        :description: QtQml/QJSValue-isDate-f.rst

    .. sip:method:: PyQt6.QtQml.QJSValue.isError
        :returns:
            bool
        :description: QtQml/QJSValue-isError-f.rst

    .. sip:method:: PyQt6.QtQml.QJSValue.isNull
        :returns:
            bool
        :description: QtQml/QJSValue-isNull-f.rst

    .. sip:method:: PyQt6.QtQml.QJSValue.isNumber
        :returns:
            bool
        :description: QtQml/QJSValue-isNumber-f.rst

    .. sip:method:: PyQt6.QtQml.QJSValue.isObject
        :returns:
            bool
        :description: QtQml/QJSValue-isObject-f.rst

    .. sip:method:: PyQt6.QtQml.QJSValue.isQObject
        :returns:
            bool
        :description: QtQml/QJSValue-isQObject-f.rst

    .. sip:method:: PyQt6.QtQml.QJSValue.isRegExp
        :returns:
            bool
        :description: QtQml/QJSValue-isRegExp-f.rst

    .. sip:method:: PyQt6.QtQml.QJSValue.isString
        :returns:
            bool
        :description: QtQml/QJSValue-isString-f.rst

    .. sip:method:: PyQt6.QtQml.QJSValue.isUndefined
        :returns:
            bool
        :description: QtQml/QJSValue-isUndefined-f.rst

    .. sip:method:: PyQt6.QtQml.QJSValue.isVariant
        :returns:
            bool
        :description: QtQml/QJSValue-isVariant-f.rst

    .. sip:method:: PyQt6.QtQml.QJSValue.property
        :args:
            str
        :returns:
            :sip:ref:`~PyQt6.QtQml.QJSValue`
        :description: QtQml/QJSValue-property-f.rst

    .. sip:method:: PyQt6.QtQml.QJSValue.property
        :args:
            int
        :returns:
            :sip:ref:`~PyQt6.QtQml.QJSValue`
        :description: QtQml/QJSValue-property-f-1.rst

    .. sip:method:: PyQt6.QtQml.QJSValue.prototype
        :returns:
            :sip:ref:`~PyQt6.QtQml.QJSValue`
        :description: QtQml/QJSValue-prototype-f.rst

    .. sip:method:: PyQt6.QtQml.QJSValue.setProperty
        :args:
            str
            Union[:sip:ref:`~PyQt6.QtQml.QJSValue`, :sip:ref:`~PyQt6.QtQml.QJSValue.SpecialValue`, bool, int, float, str]
        :description: QtQml/QJSValue-setProperty-f.rst

    .. sip:method:: PyQt6.QtQml.QJSValue.setProperty
        :args:
            int
            Union[:sip:ref:`~PyQt6.QtQml.QJSValue`, :sip:ref:`~PyQt6.QtQml.QJSValue.SpecialValue`, bool, int, float, str]
        :description: QtQml/QJSValue-setProperty-f-1.rst

    .. sip:method:: PyQt6.QtQml.QJSValue.setPrototype
        :args:
            Union[:sip:ref:`~PyQt6.QtQml.QJSValue`, :sip:ref:`~PyQt6.QtQml.QJSValue.SpecialValue`, bool, int, float, str]
        :description: QtQml/QJSValue-setPrototype-f.rst

    .. sip:method:: PyQt6.QtQml.QJSValue.strictlyEquals
        :args:
            Union[:sip:ref:`~PyQt6.QtQml.QJSValue`, :sip:ref:`~PyQt6.QtQml.QJSValue.SpecialValue`, bool, int, float, str]
        :returns:
            bool
        :description: QtQml/QJSValue-strictlyEquals-f.rst

    .. sip:method:: PyQt6.QtQml.QJSValue.toBool
        :returns:
            bool
        :description: QtQml/QJSValue-toBool-f.rst

    .. sip:method:: PyQt6.QtQml.QJSValue.toDateTime
        :returns:
            :sip:ref:`~PyQt6.QtCore.QDateTime`
        :description: QtQml/QJSValue-toDateTime-f.rst

    .. sip:method:: PyQt6.QtQml.QJSValue.toInt
        :returns:
            int
        :description: QtQml/QJSValue-toInt-f.rst

    .. sip:method:: PyQt6.QtQml.QJSValue.toNumber
        :returns:
            float
        :description: QtQml/QJSValue-toNumber-f.rst

    .. sip:method:: PyQt6.QtQml.QJSValue.toQObject
        :returns:
            :sip:ref:`~PyQt6.QtCore.QObject`
        :description: QtQml/QJSValue-toQObject-f.rst

    .. sip:method:: PyQt6.QtQml.QJSValue.toString
        :returns:
            str
        :description: QtQml/QJSValue-toString-f.rst

    .. sip:method:: PyQt6.QtQml.QJSValue.toUInt
        :returns:
            int
        :description: QtQml/QJSValue-toUInt-f.rst

    .. sip:method:: PyQt6.QtQml.QJSValue.toVariant
        :returns:
            Any
        :description: QtQml/QJSValue-toVariant-f.rst
