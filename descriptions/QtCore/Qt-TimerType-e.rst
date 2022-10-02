.. sip:enum-description::
    :status: todo
    :digest: 8c29cdf3f5202450e57cdc13e8a43596

The timer type indicates how accurate a timer can be.

On UNIX (including Linux, macOS, and iOS), Qt will keep millisecond accuracy for Qt::PreciseTimer. For Qt::CoarseTimer, the interval will be adjusted up to 5% to align the timer with other timers that are expected to fire at or around the same time. The objective is to make most timers wake up at the same time, thereby reducing CPU wakeups and power consumption.

On Windows, Qt will use Windows's Multimedia timer facility (if available) for Qt::PreciseTimer and normal Windows timers for Qt::CoarseTimer and Qt::VeryCoarseTimer.

On all platforms, the interval for Qt::VeryCoarseTimer is rounded to the nearest full second (e.g. an interval of 23500ms will be rounded to 24000ms, and 20300ms to 20000ms).
