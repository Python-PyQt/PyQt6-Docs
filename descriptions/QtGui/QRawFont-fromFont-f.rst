.. sip:method-description::
    :status: todo
    :pysig: 05fd0a443f5d9d2f40334be4b52ab728
    :realsig: (const QFont&,QFontDatabase::WritingSystem)
    :digest: 98d76bfd0fb5cffc6d592721715e4876

Fetches the physical representation based on a *font* query. The physical font returned is the font that will be preferred by Qt in order to display text in the selected *writingSystem*.

**Warning:** This function is potentially expensive and should not be called in performance sensitive code.
