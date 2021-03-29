.. sip:class-description::
    :status: todo
    :brief: The base class for SQL driver factories
    :digest: 2060cff7f5433c8e845f3e956981c37b

The :sip:ref:`~PyQt6.QtSql.QSqlDriverCreatorBase` class is the base class for SQL driver factories.

Reimplement :sip:ref:`~PyQt6.QtSql.QSqlDriverCreatorBase.createObject` to return an instance of the specific :sip:ref:`~PyQt6.QtSql.QSqlDriver` subclass that you want to provide.

See :sip:ref:`~PyQt6.QtSql.QSqlDatabase.registerSqlDriver` for details.

.. seealso:: QSqlDriverCreator.
