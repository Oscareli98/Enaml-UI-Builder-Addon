""" Allows Canopy to open CSV files in the Enaml UI Builder """

from envisage.api import Plugin
from envisage.ui.tasks.api import TaskExtension
from traits.api import List
from pyface.action.api import Action
from pyface.tasks.action.api import SchemaAddition

class ImportPlugin(Plugin):
    """ Allows for Canopy to open CSV files in the Enaml UI Builder """

    # Extension point IDs.
    TASK_EXTENSIONS = 'envisage.ui.tasks.task_extensions'
    COMMANDS = 'canopy.python_frontend.commands'

    # Unique ID for this Plugin.
    id = 'import_addon'

    # User-readable name for this Plugin.
    name = 'Import Addon'



    #### Contributions to extension points made by this plugin ################

    task_extensions = List(contributes_to=TASK_EXTENSIONS)

    def _task_extensions_default(self):
        from import_addon.ui.actions import menu_group_schema

        menu_extension = TaskExtension(
            task_id='canopy.integrated_code_editor',
            actions=[ SchemaAddition(
                path='MenuBar/File',
                after="SaveGroup",
                before="PrintGroup",
                factory=lambda : menu_group_schema,
                id='csv_drop'),
            ],
        )

        return [menu_extension]

    commands = List(contributes_to=COMMANDS)

    def _commands_default(self):
        code =\
"""
import table_import
def callback(df):
    globals()['df'] = df
"""
        code += "table_import.setup('"+self.home+"',callback)"
        return [code]