from robot.libraries.BuiltIn import BuiltIn
from robot.utils import timestr_to_secs

import time


class ExtJSLibrary:

    ROBOT_LIBRARY_SCOPE = 'GLOBAL'
    ROBOT_LIBRARY_VERSION = '0.0.1'

    def __init__(self):
        self._selenium().add_location_strategy('Ext.ComponentQuery', lambda browser, criteria, tag, constraints: self.component_query(criteria))
        self._selenium().add_location_strategy('Ext.DomQuery', lambda browser, criteria, tag, constraints: self.dom_query(criteria))

    def _selenium(self):
        return BuiltIn().get_library_instance('Selenium2Library')

    def component_query(self, query):
        query = query.replace("'", "\\'")
        return self._exec_js("""
            var queryResults = window.Ext.ComponentQuery.query('%s');
            if(queryResults.length > 0)
              return queryResults[0].el.dom;
            else
              return null;
        """ % query)

    def dom_query(self, query):
        return self._exec_js("return window.Ext.DomQuery.selectNode('%s')" % query)

    def wait_until_ext_is_ready(self, timeout=None, error=None):

        # Determine timeout and error
        timeout = timeout or self._selenium().get_selenium_timeout()
        timeout = timestr_to_secs(timeout)
        error = error or 'Ext was not loaded before the specified timeout'

        # Wait for Ext to be ready
        maxtime = time.time() + timeout
        while not self._exec_js("return window.Ext ? true : false"):
            if time.time() > maxtime:
                raise AssertionError(error)
            time.sleep(0.2)

    def _exec_js(self, code):
        return self._selenium().execute_javascript(code)
