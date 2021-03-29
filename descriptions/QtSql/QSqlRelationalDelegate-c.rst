.. sip:class-description::
    :status: todo
    :brief: Delegate that is used to display and edit data from a QSqlRelationalTableModel
    :digest: 320813a79ba89176b90b92c5be8e6e1f

The :sip:ref:`~PyQt6.QtSql.QSqlRelationalDelegate` class provides a delegate that is used to display and edit data from a :sip:ref:`~PyQt6.QtSql.QSqlRelationalTableModel`.

Unlike the default delegate, :sip:ref:`~PyQt6.QtSql.QSqlRelationalDelegate` provides a combobox for fields that are foreign keys into other tables. To use the class, simply call :sip:ref:`~PyQt6.QtWidgets.QAbstractItemView.setItemDelegate` on the view with an instance of :sip:ref:`~PyQt6.QtSql.QSqlRelationalDelegate`:

.. literalinclude:: ../../../snippets/qtbase-examples-sql-relationaltablemodel-relationaltablemodel.py
    :lines: 86-88

The `Relational Table Model <https://doc.qt.io/qt-6/qtsql-relationaltablemodel-example.html>`_ example (shown below) illustrates how to use :sip:ref:`~PyQt6.QtSql.QSqlRelationalDelegate` in conjunction with :sip:ref:`~PyQt6.QtSql.QSqlRelationalTableModel` to provide tables with foreign key support.

.. image:: ../../../images/relationaltable.png

.. seealso:: :sip:ref:`~PyQt6.QtSql.QSqlRelationalTableModel`, `Model/View Programming <https://doc.qt.io/qt-6/model-view-programming.html>`_.
