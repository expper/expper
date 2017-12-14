import sys
from db_objects import *


if __name__ == "__main__":
    db_name = sys.argv[1]
    m = db_manager(db_name)

    c = m.get_config_object()
    s = m.get_speach_object()
    t = m.get_tags_object()
    p = m.get_speach_object()

    #dd = d.get_config_object()
    #ss = d.get_speach_object(dd)
    #dd.set_state("mood", "88")
    #dd = ss.get_config()
    #print(dd.get_state("mood"))

    #print(ss.get_answer({"greet", "how", "you"}))

