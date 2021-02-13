.. sip:class-description::
    :status: todo
    :brief: Describes the size, orientation and margins of a page
    :digest: 325ac63765ff63dccadddc259149b78b

Describes the size, orientation and margins of a page.

The :sip:ref:`~PyQt6.QtGui.QPageLayout` class defines the layout of a page in a paged document, with the page size, orientation and margins able to be set and the full page and paintable page rectangles defined by those attributes able to be queried in a variety of units.

The page size is defined by the :sip:ref:`~PyQt6.QtGui.QPageSize` class which can be queried for page size attributes. Note that the :sip:ref:`~PyQt6.QtGui.QPageSize` itself is always defined in a Portrait orientation.

The minimum margins can be defined for the layout but normally default to 0. When used in conjunction with Qt's printing support the minimum margins will reflect the minimum printable area defined by the printer.

In the default :sip:ref:`~PyQt6.QtGui.QPageLayout.Mode.StandardMode` the current margins and minimum margins are always taken into account. The paintable rectangle is the full page rectangle less the current margins, and the current margins can only be set to values between the minimum margins and the maximum margins allowed by the full page size.

In :sip:ref:`~PyQt6.QtGui.QPageLayout.Mode.FullPageMode` the current margins and minimum margins are not taken into account. The paintable rectangle is the full page rectangle, and the current margins can be set to any values regardless of the minimum margins and page size.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QPageSize`.
