.. sip:method-description::
    :status: todo
    :pysig: 6a1bb6ed41f44b60e7bd83b0e9945aa7
    :realsig: (double,double)
    :digest: 99175f381c1e572e11b7340bb58afef9

Translates this geo rectangle by *degreesLatitude* northwards and *degreesLongitude* eastwards.

Negative values of *degreesLatitude* and *degreesLongitude* correspond to southward and westward translation respectively.

If the translation would have caused the geo rectangle to cross a pole the geo rectangle will be translated until the top or bottom edge of the geo rectangle touches the pole but not further.
