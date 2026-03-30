.. sip:method-description::
    :status: todo
    :pysig: 1903d51226141b457daf0aecc4d4e9b4
    :realsig: (const QString&, const QString&)
    :digest: 86be27dfc5fd5bf97b77c9ec7155e26c

Filters the indices and returns the model index of the best matching keyword. In a first step, only the keywords containing *filter* are kept in the model's index list. Analogously, if *wildcard* is not empty, only the keywords matched are left in the index list. In a second step, the best match is determined and its index model returned. When specifying a wildcard expression, the *filter* string is used to search for the best match.
