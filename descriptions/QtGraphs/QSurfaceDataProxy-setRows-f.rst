.. sip:method-description::
    :status: todo
    :pysig: e5675ed1905c3cb1306792f000945f52
    :realsig: (qsizetype, QSurfaceDataArray)
    :digest: c36f9c24270fb20d758b0bbc87f67d0d

Changes existing rows by replacing the rows starting at the position *rowIndex* with the new rows specifies by *rows*. The rows in the *rows* array can be the same as the existing rows already stored at the *rowIndex*. The new rows must have the same number of columns as the rows they are replacing.
