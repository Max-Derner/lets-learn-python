The logging library is super powerful.
It doesn't care if you move the files around during runtime what-so-ever, it's more than happy to keep writing to the same file wherever you move it.
The way I have laid out setting up a logger is so that you can simply import the logger itself without having to worry about handlers or anything, just drop logging_set_up.py into your project, import logger and start using it.
There are much much more simple ways of setting it up but the docs are provided.