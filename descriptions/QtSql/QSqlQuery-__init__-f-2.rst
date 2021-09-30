.. sip:method-description::
    :status: todo
    :pysig: 655d20e61252cd429bdaa7e9d3f8a1a0
    :realsig: (const QSqlQuery&)
    :digest: cc27571b41a0ae62e509cf11c7cbdc74

Constructs a copy of *other*.

:sip:ref:`~PyQt6.QtSql.QSqlQuery` cannot be meaningfully copied. Prepared statements, bound values and so on will not work correctly, depending on your database driver (for instance, changing the copy will affect the original). Treat :sip:ref:`~PyQt6.QtSql.QSqlQuery` as a move-only type instead.
