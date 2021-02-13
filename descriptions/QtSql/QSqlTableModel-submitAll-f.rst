.. sip:method-description::
    :status: todo
    :pysig: c506ff134babdd6e68ab3e6350e95305
    :realsig: ()
    :digest: b2ceacd6a6b7ce6ff56146a1c12cab56

Submits all pending changes and returns ``true`` on success. Returns ``false`` on error, detailed error information can be obtained with lastError().

In :sip:ref:`~PyQt6.QtSql.QSqlTableModel.EditStrategy.OnManualSubmit`, on success the model will be repopulated. Any views presenting it will lose their selections.

Note: In :sip:ref:`~PyQt6.QtSql.QSqlTableModel.EditStrategy.OnManualSubmit` mode, already submitted changes won't be cleared from the cache when  fails. This allows transactions to be rolled back and resubmitted without losing data.

.. seealso:: :sip:ref:`~PyQt6.QtSql.QSqlTableModel.revertAll`, lastError().
