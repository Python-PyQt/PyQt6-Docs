.. sip:method-description::
    :status: todo
    :pysig: 691785c077f1026527d18c30bdb426b1
    :realsig: (const QString&,const QHelpFilterData&)
    :digest: cf160b7e42d98be1f1a6ef20aceb32aa

Changes the existing filter details of the filter identified by *filterName* to *filterData*. If the filter does not exist, a new filter is created.

Returns ``true`` if setting the filter succeeded, otherwise returns ``false``.

.. seealso:: :sip:ref:`~PyQt6.QtHelp.QHelpFilterEngine.filterData`.
