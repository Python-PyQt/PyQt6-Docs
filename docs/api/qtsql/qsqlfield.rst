:orphan:

.. sip:class:: PyQt6.QtSql.QSqlField
    :description: QtSql/QSqlField-c.rst

    .. sip:enum:: PyQt6.QtSql.QSqlField.RequiredStatus
        :description: QtSql/QSqlField-RequiredStatus-e.rst

        .. sip:enum-member:: PyQt6.QtSql.QSqlField.RequiredStatus.Optional
            :description: QtSql/QSqlField-RequiredStatus-Optional-v.rst

        .. sip:enum-member:: PyQt6.QtSql.QSqlField.RequiredStatus.Required
            :description: QtSql/QSqlField-RequiredStatus-Required-v.rst

        .. sip:enum-member:: PyQt6.QtSql.QSqlField.RequiredStatus.Unknown
            :description: QtSql/QSqlField-RequiredStatus-Unknown-v.rst

    .. sip:method:: PyQt6.QtSql.QSqlField.__init__
        :args:
            :sip:ref:`~PyQt6.QtSql.QSqlField`
        :description: QtSql/QSqlField-__init__-f.rst

    .. sip:method:: PyQt6.QtSql.QSqlField.__init__
        :args:
            fieldName: Optional[str] = ''
            type: :sip:ref:`~PyQt6.QtCore.QMetaType` = QMetaType()
            tableName: Optional[str] = ''
        :description: QtSql/QSqlField-__init__-f-2.rst

    .. sip:method:: PyQt6.QtSql.QSqlField.clear
        :description: QtSql/QSqlField-clear-f.rst

    .. sip:method:: PyQt6.QtSql.QSqlField.defaultValue
        :returns:
            Any
        :description: QtSql/QSqlField-defaultValue-f.rst

    .. sip:method:: PyQt6.QtSql.QSqlField.__eq__
        :args:
            :sip:ref:`~PyQt6.QtSql.QSqlField`
        :returns:
            bool
        :description: QtSql/QSqlField-__eq__-f.rst

    .. sip:method:: PyQt6.QtSql.QSqlField.isAutoValue
        :returns:
            bool
        :description: QtSql/QSqlField-isAutoValue-f.rst

    .. sip:method:: PyQt6.QtSql.QSqlField.isGenerated
        :returns:
            bool
        :description: QtSql/QSqlField-isGenerated-f.rst

    .. sip:method:: PyQt6.QtSql.QSqlField.isNull
        :returns:
            bool
        :description: QtSql/QSqlField-isNull-f.rst

    .. sip:method:: PyQt6.QtSql.QSqlField.isReadOnly
        :returns:
            bool
        :description: QtSql/QSqlField-isReadOnly-f.rst

    .. sip:method:: PyQt6.QtSql.QSqlField.isValid
        :returns:
            bool
        :description: QtSql/QSqlField-isValid-f.rst

    .. sip:method:: PyQt6.QtSql.QSqlField.length
        :returns:
            int
        :description: QtSql/QSqlField-length-f.rst

    .. sip:method:: PyQt6.QtSql.QSqlField.metaType
        :returns:
            :sip:ref:`~PyQt6.QtCore.QMetaType`
        :description: QtSql/QSqlField-metaType-f.rst

    .. sip:method:: PyQt6.QtSql.QSqlField.name
        :returns:
            str
        :description: QtSql/QSqlField-name-f.rst

    .. sip:method:: PyQt6.QtSql.QSqlField.__ne__
        :args:
            :sip:ref:`~PyQt6.QtSql.QSqlField`
        :returns:
            bool
        :description: QtSql/QSqlField-__ne__-f.rst

    .. sip:method:: PyQt6.QtSql.QSqlField.precision
        :returns:
            int
        :description: QtSql/QSqlField-precision-f.rst

    .. sip:method:: PyQt6.QtSql.QSqlField.requiredStatus
        :returns:
            :sip:ref:`~PyQt6.QtSql.QSqlField.RequiredStatus`
        :description: QtSql/QSqlField-requiredStatus-f.rst

    .. sip:method:: PyQt6.QtSql.QSqlField.setAutoValue
        :args:
            bool
        :description: QtSql/QSqlField-setAutoValue-f.rst

    .. sip:method:: PyQt6.QtSql.QSqlField.setDefaultValue
        :args:
            Any
        :description: QtSql/QSqlField-setDefaultValue-f.rst

    .. sip:method:: PyQt6.QtSql.QSqlField.setGenerated
        :args:
            bool
        :description: QtSql/QSqlField-setGenerated-f.rst

    .. sip:method:: PyQt6.QtSql.QSqlField.setLength
        :args:
            int
        :description: QtSql/QSqlField-setLength-f.rst

    .. sip:method:: PyQt6.QtSql.QSqlField.setMetaType
        :args:
            :sip:ref:`~PyQt6.QtCore.QMetaType`
        :description: QtSql/QSqlField-setMetaType-f.rst

    .. sip:method:: PyQt6.QtSql.QSqlField.setName
        :args:
            Optional[str]
        :description: QtSql/QSqlField-setName-f-1.rst

    .. sip:method:: PyQt6.QtSql.QSqlField.setPrecision
        :args:
            int
        :description: QtSql/QSqlField-setPrecision-f.rst

    .. sip:method:: PyQt6.QtSql.QSqlField.setReadOnly
        :args:
            bool
        :description: QtSql/QSqlField-setReadOnly-f.rst

    .. sip:method:: PyQt6.QtSql.QSqlField.setRequired
        :args:
            bool
        :description: QtSql/QSqlField-setRequired-f.rst

    .. sip:method:: PyQt6.QtSql.QSqlField.setRequiredStatus
        :args:
            :sip:ref:`~PyQt6.QtSql.QSqlField.RequiredStatus`
        :description: QtSql/QSqlField-setRequiredStatus-f.rst

    .. sip:method:: PyQt6.QtSql.QSqlField.setSqlType
        :args:
            int
        :description: QtSql/QSqlField-setSqlType-f.rst

    .. sip:method:: PyQt6.QtSql.QSqlField.setTableName
        :args:
            Optional[str]
        :description: QtSql/QSqlField-setTableName-f-1.rst

    .. sip:method:: PyQt6.QtSql.QSqlField.setValue
        :args:
            Any
        :description: QtSql/QSqlField-setValue-f.rst

    .. sip:method:: PyQt6.QtSql.QSqlField.swap
        :args:
            :sip:ref:`~PyQt6.QtSql.QSqlField`
        :description: QtSql/QSqlField-swap-f.rst

    .. sip:method:: PyQt6.QtSql.QSqlField.tableName
        :returns:
            str
        :description: QtSql/QSqlField-tableName-f.rst

    .. sip:method:: PyQt6.QtSql.QSqlField.typeID
        :returns:
            int
        :description: QtSql/QSqlField-typeID-f.rst

    .. sip:method:: PyQt6.QtSql.QSqlField.value
        :returns:
            Any
        :description: QtSql/QSqlField-value-f.rst
