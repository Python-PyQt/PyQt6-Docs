.. sip:method-description::
    :status: todo
    :pysig: c506ff134babdd6e68ab3e6350e95305
    :realsig: ()
    :digest: 890a29e61fa8b31f32d84ea9f8442daf

Submits all changes from the mapped widgets to the model.

For every mapped section, the item delegate reads the current value from the widget and sets it in the model. Finally, the model's :sip:ref:`~PyQt6.QtCore.QAbstractItemModel.submit` method is invoked.

Returns ``true`` if all the values were submitted, otherwise false.

Note: For database models, :sip:ref:`~PyQt6.QtSql.QSqlQueryModel.lastError` can be used to retrieve the last error.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QDataWidgetMapper.revert`, :sip:ref:`~PyQt6.QtWidgets.QDataWidgetMapper.setSubmitPolicy`.
