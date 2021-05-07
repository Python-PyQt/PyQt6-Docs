.. sip:method-description::
    :status: todo
    :pysig: 11a034346fb6ad8291e99111a1e5ec05
    :realsig: (QScatterDataProxy*)
    :digest: 7a28bcceaadfb663c45c91b6065fe5a8

Sets the active data proxy for the series to *proxy*. The series assumes ownership of any proxy set to it and deletes any previously set proxy when a new one is added. The *proxy* argument cannot be null or set to another series.

.. seealso:: :sip:ref:`~PyQt6.QtDataVisualization.QScatter3DSeries.dataProxy`.
