import six


def exec_file(filename, locals_, globals_):
    try:
        with open(filename, "r") as settings_file:
            six.exec_(settings_file.read(), globals_, locals_)
    except IOError:
        pass
