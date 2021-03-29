.. sip:enum-description::
    :status: todo
    :digest: fa3db7ae4de9b01276af694fc07c85f7

The timer type indicates how accurate a timer can be.

On UNIX (including Linux, macOS, and iOS), Qt will keep millisecond accuracy for . For , the interval will be adjusted up to 5% to align the timer with other timers that are expected to fire at or around the same time. The objective is to make most timers wake up at the same time, thereby reducing CPU wakeups and power consumption.

On Windows, Qt will use Windows's Multimedia timer facility (if available) for  and normal Windows timers for  and .

On all platforms, the interval for  is rounded to the nearest full second (e.g. an interval of 23500ms will be rounded to 24000ms, and 20300ms to 20000ms).
