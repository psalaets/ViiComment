import sublime, sublime_plugin

from datetime import date
from string import Template

# In ST2, param is a sublime.RegionSet. In ST3 it's a sublime.Selection
# They appear to be the same API-wise
def no_selected_text(selection):
    for region in selection:
        if region.size() > 0:
            return False
    return True

def read_initials():
    return sublime.load_settings('vii_comment.sublime-settings').get('initials')

class ViiComment(sublime_plugin.TextCommand):
    def run(self, edit):
        self.view.run_command('toggle_comment')
        
        # insert snippet if there is no selected text
        if no_selected_text(self.view.sel()):
            today = date.today().strftime('%m/%d/%y')
            initials = read_initials()
            
            snippet = Template('${initials} - $$1 ${date}').substitute(date=today, initials=initials)
            
            self.view.run_command('insert_snippet', {
                'contents': snippet
            })
