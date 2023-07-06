Args and Kwargs are great in certain circumstances.
Say you have a decorator function and need to preserve the arguments passed from your decorator down to the decorated function.
Then having the decorator take args and kwargs, and then passing those on makes perfect sense.
Beyond that, it gets a bit tenuous in my opinion. There's definitely more practical uses for args than for kwargs, but I'm sure you find your way.