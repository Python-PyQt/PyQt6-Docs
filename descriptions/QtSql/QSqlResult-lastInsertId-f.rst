.. sip:method-description::
    :status: todo
    :pysig: ed36a1ef76a59ee3f15180e0441188ad
    :realsig: () const
    :digest: 1353d0301d520b991b46de542183a67d

Returns the object ID of the most recent inserted row if the database supports it. An invalid `QVariant <https://doc.qt.io/qt-6/qtcore-changes-qt6.html#qvariant>`_ will be returned if the query did not insert any value or if the database does not report the id back. If more than one row was touched by the insert, the behavior is undefined.

Note that for Oracle databases the row's ROWID will be returned, while for MySQL databases the row's auto-increment field will be returned.

.. seealso:: :sip:ref:`~PyQt6.QtSql.QSqlDriver.hasFeature`.
