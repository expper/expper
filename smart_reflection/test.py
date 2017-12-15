import sys
from db_objects import *


if __name__ == "__main__":
    db_name = sys.argv[1]
    m = db_manager(db_name)

    c = m.get_config_object()
    s = m.get_speach_object()
    t = m.get_tags_object()
    p = m.get_speach_object()

    txt = s.get_answer("Hello how are you")
    print (txt)
    txt = s.get_answer("What is your name")
    print (txt)
    txt = s.get_answer("Hello how are you")
    print (txt)
