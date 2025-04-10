.. sip:method-description::
    :status: todo
    :pysig: 3b9cb1fc34f8bc50978409d26ce0ef49
    :realsig: (Qt::DockWidgetArea)
    :digest: 325e449fd0e85188fa3e5a270a339387

Assigns this dock widget to *area*. If docked at another dock location, it will move to *area*. If floating or part of floating tabs, the next call of :sip:ref:`~PyQt6.QtWidgets.QDockWidget.setFloating`\ (false) will dock it at *area*.

**Note:** setDockLocation(Qt::NoDockLocation) is equivalent to :sip:ref:`~PyQt6.QtWidgets.QDockWidget.setFloating`\ (true).

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QDockWidget.dockLocation`, :sip:ref:`~PyQt6.QtWidgets.QDockWidget.dockLocationChanged`.
