.. sip:method-description::
    :status: todo
    :pysig: c506ff134babdd6e68ab3e6350e95305
    :realsig: () const
    :digest: b60b72b4d2c698e602cf6d2baab30e00

Returns ``true`` if the query is *active*. An active `QSqlQuery <https://doc.qt.io/qt-6/qtsql-changes-qt6.html#qsqlquery>`_ is one that has been :sip:ref:`~PyQt6.QtSql.QSqlQuery.exec` successfully but not yet finished with. When you are finished with an active query, you can make the query inactive by calling :sip:ref:`~PyQt6.QtSql.QSqlQuery.finish` or :sip:ref:`~PyQt6.QtSql.QSqlQuery.clear`, or you can delete the `QSqlQuery <https://doc.qt.io/qt-6/qtsql-changes-qt6.html#qsqlquery>`_ instance.

**Note:** Of particular interest is an active query that is a ``SELECT`` statement. For some databases that support transactions, an active query that is a ``SELECT`` statement can cause a :sip:ref:`~PyQt6.QtSql.QSqlDatabase.commit` or a :sip:ref:`~PyQt6.QtSql.QSqlDatabase.rollback` to fail, so before committing or rolling back, you should make your active ``SELECT`` statement query inactive using one of the ways listed above.

.. seealso:: :sip:ref:`~PyQt6.QtSql.QSqlQuery.isSelect`.
