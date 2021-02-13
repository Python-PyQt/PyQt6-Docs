.. sip:method-description::
    :status: todo
    :pysig: 93c65966a7252879a2fdbc87264c9da8
    :realsig: (int*,int*,int*,int*) const
    :digest: 4458e39d29cbc2ef544fe8c06650d9e4

If the selection spans over table cells, *firstRow* is populated with the number of the first row in the selection, *firstColumn* with the number of the first column in the selection, and *numRows* and *numColumns* with the number of rows and columns in the selection. If the selection does not span any table cells the results are harmless but undefined.
