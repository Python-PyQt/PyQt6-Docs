.. sip:method-description::
    :status: todo
    :pysig: f8cdb69e1ab6a60fe1568cc1aff418e9
    :realsig: (const QString&, const QHelpFilterData&)
    :digest: cf160b7e42d98be1f1a6ef20aceb32aa

Changes the existing filter details of the filter identified by *filterName* to *filterData*. If the filter does not exist, a new filter is created.

Returns ``true`` if setting the filter succeeded, otherwise returns ``false``.

.. seealso:: :sip:ref:`~PyQt6.QtHelp.QHelpFilterEngine.filterData`.
