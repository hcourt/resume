import os
from resume import app
import pprint

if __name__ == '__main__':
    with app.test_request_context():
        from resume.views import *
        func_list = {}
        for rule in app.url_map.iter_rules():
            func_list[rule.rule] = app.view_functions[rule.endpoint].__doc__
        pprint.pprint(func_list)
        print "done"

    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
