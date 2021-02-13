.. sip:signal-description::
    :status: todo
    :pysig: edb3c45e5d6e0ecd4da9b4b877c5546f
    :realsig: (int,QSqlRecord&)
    :digest: d76e69b4f5af6185eace9054572edba1

This signal is emitted by :sip:ref:`~PyQt6.QtSql.QSqlTableModel.insertRows`, when an insertion is initiated in the given *row* of the currently active database table. The *record* parameter can be written to (since it is a reference), for example to populate some fields with default values and set the generated flags of the fields. Do not try to edit the record via other means such as :sip:ref:`~PyQt6.QtSql.QSqlTableModel.setData` or :sip:ref:`~PyQt6.QtSql.QSqlTableModel.setRecord` while handling this signal.
