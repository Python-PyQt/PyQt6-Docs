.. sip:method-description::
    :status: todo
    :pysig: ebde01817f36406568ba0523f8497697
    :realsig: (const QGeoCoordinate&,double,double)
    :digest: e1bf9af7fa6f676973e6241c41fba568

Constructs a new geo rectangle centered at *center* with a width in degrees of *degreesWidth* and a height in degrees of *degreesHeight*.

If *degreesHeight* would take the geo rectangle beyond one of the poles, the height of the geo rectangle will be truncated such that the geo rectangle only extends up to the pole. The center of the geo rectangle will be unchanged, and the height will be adjusted such that the center point is at the center of the truncated geo rectangle.
