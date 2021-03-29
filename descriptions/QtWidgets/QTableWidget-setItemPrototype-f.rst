.. sip:method-description::
    :status: todo
    :pysig: c8a022b1c4e6a23307fd20d5779960eb
    :realsig: (const QTableWidgetItem*)
    :digest: e4790d7018b59a001e40607df10e14ba

Sets the item prototype for the table to the specified *item*.

The table widget will use the item prototype clone function when it needs to create a new table item. For example when the user is editing in an empty cell. This is useful when you have a :sip:ref:`~PyQt6.QtWidgets.QTableWidgetItem` subclass and want to make sure that :sip:ref:`~PyQt6.QtWidgets.QTableWidget` creates instances of your subclass.

The table takes ownership of the prototype.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QTableWidget.itemPrototype`.
