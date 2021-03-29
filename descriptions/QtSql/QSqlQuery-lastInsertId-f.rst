.. sip:method-description::
    :status: todo
    :pysig: ed36a1ef76a59ee3f15180e0441188ad
    :realsig: () const
    :digest: bd6bd6d1916898bf79ff675446f8c446

Returns the object ID of the most recent inserted row if the database supports it. An invalid `QVariant <https://doc.qt.io/qt-6/qtcore-changes-qt6.html#qvariant>`_ will be returned if the query did not insert any value or if the database does not report the id back. If more than one row was touched by the insert, the behavior is undefined.

For MySQL databases the row's auto-increment field will be returned.

**Note:** For this function to work in PSQL, the table table must contain OIDs, which may not have been created by default. Check the ``default_with_oids`` configuration variable to be sure.

.. seealso:: :sip:ref:`~PyQt6.QtSql.QSqlDriver.hasFeature`.
