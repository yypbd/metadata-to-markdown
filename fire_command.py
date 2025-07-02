import os

from dotenv import load_dotenv

from src.database import Database
from src.markdown import Markdown

load_dotenv()
DATABASE_URL = os.environ.get("DATABASE_URL")

class FireCommand:
    def show_schemas(self):
        database = Database()

        if database.connect(DATABASE_URL):
            return database.get_schemas()
        else:
            return "[error] cannot connect to database"

    def generate_markdown(self, schema = '', relation_type = 'none', pagebreak = False, out_filename = None):
        if out_filename is not None and os.path.exists(out_filename):
            return '[error] Exists - ' + out_filename

        database = Database()
        if not database.connect(DATABASE_URL):
            return "[error] cannot connect to database"

        if database.get_schemas().count == 0:
            return '[error] Schema is empty'

        if schema == '':
            schema = database.get_schemas()[0]

        if schema not in database.get_schemas():
            return '[error] Not exists schemas'

        output = Markdown(database).get(schema, relation_type, pagebreak)
        if out_filename is None:
            return output
        else:
            with open(out_filename, "w") as text_file:
                text_file.write(output)
                text_file.close()

            return "[success] Save markdown to " + out_filename
