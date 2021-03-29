.. sip:class-description::
    :status: todo
    :brief: Describes the size and name of a defined page size
    :digest: ee336639108a255d2cafe6cedb0e9aeb

The :sip:ref:`~PyQt6.QtGui.QPageSize` class describes the size and name of a defined page size.

This class implements support for the set of standard page sizes as defined in the Adobe Postscript PPD Standard v4.3. It defines the standard set of page sizes in points, millimeters and inches and ensures these sizes are consistently used. Other size units can be used but will be calculated results and so may not always be consistent. The defined point sizes are always a integer, all other sizes can be fractions of a unit.

The defined size is always in width x height order with no implied page orientation. Note that it is possible for page sizes to be defined where the width is greater than the height, such as :sip:ref:`~PyQt6.QtGui.QPageSize.PageSizeId.Ledger`, so you cannot rely on comparing the width and height values to determine page orientation.

For example, A4 is defined by the standard as 210mm x 297mm, 8.27in x 11.69in, or 595pt x 842pt.

You can also define custom page sizes with custom names in any units you want and this unit size will be preserved and used as the base for all other unit size calculations.

When creating a :sip:ref:`~PyQt6.QtGui.QPageSize` using a custom :sip:ref:`~PyQt6.QtCore.QSize` you can choose if you want :sip:ref:`~PyQt6.QtGui.QPageSize` to try match the size to a standard page size. By default QPaperSize uses a :sip:ref:`~PyQt6.QtGui.QPageSize.SizeMatchPolicy.FuzzyMatch` mode where it will match a given page size to a standard page size if it falls within 3 postscript points of a defined standard size. You can override this to request only an exact match but this is not recommended as conversions between units can easily lose 3 points and result in incorrect page sizes.

A :sip:ref:`~PyQt6.QtGui.QPageSize` instance may also be obtained by querying the supported page sizes for a print device. In this case the localized name returned is that defined by the printer itself. Note that the print device may not support the current default locale language.

The class also provides convenience methods for converting page size IDs to and from various unit sizes.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QPagedPaintDevice`, :sip:ref:`~PyQt6.QtGui.QPdfWriter`.
