.. sip:method-description::
    :status: todo
    :pysig: 3787259c2be1a3df14d101d8b5910091
    :realsig: (int,const QSurfaceDataArray&)
    :digest: c36f9c24270fb20d758b0bbc87f67d0d

Changes existing rows by replacing the rows starting at the position *rowIndex* with the new rows specifies by *rows*. The rows in the *rows* array can be the same as the existing rows already stored at the *rowIndex*. The new rows must have the same number of columns as the rows they are replacing.
