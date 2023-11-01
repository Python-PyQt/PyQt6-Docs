.. sip:method-description::
    :status: todo
    :pysig: 12a89cd63d1c9636620cf3e9d59333e9
    :realsig: (const QString&, const QString&) const
    :digest: 928a7ebd7d1753b906e231209db1acf6

Returns a list of the document links found for the *keyword*, filtered by *filterName*. The returned list contents depend on the passed filter, and therefore only the keywords registered for this filter will be returned. If you want to get all results unfiltered, pass empty string as *filterName*.
