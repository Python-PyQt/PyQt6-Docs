.. sip:method-description::
    :status: todo
    :pysig: d41d8cd98f00b204e9800998ecf8427e
    :realsig: ()
    :digest: d82c0ae5b92f2f7e6d5535f409b39739

Instruct the database driver that no more data will be fetched from this query until it is re-executed. There is normally no need to call this function, but it may be helpful in order to free resources such as locks or cursors if you intend to re-use the query at a later time.

Sets the query to inactive. Bound values retain their values.

.. seealso:: :sip:ref:`~PyQt6.QtSql.QSqlQuery.prepare`, :sip:ref:`~PyQt6.QtSql.QSqlQuery.exec`, :sip:ref:`~PyQt6.QtSql.QSqlQuery.isActive`.
