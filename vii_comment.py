import sublime, sublime_plugin

from datetime import date
from string import Template

class ViiComment(sublime_plugin.TextCommand):
    def run(self, edit):
        self.view.run_command('toggle_comment', {'block': False})
        
        if no_selected_text(self):
            insert_snippet(self)

def no_selected_text(self):
    # In ST2 view.sel() is a sublime.RegionSet
    # In ST3 it's a sublime.Selection
    # They appear to be the same API-wise
    for region in self.view.sel():
        if region.size() > 0:
            return False
    return True

def insert_snippet(self):
    today = date.today().strftime('%m/%d/%y')
    initials = read_initials()
    
    snippet = Template('${initials} - $$1 ${date}').substitute(date=today, initials=initials)
    
    self.view.run_command('insert_snippet', {
        'contents': snippet
    })

def read_initials():
    return sublime.load_settings('vii_comment.sublime-settings').get('initials')
