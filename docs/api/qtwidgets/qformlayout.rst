:orphan:

.. sip:class:: PyQt6.QtWidgets.QFormLayout
    :inherits: :sip:ref:`~PyQt6.QtWidgets.QLayout`
    :description: QtWidgets/QFormLayout-c.rst

    .. sip:enum:: PyQt6.QtWidgets.QFormLayout.FieldGrowthPolicy
        :description: QtWidgets/QFormLayout-FieldGrowthPolicy-e.rst

        .. sip:enum-member:: PyQt6.QtWidgets.QFormLayout.FieldGrowthPolicy.AllNonFixedFieldsGrow
            :description: QtWidgets/QFormLayout-FieldGrowthPolicy-AllNonFixedFieldsGrow-v.rst

        .. sip:enum-member:: PyQt6.QtWidgets.QFormLayout.FieldGrowthPolicy.ExpandingFieldsGrow
            :description: QtWidgets/QFormLayout-FieldGrowthPolicy-ExpandingFieldsGrow-v.rst

        .. sip:enum-member:: PyQt6.QtWidgets.QFormLayout.FieldGrowthPolicy.FieldsStayAtSizeHint
            :description: QtWidgets/QFormLayout-FieldGrowthPolicy-FieldsStayAtSizeHint-v.rst

    .. sip:enum:: PyQt6.QtWidgets.QFormLayout.ItemRole
        :description: QtWidgets/QFormLayout-ItemRole-e.rst

        .. sip:enum-member:: PyQt6.QtWidgets.QFormLayout.ItemRole.FieldRole
            :description: QtWidgets/QFormLayout-ItemRole-FieldRole-v.rst

        .. sip:enum-member:: PyQt6.QtWidgets.QFormLayout.ItemRole.LabelRole
            :description: QtWidgets/QFormLayout-ItemRole-LabelRole-v.rst

        .. sip:enum-member:: PyQt6.QtWidgets.QFormLayout.ItemRole.SpanningRole
            :description: QtWidgets/QFormLayout-ItemRole-SpanningRole-v.rst

    .. sip:enum:: PyQt6.QtWidgets.QFormLayout.RowWrapPolicy
        :description: QtWidgets/QFormLayout-RowWrapPolicy-e.rst

        .. sip:enum-member:: PyQt6.QtWidgets.QFormLayout.RowWrapPolicy.DontWrapRows
            :description: QtWidgets/QFormLayout-RowWrapPolicy-DontWrapRows-v.rst

        .. sip:enum-member:: PyQt6.QtWidgets.QFormLayout.RowWrapPolicy.WrapAllRows
            :description: QtWidgets/QFormLayout-RowWrapPolicy-WrapAllRows-v.rst

        .. sip:enum-member:: PyQt6.QtWidgets.QFormLayout.RowWrapPolicy.WrapLongRows
            :description: QtWidgets/QFormLayout-RowWrapPolicy-WrapLongRows-v.rst

    .. sip:method:: PyQt6.QtWidgets.QFormLayout.__init__
        :args:
            parent: :sip:ref:`~PyQt6.QtWidgets.QWidget` = None
        :description: QtWidgets/QFormLayout-__init__-f.rst

    .. sip:method:: PyQt6.QtWidgets.QFormLayout.addItem
        :args:
            :sip:ref:`~PyQt6.QtWidgets.QLayoutItem`
        :description: QtWidgets/QFormLayout-addItem-f.rst

    .. sip:method:: PyQt6.QtWidgets.QFormLayout.addRow
        :args:
            :sip:ref:`~PyQt6.QtWidgets.QWidget`
        :description: QtWidgets/QFormLayout-addRow-f.rst

    .. sip:method:: PyQt6.QtWidgets.QFormLayout.addRow
        :args:
            :sip:ref:`~PyQt6.QtWidgets.QLayout`
        :description: QtWidgets/QFormLayout-addRow-f-1.rst

    .. sip:method:: PyQt6.QtWidgets.QFormLayout.addRow
        :args:
            :sip:ref:`~PyQt6.QtWidgets.QWidget`
            :sip:ref:`~PyQt6.QtWidgets.QWidget`
        :description: QtWidgets/QFormLayout-addRow-f-2.rst

    .. sip:method:: PyQt6.QtWidgets.QFormLayout.addRow
        :args:
            :sip:ref:`~PyQt6.QtWidgets.QWidget`
            :sip:ref:`~PyQt6.QtWidgets.QLayout`
        :description: QtWidgets/QFormLayout-addRow-f-3.rst

    .. sip:method:: PyQt6.QtWidgets.QFormLayout.addRow
        :args:
            Optional[str]
            :sip:ref:`~PyQt6.QtWidgets.QWidget`
        :description: QtWidgets/QFormLayout-addRow-f-6.rst

    .. sip:method:: PyQt6.QtWidgets.QFormLayout.addRow
        :args:
            Optional[str]
            :sip:ref:`~PyQt6.QtWidgets.QLayout`
        :description: QtWidgets/QFormLayout-addRow-f-7.rst

    .. sip:method:: PyQt6.QtWidgets.QFormLayout.count
        :returns:
            int
        :description: QtWidgets/QFormLayout-count-f.rst

    .. sip:method:: PyQt6.QtWidgets.QFormLayout.expandingDirections
        :returns:
            :sip:ref:`~PyQt6.QtCore.Qt.Orientation`
        :description: QtWidgets/QFormLayout-expandingDirections-f-1.rst

    .. sip:method:: PyQt6.QtWidgets.QFormLayout.fieldGrowthPolicy
        :returns:
            :sip:ref:`~PyQt6.QtWidgets.QFormLayout.FieldGrowthPolicy`
        :description: QtWidgets/QFormLayout-fieldGrowthPolicy-f.rst

    .. sip:method:: PyQt6.QtWidgets.QFormLayout.formAlignment
        :returns:
            :sip:ref:`~PyQt6.QtCore.Qt.AlignmentFlag`
        :description: QtWidgets/QFormLayout-formAlignment-f-1.rst

    .. sip:method:: PyQt6.QtWidgets.QFormLayout.getItemPosition
        :args:
            int
        :returns:
            int
            :sip:ref:`~PyQt6.QtWidgets.QFormLayout.ItemRole`
        :description: QtWidgets/QFormLayout-getItemPosition-f.rst

    .. sip:method:: PyQt6.QtWidgets.QFormLayout.getLayoutPosition
        :args:
            :sip:ref:`~PyQt6.QtWidgets.QLayout`
        :returns:
            int
            :sip:ref:`~PyQt6.QtWidgets.QFormLayout.ItemRole`
        :description: QtWidgets/QFormLayout-getLayoutPosition-f.rst

    .. sip:method:: PyQt6.QtWidgets.QFormLayout.getWidgetPosition
        :args:
            :sip:ref:`~PyQt6.QtWidgets.QWidget`
        :returns:
            int
            :sip:ref:`~PyQt6.QtWidgets.QFormLayout.ItemRole`
        :description: QtWidgets/QFormLayout-getWidgetPosition-f.rst

    .. sip:method:: PyQt6.QtWidgets.QFormLayout.hasHeightForWidth
        :returns:
            bool
        :description: QtWidgets/QFormLayout-hasHeightForWidth-f.rst

    .. sip:method:: PyQt6.QtWidgets.QFormLayout.heightForWidth
        :args:
            int
        :returns:
            int
        :description: QtWidgets/QFormLayout-heightForWidth-f.rst

    .. sip:method:: PyQt6.QtWidgets.QFormLayout.horizontalSpacing
        :returns:
            int
        :description: QtWidgets/QFormLayout-horizontalSpacing-f.rst

    .. sip:method:: PyQt6.QtWidgets.QFormLayout.insertRow
        :args:
            int
            :sip:ref:`~PyQt6.QtWidgets.QWidget`
        :description: QtWidgets/QFormLayout-insertRow-f.rst

    .. sip:method:: PyQt6.QtWidgets.QFormLayout.insertRow
        :args:
            int
            :sip:ref:`~PyQt6.QtWidgets.QLayout`
        :description: QtWidgets/QFormLayout-insertRow-f-1.rst

    .. sip:method:: PyQt6.QtWidgets.QFormLayout.insertRow
        :args:
            int
            :sip:ref:`~PyQt6.QtWidgets.QWidget`
            :sip:ref:`~PyQt6.QtWidgets.QWidget`
        :description: QtWidgets/QFormLayout-insertRow-f-2.rst

    .. sip:method:: PyQt6.QtWidgets.QFormLayout.insertRow
        :args:
            int
            :sip:ref:`~PyQt6.QtWidgets.QWidget`
            :sip:ref:`~PyQt6.QtWidgets.QLayout`
        :description: QtWidgets/QFormLayout-insertRow-f-3.rst

    .. sip:method:: PyQt6.QtWidgets.QFormLayout.insertRow
        :args:
            int
            Optional[str]
            :sip:ref:`~PyQt6.QtWidgets.QWidget`
        :description: QtWidgets/QFormLayout-insertRow-f-6.rst

    .. sip:method:: PyQt6.QtWidgets.QFormLayout.insertRow
        :args:
            int
            Optional[str]
            :sip:ref:`~PyQt6.QtWidgets.QLayout`
        :description: QtWidgets/QFormLayout-insertRow-f-7.rst

    .. sip:method:: PyQt6.QtWidgets.QFormLayout.invalidate
        :description: QtWidgets/QFormLayout-invalidate-f.rst

    .. sip:method:: PyQt6.QtWidgets.QFormLayout.isRowVisible
        :args:
            :sip:ref:`~PyQt6.QtWidgets.QLayout`
        :returns:
            bool
        :description: QtWidgets/QFormLayout-isRowVisible-f.rst

    .. sip:method:: PyQt6.QtWidgets.QFormLayout.isRowVisible
        :args:
            :sip:ref:`~PyQt6.QtWidgets.QWidget`
        :returns:
            bool
        :description: QtWidgets/QFormLayout-isRowVisible-f-1.rst

    .. sip:method:: PyQt6.QtWidgets.QFormLayout.isRowVisible
        :args:
            int
        :returns:
            bool
        :description: QtWidgets/QFormLayout-isRowVisible-f-2.rst

    .. sip:method:: PyQt6.QtWidgets.QFormLayout.itemAt
        :args:
            int
        :returns:
            :sip:ref:`~PyQt6.QtWidgets.QLayoutItem`
        :description: QtWidgets/QFormLayout-itemAt-f.rst

    .. sip:method:: PyQt6.QtWidgets.QFormLayout.itemAt
        :args:
            int
            :sip:ref:`~PyQt6.QtWidgets.QFormLayout.ItemRole`
        :returns:
            :sip:ref:`~PyQt6.QtWidgets.QLayoutItem`
        :description: QtWidgets/QFormLayout-itemAt-f-1.rst

    .. sip:method:: PyQt6.QtWidgets.QFormLayout.labelAlignment
        :returns:
            :sip:ref:`~PyQt6.QtCore.Qt.AlignmentFlag`
        :description: QtWidgets/QFormLayout-labelAlignment-f-1.rst

    .. sip:method:: PyQt6.QtWidgets.QFormLayout.labelForField
        :args:
            :sip:ref:`~PyQt6.QtWidgets.QWidget`
        :returns:
            :sip:ref:`~PyQt6.QtWidgets.QWidget`
        :description: QtWidgets/QFormLayout-labelForField-f.rst

    .. sip:method:: PyQt6.QtWidgets.QFormLayout.labelForField
        :args:
            :sip:ref:`~PyQt6.QtWidgets.QLayout`
        :returns:
            :sip:ref:`~PyQt6.QtWidgets.QWidget`
        :description: QtWidgets/QFormLayout-labelForField-f-1.rst

    .. sip:method:: PyQt6.QtWidgets.QFormLayout.minimumSize
        :returns:
            :sip:ref:`~PyQt6.QtCore.QSize`
        :description: QtWidgets/QFormLayout-minimumSize-f.rst

    .. sip:method:: PyQt6.QtWidgets.QFormLayout.removeRow
        :args:
            int
        :description: QtWidgets/QFormLayout-removeRow-f.rst

    .. sip:method:: PyQt6.QtWidgets.QFormLayout.removeRow
        :args:
            :sip:ref:`~PyQt6.QtWidgets.QWidget`
        :description: QtWidgets/QFormLayout-removeRow-f-1.rst

    .. sip:method:: PyQt6.QtWidgets.QFormLayout.removeRow
        :args:
            :sip:ref:`~PyQt6.QtWidgets.QLayout`
        :description: QtWidgets/QFormLayout-removeRow-f-2.rst

    .. sip:method:: PyQt6.QtWidgets.QFormLayout.rowCount
        :returns:
            int
        :description: QtWidgets/QFormLayout-rowCount-f.rst

    .. sip:method:: PyQt6.QtWidgets.QFormLayout.rowWrapPolicy
        :returns:
            :sip:ref:`~PyQt6.QtWidgets.QFormLayout.RowWrapPolicy`
        :description: QtWidgets/QFormLayout-rowWrapPolicy-f.rst

    .. sip:method:: PyQt6.QtWidgets.QFormLayout.setFieldGrowthPolicy
        :args:
            :sip:ref:`~PyQt6.QtWidgets.QFormLayout.FieldGrowthPolicy`
        :description: QtWidgets/QFormLayout-setFieldGrowthPolicy-f.rst

    .. sip:method:: PyQt6.QtWidgets.QFormLayout.setFormAlignment
        :args:
            :sip:ref:`~PyQt6.QtCore.Qt.AlignmentFlag`
        :description: QtWidgets/QFormLayout-setFormAlignment-f-1.rst

    .. sip:method:: PyQt6.QtWidgets.QFormLayout.setGeometry
        :args:
            :sip:ref:`~PyQt6.QtCore.QRect`
        :description: QtWidgets/QFormLayout-setGeometry-f.rst

    .. sip:method:: PyQt6.QtWidgets.QFormLayout.setHorizontalSpacing
        :args:
            int
        :description: QtWidgets/QFormLayout-setHorizontalSpacing-f.rst

    .. sip:method:: PyQt6.QtWidgets.QFormLayout.setItem
        :args:
            int
            :sip:ref:`~PyQt6.QtWidgets.QFormLayout.ItemRole`
            :sip:ref:`~PyQt6.QtWidgets.QLayoutItem`
        :description: QtWidgets/QFormLayout-setItem-f.rst

    .. sip:method:: PyQt6.QtWidgets.QFormLayout.setLabelAlignment
        :args:
            :sip:ref:`~PyQt6.QtCore.Qt.AlignmentFlag`
        :description: QtWidgets/QFormLayout-setLabelAlignment-f-1.rst

    .. sip:method:: PyQt6.QtWidgets.QFormLayout.setLayout
        :args:
            int
            :sip:ref:`~PyQt6.QtWidgets.QFormLayout.ItemRole`
            :sip:ref:`~PyQt6.QtWidgets.QLayout`
        :description: QtWidgets/QFormLayout-setLayout-f.rst

    .. sip:method:: PyQt6.QtWidgets.QFormLayout.setRowVisible
        :args:
            :sip:ref:`~PyQt6.QtWidgets.QLayout`
            bool
        :description: QtWidgets/QFormLayout-setRowVisible-f.rst

    .. sip:method:: PyQt6.QtWidgets.QFormLayout.setRowVisible
        :args:
            :sip:ref:`~PyQt6.QtWidgets.QWidget`
            bool
        :description: QtWidgets/QFormLayout-setRowVisible-f-1.rst

    .. sip:method:: PyQt6.QtWidgets.QFormLayout.setRowVisible
        :args:
            int
            bool
        :description: QtWidgets/QFormLayout-setRowVisible-f-2.rst

    .. sip:method:: PyQt6.QtWidgets.QFormLayout.setRowWrapPolicy
        :args:
            :sip:ref:`~PyQt6.QtWidgets.QFormLayout.RowWrapPolicy`
        :description: QtWidgets/QFormLayout-setRowWrapPolicy-f.rst

    .. sip:method:: PyQt6.QtWidgets.QFormLayout.setSpacing
        :args:
            int
        :description: QtWidgets/QFormLayout-setSpacing-f.rst

    .. sip:method:: PyQt6.QtWidgets.QFormLayout.setVerticalSpacing
        :args:
            int
        :description: QtWidgets/QFormLayout-setVerticalSpacing-f.rst

    .. sip:method:: PyQt6.QtWidgets.QFormLayout.setWidget
        :args:
            int
            :sip:ref:`~PyQt6.QtWidgets.QFormLayout.ItemRole`
            :sip:ref:`~PyQt6.QtWidgets.QWidget`
        :description: QtWidgets/QFormLayout-setWidget-f.rst

    .. sip:method:: PyQt6.QtWidgets.QFormLayout.sizeHint
        :returns:
            :sip:ref:`~PyQt6.QtCore.QSize`
        :description: QtWidgets/QFormLayout-sizeHint-f.rst

    .. sip:method:: PyQt6.QtWidgets.QFormLayout.spacing
        :returns:
            int
        :description: QtWidgets/QFormLayout-spacing-f.rst

    .. sip:method:: PyQt6.QtWidgets.QFormLayout.takeAt
        :args:
            int
        :returns:
            :sip:ref:`~PyQt6.QtWidgets.QLayoutItem`
        :description: QtWidgets/QFormLayout-takeAt-f.rst

    .. sip:method:: PyQt6.QtWidgets.QFormLayout.takeRow
        :args:
            int
        :returns:
            :sip:ref:`~PyQt6.QtWidgets.QFormLayout.TakeRowResult`
        :description: QtWidgets/QFormLayout-takeRow-f.rst

    .. sip:method:: PyQt6.QtWidgets.QFormLayout.takeRow
        :args:
            :sip:ref:`~PyQt6.QtWidgets.QWidget`
        :returns:
            :sip:ref:`~PyQt6.QtWidgets.QFormLayout.TakeRowResult`
        :description: QtWidgets/QFormLayout-takeRow-f-1.rst

    .. sip:method:: PyQt6.QtWidgets.QFormLayout.takeRow
        :args:
            :sip:ref:`~PyQt6.QtWidgets.QLayout`
        :returns:
            :sip:ref:`~PyQt6.QtWidgets.QFormLayout.TakeRowResult`
        :description: QtWidgets/QFormLayout-takeRow-f-2.rst

    .. sip:method:: PyQt6.QtWidgets.QFormLayout.verticalSpacing
        :returns:
            int
        :description: QtWidgets/QFormLayout-verticalSpacing-f.rst
