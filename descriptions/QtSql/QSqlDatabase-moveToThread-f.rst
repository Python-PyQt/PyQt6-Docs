.. sip:method-description::
    :status: todo
    :pysig: da7ecfdafe9b6c0cf385a804cb486710
    :realsig: (QThread*)
    :digest: 4fba3cee3cdcb2b4c0d080bc5e912b96

Changes the thread affinity for :sip:ref:`~PyQt6.QtSql.QSqlDatabase` and its associated driver. This function returns ``true`` when the function succeeds. Event processing will continue in the *targetThread*.

During this operation you have to make sure that there is no :sip:ref:`~PyQt6.QtSql.QSqlQuery` bound to this instance otherwise the :sip:ref:`~PyQt6.QtSql.QSqlDatabase` will not be moved to the given thread and the function returns ``false``.

Since the associated driver is derived from :sip:ref:`~PyQt6.QtCore.QObject`, all constraints for moving a :sip:ref:`~PyQt6.QtCore.QObject` to another thread also apply to this function.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QObject.moveToThread`.
